document.addEventListener('DOMContentLoaded', function() {
    var showPasswordToggle = document.getElementById('show-password-toggle');
    var passwordField = document.getElementById('password-field');

    showPasswordToggle.addEventListener('click', function() {
        if (passwordField.type === 'password') {
            passwordField.type = 'text';
            showPasswordToggle.classList.remove('fa-eye');
            showPasswordToggle.classList.add('fa-eye-slash');
        } else {
            passwordField.type = 'password';
            showPasswordToggle.classList.remove('fa-eye-slash');
            showPasswordToggle.classList.add('fa-eye');
        }
    });
});
