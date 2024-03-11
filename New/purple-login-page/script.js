// script.js

function redirectToWelcome() {
    // Redirect to the welcome page
    window.location.href = "welcome.html";
}

document.addEventListener("DOMContentLoaded", function () {
    // Add click event listener to the "Parents login" button
    const parentsLoginButton = document.getElementById("parentsLoginButton");

    if (parentsLoginButton) {
        parentsLoginButton.addEventListener("click", function () {
            // Trigger the redirection to the welcome page
            redirectToWelcome();
        });
    }
});
document.addEventListener("DOMContentLoaded", function () {
    const signInButton = document.getElementById("signInButton");

    if (signInButton) {
        signInButton.addEventListener("click", function () {
            // Get the values of email and password fields
            const emailValue = document.getElementById("emailForm").value;
            const passwordValue = document.getElementById("passwordForm").value;

            // Check if both email and password are not empty and match specific values
            if (emailValue === "student@nexus.in" && passwordValue === "nexus") {
                // Redirect to the dashboard.html file
                window.location.href = "Dashboard.html";
            } else {
                // Show an alert or handle the case when credentials are incorrect
                alert("Invalid email or password");
            }
        });
    }
});


