import os, glob

# Each card's theme colors for the details box
card_themes = {
    "card_peacock.html":  ("#d4a843", "#e8c97a", "#fdf6e3", "#8a6a20"),
    "card_purple.html":   ("#d4a843", "#ffd700", "#fff8f0", "#8a6a20"),
    "card_sindoor.html":  ("#e8500a", "#ffd700", "#fff8f0", "#8a4a10"),
    "card_midnight.html": ("#6080c0", "#a0c0f0", "#f0f4ff", "#4050a0"),
    "card_rose.html":     ("#e080a0", "#ffc0d0", "#fff5f8", "#9a5070"),
    "card_forest.html":   ("#60a860", "#c0e8c0", "#f5fff5", "#408040"),
}

BASE = r"C:\PROJECTS\AI wedding card\templates"

for filename, (border1, border2, bg, text_col) in card_themes.items():
    path = os.path.join(BASE, filename)
    content = open(path, encoding="utf-8").read()

    # Replace the details box rect fill color
    old = '<rect x="170" y="660" width="360" height="148" rx="6" fill="#fdf6e3"'
    new = f'<rect x="170" y="660" width="360" height="148" rx="6" fill="{bg}"'
    content = content.replace(old, new)

    # Replace the details box top band
    old2 = '<rect x="170" y="660" width="360" height="8" rx="3" fill="#d4a843"/>'
    new2 = f'<rect x="170" y="660" width="360" height="8" rx="3" fill="{border1}"/>'
    content = content.replace(old2, new2)

    # Replace border stroke
    old3 = 'stroke="#d4a843" stroke-width="1.2"/>'
    new3 = f'stroke="{border1}" stroke-width="1.2"/>'
    content = content.replace(old3, new3, 1)  # only first occurrence (details box)

    # Replace "WEDDING DETAILS" text color
    old4 = 'fill="#8a6a20" letter-spacing="3">WEDDING DETAILS</text>'
    new4 = f'fill="{text_col}" letter-spacing="3">WEDDING DETAILS</text>'
    content = content.replace(old4, new4)

    # Replace divider lines
    old5 = 'stroke="#c9a96e" stroke-width="0.5"/>\n{% '
    new5 = f'stroke="{border2}" stroke-width="0.5"/>\n{{%  '
    # simpler approach - just replace both divider lines
    content = content.replace(
        '<line x1="190" y1="690" x2="510" y2="690" stroke="#c9a96e" stroke-width="0.5"/>',
        f'<line x1="190" y1="690" x2="510" y2="690" stroke="{border2}" stroke-width="0.5"/>'
    )
    content = content.replace(
        '<line x1="190" y1="784" x2="510" y2="784" stroke="#c9a96e" stroke-width="0.5"/>',
        f'<line x1="190" y1="784" x2="510" y2="784" stroke="{border2}" stroke-width="0.5"/>'
    )

    # Replace style text color
    content = content.replace(
        'fill="#c9a96e" letter-spacing="2">~ {{ details.style',
        f'fill="{border2}" letter-spacing="2">~ {{{{ details.style'
    )

    open(path, "w", encoding="utf-8").write(content)
    print(f"Fixed: {filename}")

print("All done!")