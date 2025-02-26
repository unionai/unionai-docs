document.addEventListener("DOMContentLoaded", function () {
  const expandLevel =
    typeof window.expandLevel !== "undefined" ? window.expandLevel : 1;

  /**
   * 0  => All details remain closed.
   * 1  => Open level-1 details only.
   * 2  => Open level-1 and level-2 details.
   * -1 => Open all levels.
   */

  /**
   * recursively open or close <details> elements based on the current nesting level.
   * @param {HTMLElement} ulElement - The current <ul> element containing <li> items.
   * @param {number} currentLevel - The current nesting level (starting at 1).
   */
  function openDetailsRecursive(ulElement, currentLevel) {
    // Get all direct <li> children that have children.
    const liItems = ulElement.querySelectorAll(":scope > li.has-children");
    liItems.forEach((li) => {
      const details = li.querySelector("details");
      if (details) {
        // determine whether to open this <details> element.
        // if expandLevel is -1, open everything.
        // else, open the details only if the current level is less than or equal to expandLevel.
        if (
          expandLevel === -1 ||
          (expandLevel > 0 && currentLevel <= expandLevel)
        ) {
          details.open = true;
        } else {
          details.open = false;
        }
        // if there is a nested <ul> (for deeper levels), process it recursively.
        const nestedUl = details.querySelector("ul");
        if (nestedUl) {
          openDetailsRecursive(nestedUl, currentLevel + 1);
        }
      }
    });
  }

  /**
   * Scrolls the active link in the sidebar into view.
   * tries several selectors: the link may have aria-current="page", or a class of "current" or "active".
   */
  function scrollActiveIntoView() {
    // attempt to locate the active link.
    let activeLink =
      document.querySelector('.bd-links a[aria-current="page"]') ||
      document.querySelector(".bd-links a.current") ||
      document.querySelector(".bd-links .active");
    if (activeLink) {
      // Scroll the active element smoothly into view, centering it within the scrollable container.
      activeLink.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  }

  /**
   * configures the sidebar:
   * - expands details recursively based on the desired expandLevel.
   * - marks the sidebar as initialized so this logic runs only once.
   * - then scrolls the active link into view.
   */
  function configureSidebar() {
    const sidebar = document.querySelector(".bd-links");
    if (!sidebar) return;

    // prevent duplicate processing.
    if (sidebar.dataset.sidebarInitialized === "true") return;

    // locate the main <ul> (assuming it has a class of .bd-sidenav).
    const mainUl = sidebar.querySelector("ul.bd-sidenav");
    if (mainUl) {
      // Begin processing at level 1.
      openDetailsRecursive(mainUl, 1);
    }

    // mark the sidebar as having been initialized.
    sidebar.dataset.sidebarInitialized = "true";

    // add scrolling slightly to ensure the sidebar has rendered fully.
    setTimeout(scrollActiveIntoView, 100);
  }

  // dd delay: run the config after a short delay to ensure that the sidebar is fully rendered.
  setTimeout(configureSidebar, 100);
});
