function replaceKPatternEverywhere() {
  const pattern = /\(==k\(([^)]+)\)((?:\(=[v|V]\([^)]+\)\([^)]*\)=\))+)==\)/g;

  function parseVSegments(segmentBlock) {
    const vPattern = /\(=([v|V])\(([^)]+)\)\(([^)]*)\)=\)/g;
    const entries = [];
    let match;
    while ((match = vPattern.exec(segmentBlock)) !== null) {
      entries.push({
        active: match[1] === "V",
        value: match[2],
        label: match[3],
      });
    }
    return entries;
  }

  function createReplacementHTML(key, entries) {
    var active = entries.filter((entry) => entry.active);
    var text = active.length > 0 ? active[0].label : key;
    var missing = text.length === 0;
    var values = entries
      .map((entry) => [entry.value, entry.label].join(": "))
      .join(" | ");
    var tooltip = `[${key}] ${values}`;
    if (missing) {
      text = `'${key}' does not exist`;
      tooltip = `You specified '{{< key ${key} >}}' but it does not exist.`;
    }
    return `<span class="keys ${missing ? "missing" : ""} ${text}">
      <span class="icon">
        <sl-tooltip content="${tooltip}" placement="top">
          <sl-icon name="stars"></sl-icon>
        </sl-tooltip>
      </span>
      <span class="value">${text}</span>
    </span>`;
  }

  function walkAndReplace(node) {
    // Ignore <script> and <style>
    if (
      node.nodeType === Node.ELEMENT_NODE &&
      ["SCRIPT", "STYLE"].includes(node.tagName)
    ) {
      return;
    }

    if (node.nodeType === Node.ELEMENT_NODE) {
      // Copy the childNodes array because it can change during iteration
      [...node.childNodes].forEach((child) => walkAndReplace(child));
    }

    const originalText = node.textContent;

    // If no pattern, skip
    if (!pattern.test(originalText)) return;

    const newHTML = originalText.replace(pattern, (_, key, valueBlock) => {
      const parsed = parseVSegments(valueBlock);
      // return valueBlock;
      return createReplacementHTML(key, parsed);
    });

    const temp = document.createElement("div");
    temp.innerHTML = newHTML;

    const parent = node.parentNode;
    const nextSibling = node.nextSibling;
    parent.removeChild(node);

    while (temp.firstChild) {
      parent.insertBefore(temp.firstChild, nextSibling);
    }
  }

  walkAndReplace(document.body);
}

document.addEventListener("DOMContentLoaded", function () {
  replaceKPatternEverywhere();
});
