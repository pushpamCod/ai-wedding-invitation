import os, glob

BASE = r"C:\PROJECTS\AI wedding card\templates"

# All the different versions of that line across all card files
old_lines = [
    # peacock
    '<text x="350" y="220" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="10" fill="#8a6a20">The families joyfully invite you to celebrate</text>',
    # purple
    '<text x="350" y="220" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="10" fill="#9a7a30">The families joyfully invite you</text>',
    # sindoor
    '<text x="350" y="220" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="10" fill="#9a5a20">The families joyfully invite you</text>',
    # midnight
    '<text x="350" y="220" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="10" fill="#6070b0">The families joyfully invite you</text>',
    # rose
    '<text x="350" y="220" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="10" fill="#b06080">The families joyfully invite you</text>',
    # forest
    '<text x="350" y="220" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="10" fill="#508050">The families joyfully invite you</text>',
]

# What we replace each with (dynamic priority display)
# We keep the same y position, just change the text to use Jinja
new_text_template = '''<text x="350" y="210" text-anchor="middle" font-family="\'Montserrat\',sans-serif" font-size="8" fill="{accent}" letter-spacing="3">{{{{ details.priority_title | upper }}}}</text>
<text x="350" y="226" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="10" fill="{text_col}" font-style="italic">{{{{ details.priority_tagline }}}}</text>'''

# accent colors per card
card_accents = {
    "card_peacock.html":  ("#c9a96e", "#8a6a20"),
    "card_purple.html":   ("#d4a843", "#9a7a30"),
    "card_sindoor.html":  ("#e8500a", "#9a5a20"),
    "card_midnight.html": ("#6080c0", "#6070b0"),
    "card_rose.html":     ("#e080a0", "#b06080"),
    "card_forest.html":   ("#60a860", "#508050"),
}

for filename, (accent, text_col) in card_accents.items():
    path = os.path.join(BASE, filename)
    if not os.path.exists(path):
        print(f"SKIP (not found): {filename}")
        continue

    content = open(path, encoding="utf-8").read()
    original = content

    new_text = new_text_template.format(accent=accent, text_col=text_col)

    replaced = False
    for old in old_lines:
        if old in content:
            content = content.replace(old, new_text)
            replaced = True
            break

    if not replaced:
        # Try a broader search — find the line containing "invite you"
        import re
        pattern = r'<text[^>]*y="220"[^>]*>.*?invite you.*?</text>'
        match = re.search(pattern, content)
        if match:
            content = content.replace(match.group(0), new_text)
            replaced = True

    if replaced:
        open(path, "w", encoding="utf-8").write(content)
        print(f"Fixed: {filename}")
    else:
        print(f"NOT FOUND in {filename} — checking what's there...")
        # Print lines around y="220" to help debug
        for i, line in enumerate(content.split('\n')):
            if 'y="220"' in line or 'invite you' in line:
                print(f"  Line {i}: {line[:120]}")

print("\nDone! Now update app.py")