window.addEventListener("DOMContentLoaded", function () {
  // Select all <a> elements with class "external"
  var externalLinks = document.querySelectorAll("a.external");

  // Loop through each <a> element with class "external"
  externalLinks.forEach(function (link) {
    // Set the target attribute to "_blank"
    link.setAttribute("target", "_blank");
  });

  // Remove the default search dialog if it exists (on CMD + K)
  // This collides with Algolia's search dialog
  const searchDialog = document.getElementById("pst-search-dialog");
  if (searchDialog) {
    searchDialog.remove();
  }

  // New variant selector logic
  function setupVariantSelector() {
    // Handle dropdown toggling
    document.addEventListener("click", function (event) {
      const dropdowns = document.querySelectorAll(".variant-dropdown-content");
      if (!event.target.closest(".variant-selector")) {
        dropdowns.forEach((dropdown) => {
          dropdown.classList.remove("show");
        });
      }
    });

    // Setup click handlers for variant dropdown buttons
    const variantButtons = document.querySelectorAll(
      ".variant-dropdown-button"
    );
    variantButtons.forEach((button) => {
      button.addEventListener("click", function (event) {
        event.stopPropagation();
        const dropdown = this.nextElementSibling;
        const isOpen = dropdown.classList.contains("show");

        // Close all dropdowns
        document.querySelectorAll(".variant-dropdown-content").forEach((d) => {
          d.classList.remove("show");
        });

        // Toggle current dropdown
        if (!isOpen) {
          dropdown.classList.add("show");
        }
      
      });
    });

    // Prevent dropdown from closing when clicking inside it
    document
      .querySelectorAll(".variant-dropdown-content")
      .forEach((dropdown) => {
        dropdown.addEventListener("click", function (event) {
          event.stopPropagation();
        });
      });
  }

  // Initialize variant selector
//   setupVariantSelector();
});
