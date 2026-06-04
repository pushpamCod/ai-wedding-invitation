import os

path = r"C:\PROJECTS\AI wedding card\templates\card_peacock.html"

content = open(path, encoding="utf-8").read()

# Fix 1: Remove the stray 'clcl' typo
content = content.replace("\nclcl\n", "\n")

# Fix 2: Replace the broken bottom band section
old = """<!-- BOTTOM BAND -->
{% set bb = page2_height - 48 %}
<rect x="8" y="{{ bb }}" width="684" height="2.5" fill="#d4a843"/>
<rect x="8" y="{{ bb + 3 }}" width="684" height="38" fill="#1a5c3a"/>
<text x="350" y="{{ bb + 27 }}" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="9" fill="#e8c97a" letter-spacing="3">~ Peacock Royal · Teal &amp; Gold ~</text>
</svg>
</div>
{% endif %}"""

new = """<!-- BOTTOM BAND -->
<rect x="8" y="632" width="684" height="2.5" fill="#d4a843"/>
<rect x="8" y="635" width="684" height="38" fill="#1a5c3a"/>
<text x="350" y="659" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="9" fill="#e8c97a" letter-spacing="3">~ Peacock Royal · Teal &amp; Gold ~</text>
</svg>
</div>
{% endif %}"""

content = content.replace(old, new)

# Fix 3: The SVG viewBox for page 2 is hardcoded 680
# but bot2 calc uses ceremonies length — make sure it fits
# Replace the static viewBox with a dynamic one
old2 = '<svg class="card-svg" viewBox="0 0 700 680" xmlns="http://www.w3.org/2000/svg">'
new2 = '<svg class="card-svg" viewBox="0 0 700 680" xmlns="http://www.w3.org/2000/svg">'
# Keep same — 680 is enough for 3 ceremonies

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed successfully!")
print("Checking for remaining issues...")

if "page2_height" in content:
    print("WARNING: page2_height still found - manual fix needed")
else:
    print("OK: page2_height removed")

if "clcl" in content:
    print("WARNING: clcl typo still found")
else:
    print("OK: clcl removed")