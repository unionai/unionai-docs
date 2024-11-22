document.addEventListener('DOMContentLoaded', function() {
    // expand sidebar items
    function expandSidebarItems() {
      // Get the first element with children in the sidebar
      const sidebar = document.querySelector('.bd-links');
      if (!sidebar) return;

      // find the first item that has a toctree-toggle (indicating it has children)
      const firstParentItem = sidebar.querySelector('.toctree-toggle')?.closest('li');
      if (!firstParentItem) return;

      // expand an item and all its children
      function expandItem(item) {
        // find toggle button and click it if it's collapsed
        const toggleBtn = item.querySelector('.toctree-toggle');
        if (toggleBtn) {
          const isCollapsed = !item.querySelector('ul')?.style.display || 
                            item.querySelector('ul')?.style.display === 'none';
          if (isCollapsed) {
            toggleBtn.click();
          }
        }

        // expand all child items
        const childItems = item.querySelectorAll('li');
        childItems.forEach(child => {
          const childToggle = child.querySelector('.toctree-toggle');
          if (childToggle) {
            const isChildCollapsed = !child.querySelector('ul')?.style.display || 
                                   child.querySelector('ul')?.style.display === 'none';
            if (isChildCollapsed) {
              childToggle.click();
            }
          }
        });
      }

      // Expand the first parent item and all its children
      expandItem(firstParentItem);
    }

    // let's run the expansion after a short delay to ensure sidebar is fully initialized :)
    setTimeout(expandSidebarItems, 100);
  });

//   TODO!! - ensure this only runs once. Problem - it runs on every page load. 
//   Possible solution - add a check to see if the sidebar has already been expanded.