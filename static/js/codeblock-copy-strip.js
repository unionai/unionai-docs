// Strip leading "$ " from shell/bash code blocks when copying.
// Shoelace's sl-copy-button: "from" overrides "value", so we must
// remove "from" and set "value" with the cleaned text. We also wait
// for the custom element to be defined since Shoelace loads as a module.
document.addEventListener("DOMContentLoaded", function () {
  customElements.whenDefined("sl-copy-button").then(function () {
    document
      .querySelectorAll(
        '.codeblock[data-code-lang="shell"], .codeblock[data-code-lang="bash"]'
      )
      .forEach(function (block) {
        var btn = block.querySelector("sl-copy-button");
        if (!btn) return;
        var codeEl = block.querySelector(".code");
        if (!codeEl) return;
        var raw = codeEl.textContent;
        var cleaned = raw
          .split("\n")
          .map(function (line) {
            return line.replace(/^\$ /, "");
          })
          .join("\n");
        btn.removeAttribute("from");
        btn.value = cleaned;
      });
  });
});
