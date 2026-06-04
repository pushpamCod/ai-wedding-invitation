document.addEventListener("DOMContentLoaded", function () {

    initCardGroup(".style-card");
    initCardGroup(".priority-card");
    initCardGroup(".design-card");

    const form      = document.querySelector(".wedding-form");
    const submitBtn = document.querySelector(".submit-btn");
    if (form && submitBtn) {
        form.addEventListener("submit", function () {
            showLoader();
            submitBtn.textContent = "Generating...";
            submitBtn.disabled    = true;
        });
    }
});

function initCardGroup(selector) {
    const cards = document.querySelectorAll(selector);
    cards.forEach(function (card) {
        card.addEventListener("click", function () {
            cards.forEach(function (c) { c.classList.remove("selected"); });
            card.classList.add("selected");

            // Flash animation on select
            card.style.transition = "none";
            card.style.opacity = "0.7";
            setTimeout(function() {
                card.style.transition = "all 0.25s";
                card.style.opacity = "1";
            }, 80);
        });
    });
    // Set default selected
    const checked = document.querySelector(selector + " input:checked");
    if (checked) checked.closest(selector).classList.add("selected");
}

function toggleCeremony(name) {
    const checkbox = document.getElementById(name + "_enabled");
    const fields   = document.getElementById("fields-" + name);
    if (checkbox && fields) {
        fields.style.display = checkbox.checked ? "block" : "none";

        // Visual feedback on ceremony block
        const block = checkbox.closest(".ceremony-block");
        if (block) {
            block.style.borderColor = checkbox.checked
                ? "rgba(201,169,110,0.7)"
                : "rgba(201,169,110,0.2)";
            block.style.background = checkbox.checked
                ? "rgba(201,169,110,0.06)"
                : "rgba(255,255,255,0.02)";
        }
    }
}

function showLoader() {
    const overlay = document.createElement("div");
    overlay.id = "loading-overlay";
    overlay.innerHTML = `
        <div class="loader-box">
            <div class="loader-rings">
                <div class="ring ring1"></div>
                <div class="ring ring2"></div>
                <div class="ring ring3"></div>
                <div class="loader-heart">&#128141;</div>
            </div>
            <p class="loader-title">Creating Your Invitation</p>
            <p class="loader-subtitle" id="loader-msg">AI is crafting your perfect invitation...</p>
            <div class="loader-dots">
                <span></span><span></span><span></span>
            </div>
        </div>`;
    document.body.appendChild(overlay);

    const messages = [
        "AI is crafting your perfect invitation...",
        "Weaving beautiful words for your big day...",
        "Adding a touch of elegance...",
        "Almost ready — making it perfect...",
        "Putting the final touches..."
    ];
    let i = 0;
    setInterval(function () {
        i = (i + 1) % messages.length;
        const el = document.getElementById("loader-msg");
        if (el) {
            el.style.opacity = "0";
            setTimeout(function () {
                if (el) { el.textContent = messages[i]; el.style.opacity = "1"; }
            }, 300);
        }
    }, 2000);
}
const styleDesignHints = {
    traditional: "Choose your Traditional invitation design",
    modern:      "Choose your Modern invitation design",
    casual:      "Choose your Casual invitation design"
};

function updateDesignLabels(style) {
    const hint = document.getElementById('design-hint');
    if (hint) hint.textContent = styleDesignHints[style] || styleDesignHints.traditional;

    // Scroll to design section smoothly
    const designSection = hint ? hint.closest('.form-section') : null;
    if (designSection) {
        setTimeout(() => {
            designSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }, 200);
    }
}