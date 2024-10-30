window.addEventListener("DOMContentLoaded", function() {
    // Select all <a> elements with class "external"
    var externalLinks = document.querySelectorAll("a.external");

    // Loop through each <a> element with class "external"
    externalLinks.forEach(function(link) {
        // Set the target attribute to "_blank"
        link.setAttribute("target", "_blank");
    });

    // hide login/signup buttons on BYOC pages
    if (window.location.pathname.includes('/byoc/')) {
        const loginButton = document.querySelector('.unionai-btn-login');
        const signupButton = document.querySelector('.unionai-btn-signup');
        
        if (loginButton) {
            loginButton.parentElement.style.display = 'none';
        }
        if (signupButton) {
            signupButton.parentElement.style.display = 'none';
        }
        
        //  hide vertical separator if it's the last one
        const separators = document.querySelectorAll('.vertical-separator');
        if (separators.length > 0) {
            separators[separators.length - 1].style.display = 'none';
        }
    }
});