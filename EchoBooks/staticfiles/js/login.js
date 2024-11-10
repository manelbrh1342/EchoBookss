document.addEventListener("DOMContentLoaded", function() {
    const signupForm = document.getElementById("signup-form");
    const loginForm = document.getElementById("login-form");
    const signupLink = document.getElementById("signup-link");
    const loginLink = document.getElementById("login-link");

    // Initially show the login form
    loginForm.classList.add("active");

    // Function to show the signup form and hide the login form with smooth transition
    signupLink.addEventListener("click", function() {
        loginForm.classList.remove("active");

        // Wait for the transition to finish before hiding the login form
        setTimeout(() => {
            loginForm.style.display = "none"; // Hide login form after fade-out
            signupForm.style.display = "flex"; // Show signup form
            signupForm.classList.add("active"); // Apply transition to signup form
        }, 500); // Matches the CSS transition duration (0.5s)
    });

    // Function to show the login form and hide the signup form with smooth transition
    loginLink.addEventListener("click", function() {
        signupForm.classList.remove("active");

        // Wait for the transition to finish before hiding the signup form
        setTimeout(() => {
            signupForm.style.display = "none"; // Hide signup form after fade-out
            loginForm.style.display = "flex"; // Show login form
            loginForm.classList.add("active"); // Apply transition to login form
        }, 500); // Matches the CSS transition duration (0.5s)
    });
});

