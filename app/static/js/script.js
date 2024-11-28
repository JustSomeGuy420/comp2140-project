document.addEventListener("DOMContentLoaded", () => {
    const confirmButtons = document.querySelectorAll(".confirm-submit");
    const modal = document.getElementById("confirmationModal");
    const modalConfirmButton = document.getElementById("modalConfirm");
    const modalCancelButton = document.getElementById("modalCancel");
    let formToSubmit = null;

    confirmButtons.forEach(button => {
        button.addEventListener("click", event => {
            event.preventDefault(); // Prevent form submission
            formToSubmit = event.target.closest("form"); // Store the form to submit
            modal.style.display = "block"; // Show the modal
        });
    });

    // Confirm button inside the modal
    modalConfirmButton.addEventListener("click", () => {
        if (formToSubmit) {
            formToSubmit.submit(); // Submit the stored form
        }
        modal.style.display = "none"; // Hide the modal
    });

    // Cancel button inside the modal
    modalCancelButton.addEventListener("click", () => {
        modal.style.display = "none"; // Hide the modal
    });
});
