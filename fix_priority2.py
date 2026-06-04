import os
import re
import json

BASE = r"C:\PROJECTS\AI wedding card"

# =========================================================
# 1. REMOVE PRIORITY SECTION FROM index.html
# =========================================================
idx = os.path.join(BASE, "templates", "index.html")

if os.path.exists(idx):
    with open(idx, encoding="utf-8") as f:
        c = f.read()

    c = re.sub(
        r"<!-- ── SECTION 2: GUEST PRIORITY ──.*?</div>\s*</div>\s*</div>",
        "",
        c,
        flags=re.DOTALL,
    )

    with open(idx, "w", encoding="utf-8") as f:
        f.write(c)

    print("✅ index.html - priority section removed")
else:
    print("⚠️ index.html not found")


# =========================================================
# 2. REMOVE PRIORITY FROM app.py
# =========================================================
app_path = os.path.join(BASE, "app.py")

if os.path.exists(app_path):
    with open(app_path, encoding="utf-8") as f:
        c = f.read()

    # Remove form.get line
    c = c.replace(
        "    guest_priority= request.form.get('guest_priority', 'general')", ""
    )
    c = c.replace(
        '    guest_priority = request.form.get("guest_priority", "general")', ""
    )

    # Remove priority_display block
    c = re.sub(
        r"    # Priority display.*?\"priority_tagline\": pd\[1\],\s*",
        "",
        c,
        flags=re.DOTALL,
    )

    # Remove from wedding_details dict
    c = c.replace('        "guest_priority":   guest_priority,\n', "")
    c = c.replace('        "guest_priority":  guest_priority,\n', "")
    c = c.replace('        "priority_title":   pd[0],\n', "")
    c = c.replace('        "priority_tagline": pd[1],\n', "")

    with open(app_path, "w", encoding="utf-8") as f:
        f.write(c)

    print("✅ app.py - priority removed")
else:
    print("⚠️ app.py not found")


# =========================================================
# 3. FIX CARD TEMPLATES
# =========================================================
templates = [
    ("card_peacock.html",  "The families joyfully invite you to celebrate", "#8a6a20"),
    ("card_purple.html",   "The families joyfully invite you", "#9a7a30"),
    ("card_sindoor.html",  "The families joyfully invite you", "#9a5a20"),
    ("card_midnight.html", "The families joyfully invite you", "#6070b0"),
    ("card_rose.html",     "The families joyfully invite you", "#b06080"),
    ("card_forest.html",   "The families joyfully invite you", "#508050"),
]

for fname, invite_text, fill_color in templates:
    path = os.path.join(BASE, "templates", fname)

    if not os.path.exists(path):
        print(f"⚠️ SKIP: {fname}")
        continue

    with open(path, encoding="utf-8") as f:
        c = f.read()

    c = re.sub(
        r'<text[^>]*y="210"[^>]*>.*?priority_title.*?</text>\s*'
        r'<text[^>]*y="226"[^>]*>.*?priority_tagline.*?</text>',
        f'<text x="350" y="220" text-anchor="middle" '
        f'font-family="\'Cormorant Garamond\',Georgia,serif" '
        f'font-size="10" fill="{fill_color}">{invite_text}</text>',
        c,
        flags=re.DOTALL,
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(c)

    print(f"✅ Fixed: {fname}")


print("\n🎉 All done successfully!")