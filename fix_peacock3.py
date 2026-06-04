path = r"C:\PROJECTS\AI wedding card\templates\card_peacock.html"

with open(path, encoding="utf-8") as f:
    content = f.read()

# Insert wedding details box BEFORE the bottom lotus band on page 1
old = '''<rect x="8" y="820" width="684" height="3" fill="#d4a843"/>
<rect x="8" y="823" width="684" height="49" fill="#1a5c3a"/>
<path d="M30 836 Q80 822 130 836 Q180 850 230 835 Q280 820 350 826 Q420 820 470 835 Q520 850 570 836 Q620 822 670 836" stroke="#2a8a50" stroke-width="1.4" fill="none"/>
{% for lx in [75,160,245,350,455,540,625] %}
<ellipse cx="{{ lx }}" cy="838" rx="6" ry="10" fill="#e8c97a"/>
<ellipse cx="{{ lx-6 }}" cy="843" rx="4.5" ry="7.5" fill="#d4a843"/>
<ellipse cx="{{ lx+6 }}" cy="843" rx="4.5" ry="7.5" fill="#d4a843"/>
<ellipse cx="{{ lx }}" cy="854" rx="8" ry="3.5" fill="#0f4a2a"/>
{% endfor %}
<text x="350" y="866" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="9" fill="#e8c97a" letter-spacing="3">~ Peacock Royal · Teal &amp; Gold ~</text>'''

new = '''<!-- WEDDING DETAILS BOX -->
<rect x="170" y="660" width="360" height="148" rx="6" fill="#fdf6e3" stroke="#d4a843" stroke-width="1.2"/>
<rect x="170" y="660" width="360" height="8" rx="3" fill="#d4a843"/>
<text x="350" y="682" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="9" fill="#8a6a20" letter-spacing="3">WEDDING DETAILS</text>
<line x1="190" y1="690" x2="510" y2="690" stroke="#c9a96e" stroke-width="0.5"/>
{% set fd = details.wedding_date.split(\'-\') %}
{% set months = [\'\',\'January\',\'February\',\'March\',\'April\',\'May\',\'June\',\'July\',\'August\',\'September\',\'October\',\'November\',\'December\'] %}
<text x="200" y="714" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="12" fill="#5a3a10">&#128197;</text>
{% if fd|length == 3 %}
<text x="220" y="714" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="12" fill="#3a2000">{{ months[fd[1]|int] }} {{ fd[2] }}, {{ fd[0] }}</text>
{% else %}
<text x="220" y="714" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="12" fill="#3a2000">{{ details.wedding_date }}</text>
{% endif %}
{% if details.ceremony_time %}
<text x="200" y="734" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="12" fill="#5a3a10">&#8987;</text>
<text x="220" y="734" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="12" fill="#5a3a10">{{ details.ceremony_time }}</text>
{% endif %}
<text x="200" y="756" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="12" fill="#5a3a10">&#127963;</text>
<text x="220" y="756" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="13" fill="#2a1800" font-weight="bold">{{ details.venue_name }}</text>
<text x="220" y="774" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="11" fill="#7a5a20">{{ details.venue_city }}</text>
<line x1="190" y1="784" x2="510" y2="784" stroke="#c9a96e" stroke-width="0.5"/>
<text x="350" y="800" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="9" fill="#c9a96e" letter-spacing="2">~ {{ details.style | upper }} STYLE ~</text>
<!-- BOTTOM LOTUS BAND -->
<rect x="8" y="812" width="684" height="3" fill="#d4a843"/>
<rect x="8" y="815" width="684" height="49" fill="#1a5c3a"/>
<path d="M30 828 Q80 815 130 828 Q180 841 230 827 Q280 813 350 819 Q420 813 470 827 Q520 841 570 828 Q620 815 670 828" stroke="#2a8a50" stroke-width="1.4" fill="none"/>
{% for lx in [75,160,245,350,455,540,625] %}
<ellipse cx="{{ lx }}" cy="830" rx="6" ry="10" fill="#e8c97a"/>
<ellipse cx="{{ lx-6 }}" cy="835" rx="4.5" ry="7.5" fill="#d4a843"/>
<ellipse cx="{{ lx+6 }}" cy="835" rx="4.5" ry="7.5" fill="#d4a843"/>
<ellipse cx="{{ lx }}" cy="846" rx="8" ry="3.5" fill="#0f4a2a"/>
{% endfor %}
<text x="350" y="858" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="9" fill="#e8c97a" letter-spacing="3">~ Peacock Royal · Teal &amp; Gold ~</text>'''

content = content.replace(old, new)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done! Wedding details box added to page 1.")