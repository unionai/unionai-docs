// Function to set the theme based on preference
function setTheme(theme) {
  document.documentElement.setAttribute("data-theme", theme);
  localStorage.setItem("theme", theme);

  // Set the theme in the HTML element
  document.documentElement.className = theme === "dark" ? "sl-theme-dark" : "";

  // Set cookie for 24 hours
  const date = new Date();
  date.setTime(date.getTime() + 24 * 60 * 60 * 1000);
  document.cookie = `theme=${theme};expires=${date.toUTCString()};path=/`;
}

// Function to get cookie value
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
  return null;
}

// Check for saved theme preference
const savedTheme = localStorage.getItem("theme") || getCookie("theme");

// Check for system preference if no saved preference
if (!savedTheme && window.matchMedia) {
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  setTheme(prefersDark ? "dark" : "light");
} else if (savedTheme) {
  setTheme(savedTheme);
} else {
  setTheme("light"); // Default to light if no preference detected
}
