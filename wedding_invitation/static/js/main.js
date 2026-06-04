// main.js — Handles style card selection UI

document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ JavaScript loaded");

    // === Style Card Selection ===
    // When user clicks a style card, highlight it visually
    // (CSS alone can't style a parent from a child's :checked state easily)

    const styleCards = document.querySelectorAll(".style-card");

    styleCards.forEach(function (card) {
        card.addEventListener("click", function () {
            // Remove 'selected' class from ALL cards first
            styleCards.forEach(function (c) {
                c.classList.remove("selected");
            });

            // Add 'selected' class to the one just clicked
            card.classList.add("selected");
        });
    });

    // Set the default selected card on page load
    // (the one whose radio input is checked by default)
    const defaultChecked = document.querySelector(".style-card input[type='radio']:checked");
    if (defaultChecked) {
        // .closest() walks up the DOM tree to find the parent .style-card
        defaultChecked.closest(".style-card").classList.add("selected");
    }

    // === Form Submit Feedback ===
    const form = document.querySelector(".wedding-form");
    const submitBtn = document.querySelector(".submit-btn");

    if (form && submitBtn) {
        form.addEventListener("submit", function () {
            submitBtn.textContent = "⏳ Generating...";
            submitBtn.disabled = true;
        });
    }
});