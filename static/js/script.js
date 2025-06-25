// static/js/script.js

document.addEventListener('DOMContentLoaded', () => {
    // 1. Focus on input field when page loads
    const input = document.querySelector('input[name="content"]');
    if (input) input.focus();

    // 2. Add confirmation before deleting a task
    document.querySelectorAll('a.btn-outline-danger').forEach(button => {
        button.addEventListener('click', function (event) {
            const confirmed = confirm("Are you sure you want to delete this task?");
            if (!confirmed) {
                event.preventDefault();
            }
        });
    });

    // 3. Show a basic toast for actions (optional)
    const toast = document.createElement("div");
    toast.id = "toast";
    toast.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: rgba(0,0,0,0.8);
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        display: none;
        z-index: 9999;
    `;
    document.body.appendChild(toast);

    function showToast(message) {
        toast.textContent = message;
        toast.style.display = "block";
        setTimeout(() => {
            toast.style.display = "none";
        }, 2000);
    }

    // 4. Optionally show a toast on task add (based on URL)
    if (window.location.search.includes("added=true")) {
        showToast("Task added successfully!");
    }
});
