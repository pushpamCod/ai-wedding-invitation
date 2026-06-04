import os
import re

BASE = r"C:\PROJECTS\AI wedding card"

# ── 1. Fix index.html ──────────────────────────────────────
idx = os.path.join(BASE, "templates", "index.html")
c = open(idx, encoding="utf-8").read()

c = re.sub(
    r'<!-- ── SECTION 2: GUEST PRIORITY ──.*?</div>\s*</div>\s*</div>',
    '',
    c, flags=re.DOTALL
)

open(idx, "w", encoding="utf-8").write(c)
print("index.html done")

# ── 2. Fix app.py ──────────────────────────────────────────
app_path = os.path.join(BASE, "app.py")
c = open(app_path, encoding="utf-8").read()

# Remove guest_priority form.get line
c = re.sub(r"\s*guest_priority\s*=\s*request\.form\.get\([^)]+\)\s*\n", "\n", c)

# Remove priority_display dict and pd assignment
c = re.sub(
    r"\s*# Priority display.*?pd\[1\]\s*\n",
    "\n", c, flags=re.DOTALL
)

# Remove from wedding_details dict
c = re.sub(r'\s*"guest_priority"\s*:\s*guest_priority\s*,\s*\n', "\n", c)
c = re.sub(r'\s*"priority_title"\s*:\s*pd\[0\][^\n]*\n', "\n", c)
c = re.sub(r'\s*"priority_tagline"\s*:\s*pd\[1\][^\n]*\n', "\n", c)

open(app_path, "w", encoding="utf-8").write(c)
print("app.py done")

# ── 3. Fix all card templates ─────────────────────────────
cards = [
    ("card_peacock.html",  "The families joyfully invite you to celebrate", "#8a6a20"),
    ("card_purple.html",   "The families joyfully invite you",              "#9a7a30"),
    ("card_sindoor.html",  "The families joyfully invite you",              "#9a5a20"),
    ("card_midnight.html", "The families joyfully invite you",              "#6070b0"),
    ("card_rose.html",     "The families joyfully invite you",              "#b06080"),
    ("card_forest.html",   "The families joyfully invite you",              "#508050"),
]

for fname, invite_text, fill_color in cards:
    path = os.path.join(BASE, "templates", fname)
    if not os.path.exists(path):
        print(f"SKIP (not found): {fname}")
        continue

    c = open(path, encoding="utf-8").read()

    # Replace two-line priority block if it exists
    c = re.sub(
        r'<text[^>]*y="210"[^>]*>.*?priority_title.*?</text>\s*'
        r'<text[^>]*y="226"[^>]*>.*?priority_tagline.*?</text>',
        f'<text x="350" y="220" text-anchor="middle" '
        f'font-family="\'Cormorant Garamond\',Georgia,serif" '
        f'font-size="10" fill="{fill_color}">{invite_text}</text>',
        c, flags=re.DOTALL
    )

    open(path, "w", encoding="utf-8").write(c)
    print(f"Fixed: {fname}")

print("\nAll done! Run: python app.py")