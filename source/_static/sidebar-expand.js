document.addEventListener('DOMContentLoaded', function() {
  const expandLevel = (typeof window.expandLevel !== 'undefined') ? window.expandLevel : 1;

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
    const liItems = ulElement.querySelectorAll(':scope > li.has-children');
    liItems.forEach(li => {
      const details = li.querySelector('details');
      if (details) {
        // determine whether to open this <details> element.
        // if expandLevel is -1, open everything.
        // else, open the details only if the current level is less than or equal to expandLevel.
        if (expandLevel === -1 || (expandLevel > 0 && currentLevel <= expandLevel)) {
          details.open = true;
        } else {
          details.open = false;
        }
        // if there is a nested <ul> (for deeper levels), process it recursively.
        const nestedUl = details.querySelector('ul');
        if (nestedUl) {
          openDetailsRecursive(nestedUl, currentLevel + 1);
        }
      }
    });
  }

  function configureSidebar() {
    
    const sidebar = document.querySelector('.bd-links');
    if (!sidebar) return;

    // chck whether config has already been applied.
    if (sidebar.dataset.sidebarInitialized === 'true') return;


    const mainUl = sidebar.querySelector('ul.bd-sidenav');
    if (mainUl) {
      // init processing at level 1.
      openDetailsRecursive(mainUl, 1);
    }

    // mark the sidebar as init: prevent fn from running again.
    sidebar.dataset.sidebarInitialized = 'true';
  }

  // add delay: run the config after a short delay to ensure that the sidebar is fully rendered.
  setTimeout(configureSidebar, 100);
});