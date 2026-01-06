/**
 * Automatic linking for inline code elements.
 * Loads the linkmap JSON and adds links to matching inline code.
 */

(function() {
  // Get the site base path by looking at existing links
  const getBasePath = () => {
    // Find any link in the page and extract the base path from it
    const link = document.querySelector('a[href^="/"]');
    if (link) {
      const href = link.getAttribute('href');
      // Try to match common base path patterns like /dev/site/p/
      const match = href.match(/^(\/[^\/]+\/[^\/]+\/[^\/]+)/);
      if (match) {
        return match[1];
      }
    }

    // Fallback: try to infer from current pathname
    const path = window.location.pathname;
    const match = path.match(/^(\/[^\/]+\/[^\/]+\/[^\/]+)/);
    return match ? match[1] : '';
  };

  // Load linkmap and process inline code
  const processInlineCode = async () => {
    try {
      const basePath = getBasePath();

      // Construct the JSON URL - it's at the root of the site
      const jsonURL = basePath ? `${basePath}/flytesdk-linkmap.json` : '/flytesdk-linkmap.json';
      const response = await fetch(jsonURL);

      if (!response.ok) {
        console.warn('Could not load linkmap for inline code linking');
        return;
      }

      const linkmap = await response.json();

      // More specific selector to exclude code blocks and syntax-highlighted code
      // Only target inline code that's not inside:
      // 1. <pre> elements (code blocks)
      // 2. Elements with syntax highlighting classes
      // 3. Elements inside .codeblock containers
      const codeElements = document.querySelectorAll('code:not(.codeblock code):not(.highlight code):not(pre code):not([class*="language-"]):not([class*="chroma"])');

      codeElements.forEach(codeEl => {
        // Skip if this code element is inside a syntax-highlighted container
        if (codeEl.closest('.highlight, .codeblock, pre, .chroma')) {
          return;
        }

        // Skip if already processed (has a link parent)
        if (codeEl.parentElement.tagName === 'A') {
          return;
        }

        const text = codeEl.textContent.trim();

        // Skip empty or very short text
        if (!text || text.length < 2) {
          return;
        }

        // Check for magic marker syntax [[...]]
        const magicMatch = text.match(/^\[\[(.+?)\]\]$/);
        if (magicMatch) {
          const innerText = magicMatch[1];
          const displayText = innerText; // What we'll show (without brackets)

          // Strip trailing () for matching
          const textForMatching = innerText.endsWith('()') ? innerText.slice(0, -2) : innerText;

          // Check if it's a ClassName.method pattern (for magic matching)
          const classMethodMatch = textForMatching.match(/^([^.]+)\.(.+)$/);
          if (classMethodMatch) {
            const className = classMethodMatch[1];
            const methodName = classMethodMatch[2];

            // Try to find identifier ending with the class name
            if (linkmap.identifiers) {
              for (const [fullIdentifier, url] of Object.entries(linkmap.identifiers)) {
                const lastPart = fullIdentifier.split('.').pop();
                if (lastPart === className) {
                  // Found the class, append #methodName to the URL
                  wrapWithLink(codeEl, url + '#' + methodName, displayText);
                  return;
                }
              }
            }
          }

          // Try to match by the last part after dots
          let matched = false;

          // First try exact match in methods
          if (linkmap.methods) {
            for (const [fullMethod, url] of Object.entries(linkmap.methods)) {
              const lastPart = fullMethod.split('.').pop();
              if (lastPart === textForMatching) {
                wrapWithLink(codeEl, url, displayText);
                matched = true;
                break;
              }
            }
          }

          // If not matched, try identifiers
          if (!matched && linkmap.identifiers) {
            for (const [fullIdentifier, url] of Object.entries(linkmap.identifiers)) {
              const lastPart = fullIdentifier.split('.').pop();
              if (lastPart === textForMatching) {
                wrapWithLink(codeEl, url, displayText);
                matched = true;
                break;
              }
            }
          }

          // If matched, we already wrapped it with a link, so return
          if (matched) {
            return;
          }
        }

        // Regular matching (no magic markers)
        // Strip trailing () for matching methods
        const textForMatching = text.endsWith('()') ? text.slice(0, -2) : text;

        // Check if it's a ClassName.method or fully.qualified.ClassName.method pattern
        const classMethodMatch = textForMatching.match(/^(.+)\.(.+)$/);
        if (classMethodMatch) {
          const classPart = classMethodMatch[1];
          const methodName = classMethodMatch[2];

          // Try exact match first (fully qualified)
          if (linkmap.identifiers && linkmap.identifiers[classPart]) {
            // Found the class, append #methodName to the URL
            wrapWithLink(codeEl, linkmap.identifiers[classPart] + '#' + methodName, text);
            return;
          }

          // Try to find identifier ending with the class name (for partial matches)
          if (linkmap.identifiers) {
            for (const [fullIdentifier, url] of Object.entries(linkmap.identifiers)) {
              const lastPart = fullIdentifier.split('.').pop();
              if (lastPart === classPart) {
                // Found the class, append #methodName to the URL
                wrapWithLink(codeEl, url + '#' + methodName, text);
                return;
              }
            }
          }
        }

        // Check if it matches a method
        if (linkmap.methods && linkmap.methods[textForMatching]) {
          wrapWithLink(codeEl, linkmap.methods[textForMatching], text);
          return;
        }

        // Check if it matches an identifier
        if (linkmap.identifiers && linkmap.identifiers[textForMatching]) {
          wrapWithLink(codeEl, linkmap.identifiers[textForMatching], text);
          return;
        }
      });
    } catch (error) {
      console.error('Error processing inline code links:', error);
    }
  };

  // Wrap a code element with a link
  const wrapWithLink = (codeEl, url, text) => {
    const basePath = getBasePath();
    const fullURL = `${basePath}${url}`;

    // Preserve any existing classes from the original code element
    const existingClasses = codeEl.className;

    // Create link element
    const link = document.createElement('a');
    link.href = fullURL;

    // Create new code element with preserved classes
    const newCode = document.createElement('code');
    if (existingClasses) {
      newCode.className = existingClasses;
    }
    newCode.textContent = text;

    // Wrap code in link
    link.appendChild(newCode);

    // Replace original code element with linked version
    codeEl.parentNode.replaceChild(link, codeEl);
  };

  // Wait for syntax highlighting to complete before processing
  const waitForSyntaxHighlighting = () => {
    return new Promise((resolve) => {
      // Use MutationObserver to wait for DOM changes to settle
      let timeoutId;
      const observer = new MutationObserver(() => {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => {
          observer.disconnect();
          resolve();
        }, 100);
      });

      observer.observe(document.body, {
        childList: true,
        subtree: true,
        attributes: true,
        attributeFilter: ['class']
      });

      // Fallback timeout in case no changes are detected
      setTimeout(() => {
        observer.disconnect();
        resolve();
      }, 1000);
    });
  };

  // Initialize the linking process
  const initialize = async () => {
    // Wait for syntax highlighting to complete
    await waitForSyntaxHighlighting();
    // Then process inline code
    await processInlineCode();
  };

  // Run when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initialize);
  } else {
    initialize();
  }
})();
