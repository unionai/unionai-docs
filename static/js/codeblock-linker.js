/**
 * Client-side autolinking for Python code blocks.
 * Loads linkmap JSON files and wraps matching identifiers in <a> tags
 * by walking Chroma-highlighted <span> elements with semantic CSS classes.
 */
(function() {
  const getBasePath = () => {
    const link = document.querySelector('a[href^="/"]');
    if (link) {
      const href = link.getAttribute('href');
      const match = href.match(/^(\/[^\/]+\/[^\/]+\/[^\/]+)/);
      if (match) return match[1];
    }
    const path = window.location.pathname;
    const match = path.match(/^(\/[^\/]+\/[^\/]+\/[^\/]+)/);
    return match ? match[1] : '';
  };

  const loadLinkmaps = async (basePath) => {
    const sources = window.__LINKMAP_SOURCES || [];
    const linkmapFiles = sources.map(s => `${s}-linkmap.json`);
    const merged = { packages: {}, identifiers: {}, methods: {} };

    for (const filename of linkmapFiles) {
      try {
        const url = basePath ? `${basePath}/${filename}` : `/${filename}`;
        const response = await fetch(url);
        if (response.ok) {
          const data = await response.json();
          Object.assign(merged.packages, data.packages || {});
          Object.assign(merged.identifiers, data.identifiers || {});
          Object.assign(merged.methods, data.methods || {});
        }
      } catch (e) {
        // Silently ignore missing linkmaps
      }
    }
    return merged;
  };

  // Chroma CSS classes for name tokens (candidates for linking)
  const NAME_CLASSES = new Set(['n', 'nc', 'nf', 'nn', 'nd', 'nb', 'ne', 'na', 'nx', 'fm']);
  // Chroma CSS classes to skip (strings and comments)
  const SKIP_CLASSES = new Set([
    's', 's1', 's2', 'sa', 'sb', 'sc', 'sd', 'se', 'sf', 'sh', 'si', 'dl',
    'c', 'c1', 'cm', 'cp', 'ch', 'cs'
  ]);

  // Parse "from X import Y, Z" and "import X" statements
  const parseImports = (text) => {
    const symbols = {}; // shortName -> fullQualifiedName
    const packages = {}; // alias -> packageName

    // "from X import Y, Z" style
    const fromImportRe = /^from\s+([\w.]+)\s+import\s+(.+)$/gm;
    let match;
    while ((match = fromImportRe.exec(text)) !== null) {
      const pkg = match[1];
      const names = match[2].split(',').map(s => s.trim().split(/\s+as\s+/));
      for (const parts of names) {
        const importedName = parts[0].trim();
        const alias = parts.length > 1 ? parts[1].trim() : importedName;
        if (importedName && /^\w+$/.test(importedName)) {
          symbols[alias] = `${pkg}.${importedName}`;
        }
      }
    }

    // "import X" and "import X as Y" style
    const importRe = /^import\s+([\w.]+)(?:\s+as\s+(\w+))?$/gm;
    while ((match = importRe.exec(text)) !== null) {
      const pkg = match[1];
      const alias = match[2] || pkg;
      packages[alias] = pkg;
    }

    return { symbols, packages };
  };

  // Build a map of name -> URL for a given code block
  const buildMatchSet = (text, imports, linkmap) => {
    const matches = {}; // name -> url
    const { symbols, packages } = imports;

    // "from X import Y": check if full qualified name is in the linkmap
    for (const [shortName, fullName] of Object.entries(symbols)) {
      if (linkmap.identifiers[fullName]) {
        matches[shortName] = linkmap.identifiers[fullName];
      }
    }

    // "import X": add the package name itself if it's in packages linkmap
    for (const [alias, pkg] of Object.entries(packages)) {
      if (linkmap.packages[pkg]) {
        matches[alias] = linkmap.packages[pkg];
      }
      // Also add all pkg.* identifiers by their short name
      const prefix = pkg + '.';
      for (const [fullName, url] of Object.entries(linkmap.identifiers)) {
        if (fullName.startsWith(prefix)) {
          const shortName = fullName.slice(prefix.length);
          // Only single-level names (not nested like "app.AppEndpoint")
          if (/^\w+$/.test(shortName)) {
            matches[shortName] = url;
          }
        }
      }
    }

    // Fully-qualified names that appear literally in the code text
    for (const [fullName, url] of Object.entries(linkmap.identifiers)) {
      if (text.includes(fullName)) {
        matches[fullName] = url;
      }
    }

    return matches;
  };

  const hasNameClass = (span) => {
    const cls = span.className;
    if (!cls) return false;
    return cls.split(/\s+/).some(c => NAME_CLASSES.has(c));
  };

  const processCodeBlocks = async () => {
    try {
      const basePath = getBasePath();
      const linkmap = await loadLinkmaps(basePath);

      if (Object.keys(linkmap.identifiers).length === 0 &&
          Object.keys(linkmap.methods).length === 0) {
        return;
      }

      const codeEls = document.querySelectorAll(
        '.codeblock code[data-syntax="python"], .codeblock code.syntax-python'
      );
      if (codeEls.length === 0) return;

      codeEls.forEach(codeEl => {
        const text = codeEl.textContent;
        const imports = parseImports(text);
        const matchSet = buildMatchSet(text, imports, linkmap);

        if (Object.keys(matchSet).length === 0) return;

        // Sort keys longest-first to prefer longer matches
        const sortedKeys = Object.keys(matchSet).sort((a, b) => b.length - a.length);

        // Collect name spans in document order (excluding line/cl wrapper spans)
        const allSpans = Array.from(codeEl.querySelectorAll('span'));

        for (let i = 0; i < allSpans.length; i++) {
          const span = allSpans[i];
          if (!hasNameClass(span)) continue;
          if (span.closest('a')) continue;

          const spanText = span.textContent;
          const textForMatch = spanText.startsWith('@') ? spanText.slice(1) : spanText;

          // Try to build a dotted name by looking ahead: name.name.name...
          // Chroma emits: <span class="n">pkg</span><span class="o">.</span><span class="n">Name</span>
          let dottedName = textForMatch;
          let dottedSpans = [span]; // spans to coalesce
          let dotSpans = [];        // the "." operator spans between names
          let j = i + 1;
          while (j + 1 < allSpans.length) {
            const dotSpan = allSpans[j];
            const nextSpan = allSpans[j + 1];
            // Check for operator "." followed by a name span
            if (dotSpan.textContent === '.' &&
                dotSpan.className.split(/\s+/).some(c => c === 'o') &&
                hasNameClass(nextSpan)) {
              const candidate = dottedName + '.' + nextSpan.textContent;
              // Only extend if the longer dotted name exists in the matchSet
              if (matchSet[candidate]) {
                dottedName = candidate;
                dotSpans.push(dotSpan);
                dottedSpans.push(nextSpan);
                j += 2;
                continue;
              }
            }
            break;
          }

          // Check if the (possibly dotted) name matches
          let url = matchSet[dottedName];
          if (url) {
            const fullURL = `${basePath}${url}`;
            const link = document.createElement('a');
            link.href = fullURL;
            // Insert link before the first span
            span.parentNode.insertBefore(link, span);
            // Move all spans (names and dots) inside the link
            link.appendChild(span);
            for (let k = 0; k < dotSpans.length; k++) {
              link.appendChild(dotSpans[k]);
              link.appendChild(dottedSpans[k + 1]);
            }
            // Skip past the spans we just consumed
            i = j - 1;
            continue;
          }

          // No dotted match — try single span match
          for (const key of sortedKeys) {
            if (textForMatch === key) {
              const fullURL = `${basePath}${matchSet[key]}`;
              const link = document.createElement('a');
              link.href = fullURL;
              span.parentNode.insertBefore(link, span);
              link.appendChild(span);
              break;
            }
          }
        }
      });
    } catch (error) {
      console.error('Error processing code block links:', error);
    }
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', processCodeBlocks);
  } else {
    processCodeBlocks();
  }
})();
