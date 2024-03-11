function validateAndRedirect() {
    const password = document.getElementById("passwordForm").value;
    const confirmPassword = document.getElementById("confirmPasswordForm").value;

    if (password === "parent@nexus" && password === confirmPassword) {
        // Redirect to the dashboard.html file
        window.location.href = "Dashboard.html";
    } else {
        alert("Passwords do not match or incorrect password");
    }
}