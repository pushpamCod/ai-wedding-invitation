import os
BASE = r"C:\PROJECTS\AI wedding card\templates"

# ═══════════════════════════════════════════════════════
# SHARED PAGE 2 GENERATOR — same layout, different colors
# ═══════════════════════════════════════════════════════
def page2(bg1, bg2, band_color, border1, border2, text_gold, card_bg):
    return f'''
{{% if details.ceremonies %}}
<p class="page-label">Page 2 of 2 — Celebrations Schedule</p>
<div class="card-container">
{{% set months2 = ['','January','February','March','April','May','June','July','August','September','October','November','December'] %}}
{{% set num_cer = details.ceremonies | length %}}
{{% set p2h = 880 %}}
<svg class="card-svg" viewBox="0 0 700 {{{{ p2h }}}}" xmlns="http://www.w3.org/2000/svg">
<defs>
  <pattern id="bgp2" patternUnits="userSpaceOnUse" width="28" height="28">
    <rect width="28" height="28" fill="{bg1}"/>
    <circle cx="14" cy="14" r="1.1" fill="{bg2}" opacity="0.45"/>
    <circle cx="0" cy="0" r="0.7" fill="{bg2}" opacity="0.25"/>
    <circle cx="28" cy="28" r="0.7" fill="{bg2}" opacity="0.25"/>
  </pattern>
</defs>
<rect width="700" height="{{{{ p2h }}}}" fill="url(#bgp2)"/>
<rect x="8" y="8" width="684" height="{{{{ p2h-16 }}}}" rx="3" fill="none" stroke="{border1}" stroke-width="2.5"/>
<rect x="14" y="14" width="672" height="{{{{ p2h-28 }}}}" rx="2" fill="none" stroke="{border2}" stroke-width="0.8"/>
<circle cx="36"  cy="36"           r="9" fill="{border1}"/><circle cx="36"  cy="36"           r="6" fill="{bg1}"/><circle cx="36"  cy="36"           r="3" fill="{border2}"/>
<circle cx="664" cy="36"           r="9" fill="{border1}"/><circle cx="664" cy="36"           r="6" fill="{bg1}"/><circle cx="664" cy="36"           r="3" fill="{border2}"/>
<circle cx="36"  cy="{{{{ p2h-36 }}}}" r="9" fill="{border1}"/><circle cx="36"  cy="{{{{ p2h-36 }}}}" r="6" fill="{bg1}"/><circle cx="36"  cy="{{{{ p2h-36 }}}}" r="3" fill="{border2}"/>
<circle cx="664" cy="{{{{ p2h-36 }}}}" r="9" fill="{border1}"/><circle cx="664" cy="{{{{ p2h-36 }}}}" r="6" fill="{bg1}"/><circle cx="664" cy="{{{{ p2h-36 }}}}" r="3" fill="{border2}"/>
<rect x="8" y="8" width="684" height="56" fill="{band_color}"/>
<rect x="8" y="61" width="684" height="3" fill="{border1}"/>
{{% for lx in [75,160,245,350,455,540,625] %}}
<ellipse cx="{{{{ lx }}}}" cy="34" rx="7" ry="10" fill="{border2}"/>
<ellipse cx="{{{{ lx-7 }}}}" cy="39" rx="5" ry="8" fill="{border1}"/>
<ellipse cx="{{{{ lx+7 }}}}" cy="39" rx="5" ry="8" fill="{border1}"/>
<ellipse cx="{{{{ lx }}}}" cy="50" rx="9" ry="4" fill="{bg1}"/>
{{% endfor %}}
<text x="350" y="92" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="12" fill="{border1}" letter-spacing="4">CELEBRATIONS SCHEDULE</text>
<text x="350" y="120" text-anchor="middle" font-family="'Great Vibes',cursive,Georgia,serif" font-size="34" fill="{text_gold}">{{{{ details.bride_name }}}} &amp; {{{{ details.groom_name }}}}</text>
<line x1="100" y1="134" x2="600" y2="134" stroke="{border1}" stroke-width="0.8"/>
<polygon points="350,130 357,134 350,138 343,134" fill="{border1}"/>
<rect x="50" y="150" width="600" height="90" rx="8" fill="{card_bg}" stroke="{border1}" stroke-width="2"/>
<rect x="50" y="150" width="10" height="90" rx="4" fill="{border1}"/>
<circle cx="50" cy="150" r="6" fill="{border1}"/>
<circle cx="650" cy="150" r="6" fill="{border1}"/>
<circle cx="50" cy="240" r="6" fill="{border1}"/>
<circle cx="650" cy="240" r="6" fill="{border1}"/>
<text x="80" y="178" font-family="'Great Vibes',cursive,Georgia,serif" font-size="22" fill="#7a1030">💍 Wedding Ceremony</text>
{{% set fd2 = details.wedding_date.split('-') %}}
{{% if fd2|length == 3 %}}
<text x="80" y="202" font-family="'Cormorant Garamond',Georgia,serif" font-size="13" fill="#3a2000">📅 {{{{ months2[fd2[1]|int] }}}} {{{{ fd2[2] }}}}, {{{{ fd2[0] }}}}{{% if details.ceremony_time %}}   ⏳ {{{{ details.ceremony_time }}}}{{% endif %}}</text>
{{% endif %}}
<text x="80" y="224" font-family="'Cormorant Garamond',Georgia,serif" font-size="12" fill="#6a4010">🏛 {{{{ details.venue_name }}}}, {{{{ details.venue_city }}}}</text>
{{% set all_cers = details.ceremonies.items() | list %}}
{{% for key, cer in all_cers %}}
  {{% if loop.index0 % 2 == 0 %}}
    {{% set cx3 = 50 %}}{{% set cy3 = 260 + (loop.index0 // 2) * 150 %}}{{% set cw3 = 295 %}}
  {{% else %}}
    {{% set cx3 = 355 %}}{{% set cy3 = 320 + ((loop.index0 - 1) // 2) * 150 %}}{{% set cw3 = 295 %}}
  {{% endif %}}
  {{% if key == 'haldi' %}}{{% set accent = '#e8a020' %}}{{% set icon = '🌼' %}}
  {{% elif key == 'mehendi' %}}{{% set accent = '#2a8a40' %}}{{% set icon = '🌿' %}}
  {{% else %}}{{% set accent = '#9a2060' %}}{{% set icon = '🥂' %}}{{% endif %}}
<rect x="{{{{ cx3 }}}}" y="{{{{ cy3 }}}}" width="{{{{ cw3 }}}}" height="120" rx="10" fill="{card_bg}" stroke="{{{{ accent }}}}" stroke-width="1.5"/>
<rect x="{{{{ cx3 }}}}" y="{{{{ cy3 }}}}" width="8" height="120" rx="4" fill="{{{{ accent }}}}"/>
<circle cx="{{{{ cx3 }}}}" cy="{{{{ cy3 }}}}" r="5" fill="{{{{ accent }}}}"/>
<circle cx="{{{{ cx3 + cw3 }}}}" cy="{{{{ cy3 }}}}" r="5" fill="{{{{ accent }}}}"/>
<circle cx="{{{{ cx3 }}}}" cy="{{{{ cy3 + 120 }}}}" r="5" fill="{{{{ accent }}}}"/>
<circle cx="{{{{ cx3 + cw3 }}}}" cy="{{{{ cy3 + 120 }}}}" r="5" fill="{{{{ accent }}}}"/>
<text x="{{{{ cx3 + 22 }}}}" y="{{{{ cy3 + 28 }}}}" font-family="'Great Vibes',cursive,Georgia,serif" font-size="20" fill="{{{{ accent }}}}">{{{{ icon }}}} {{{{ cer.label if cer.label else key | capitalize }}}}</text>
{{% if cer.date %}}{{% set cfd = cer.date.split('-') %}}
  {{% if cfd|length == 3 %}}
<text x="{{{{ cx3 + 22 }}}}" y="{{{{ cy3 + 52 }}}}" font-family="'Cormorant Garamond',Georgia,serif" font-size="12" fill="#3a2000">📅 {{{{ months2[cfd[1]|int] }}}} {{{{ cfd[2] }}}}, {{{{ cfd[0] }}}}</text>
  {{% else %}}
<text x="{{{{ cx3 + 22 }}}}" y="{{{{ cy3 + 52 }}}}" font-family="'Cormorant Garamond',Georgia,serif" font-size="12" fill="#3a2000">📅 {{{{ cer.date }}}}</text>
  {{% endif %}}{{% endif %}}
{{% if cer.time %}}
<text x="{{{{ cx3 + 22 }}}}" y="{{{{ cy3 + 72 }}}}" font-family="'Cormorant Garamond',Georgia,serif" font-size="12" fill="#5a3a10">⏳ {{{{ cer.time }}}}</text>
{{% endif %}}
{{% if cer.venue %}}
<text x="{{{{ cx3 + 22 }}}}" y="{{{{ cy3 + 92 }}}}" font-family="'Cormorant Garamond',Georgia,serif" font-size="11" fill="#7a5a20">🏛 {{{{ cer.venue }}}}</text>
{{% endif %}}
{{% endfor %}}
{{% set pt_y = 260 + ((num_cer + 1) // 2) * 150 + 20 %}}
{{% if details.special_msg %}}
<rect x="50" y="{{{{ pt_y }}}}" width="600" height="80" rx="30" fill="{band_color}" stroke="{border1}" stroke-width="1.5"/>
<text x="350" y="{{{{ pt_y + 24 }}}}" text-anchor="middle" font-family="'Montserrat',sans-serif" font-size="8" fill="{border2}" letter-spacing="3">PERSONAL MESSAGE</text>
<text x="350" y="{{{{ pt_y + 48 }}}}" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="12" fill="{card_bg}" font-style="italic">{{{{ details.special_msg[:80] }}}}</text>
{{% else %}}
<rect x="150" y="{{{{ pt_y }}}}" width="400" height="50" rx="25" fill="{band_color}" stroke="{border1}" stroke-width="1"/>
<text x="350" y="{{{{ pt_y + 20 }}}}" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11" fill="{border2}" letter-spacing="1">Your presence is our greatest blessing</text>
<text x="350" y="{{{{ pt_y + 38 }}}}" text-anchor="middle" font-family="'Montserrat',sans-serif" font-size="8" fill="{border1}" letter-spacing="2">~ WE JOYFULLY AWAIT YOU ~</text>
{{% endif %}}
<rect x="8" y="{{{{ p2h - 48 }}}}" width="684" height="3" fill="{border1}"/>
<rect x="8" y="{{{{ p2h - 45 }}}}" width="684" height="40" fill="{band_color}"/>
{{% for lx in [75,160,245,350,455,540,625] %}}
<ellipse cx="{{{{ lx }}}}" cy="{{{{ p2h - 28 }}}}" rx="6" ry="9" fill="{border2}"/>
<ellipse cx="{{{{ lx-6 }}}}" cy="{{{{ p2h - 23 }}}}" rx="4.5" ry="7" fill="{border1}"/>
<ellipse cx="{{{{ lx+6 }}}}" cy="{{{{ p2h - 23 }}}}" rx="4.5" ry="7" fill="{border1}"/>
{{% endfor %}}
</svg>
</div>
{{% endif %}}'''


# ═══════════════════════════════════════════════════════
# SHARED HTML WRAPPER
# ═══════════════════════════════════════════════════════
def html_wrapper(card_name, body_bg, btn_color, btn_text):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{{{ details.bride_name }}}} &amp; {{{{ details.groom_name }}}} — Wedding Invitation</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400;1,600&family=Great+Vibes&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        * {{ margin:0; padding:0; box-sizing:border-box; }}
        body {{ background:{body_bg}; min-height:100vh; display:flex; flex-direction:column; align-items:center; padding:30px 20px 60px; font-family:'Cormorant Garamond',Georgia,serif; }}
        .action-bar {{ display:flex; gap:14px; margin-bottom:20px; flex-wrap:wrap; justify-content:center; }}
        .btn-primary {{ padding:13px 32px; background:{btn_color}; color:{btn_text}; border:none; border-radius:8px; font-family:'Montserrat',sans-serif; font-size:0.9rem; font-weight:600; cursor:pointer; text-decoration:none; display:inline-block; transition:transform 0.2s,box-shadow 0.2s; }}
        .btn-primary:hover {{ transform:translateY(-2px); box-shadow:0 6px 20px rgba(0,0,0,0.3); }}
        .btn-secondary {{ padding:13px 32px; background:transparent; color:{btn_color}; border:2px solid {btn_color}; border-radius:8px; font-family:'Montserrat',sans-serif; font-size:0.9rem; font-weight:500; text-decoration:none; transition:all 0.2s; display:inline-block; }}
        .btn-secondary:hover {{ background:{btn_color}; color:{btn_text}; }}
        .share-row {{ display:flex; flex-direction:column; align-items:center; gap:10px; margin-bottom:28px; width:100%; max-width:720px; }}
        .share-label {{ font-family:'Montserrat',sans-serif; font-size:0.7rem; letter-spacing:3px; text-transform:uppercase; color:{btn_color}; opacity:0.75; }}
        .share-btns {{ display:flex; gap:12px; flex-wrap:wrap; justify-content:center; }}
        .share-btn {{ display:flex; align-items:center; gap:8px; padding:10px 22px; border-radius:8px; font-family:'Montserrat',sans-serif; font-size:0.85rem; font-weight:500; text-decoration:none; transition:transform 0.2s; }}
        .share-btn:hover {{ transform:translateY(-2px); }}
        .wa {{ background:#25D366; color:white; }} .em {{ background:#4a90d9; color:white; }}
        .share-link-row {{ display:flex; gap:8px; width:100%; max-width:500px; }}
        .share-link-row input {{ flex:1; padding:9px 14px; background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.2); border-radius:8px; color:{btn_color}; font-size:0.82rem; outline:none; font-family:'Montserrat',sans-serif; }}
        .copy-btn {{ padding:9px 16px; background:{btn_color}; color:{btn_text}; border:none; border-radius:8px; cursor:pointer; font-family:'Montserrat',sans-serif; font-size:0.82rem; font-weight:600; white-space:nowrap; }}
        .page-label {{ font-family:'Montserrat',sans-serif; font-size:0.7rem; letter-spacing:3px; text-transform:uppercase; color:{btn_color}; opacity:0.6; margin:20px 0 8px; }}
        .card-container {{ width:100%; max-width:720px; position:relative; }}
        .card-svg {{ width:100%; height:auto; display:block; border-radius:4px; box-shadow:0 8px 60px rgba(0,0,0,0.6); }}
        @media print {{
            body {{ background:white; padding:0; }}
            .action-bar,.share-row,.page-label {{ display:none !important; }}
            .card-container {{ max-width:100%; page-break-after:always; }}
            .card-container:last-child {{ page-break-after:auto; }}
            .card-svg {{ box-shadow:none; width:100%; }}
            @page {{ size:A4 portrait; margin:5mm; }}
        }}
    </style>
</head>
<body>
<div class="action-bar">
    <a href="/" class="btn-secondary">&#8592; Generate Another</a>
    <button onclick="window.print()" class="btn-primary">&#128438; Download PDF</button>
</div>
<div class="share-row">
    <p class="share-label">Share your invitation</p>
    <div class="share-btns">
        <a href="{{{{ whatsapp_url }}}}" target="_blank" class="share-btn wa">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
            WhatsApp
        </a>
        <a href="{{{{ email_url }}}}" class="share-btn em">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,12 2,6"/></svg>
            Email
        </a>
    </div>
    {{% if share_link %}}
    <div class="share-link-row">
        <input type="text" value="{{{{ share_link }}}}" id="slink" readonly>
        <button class="copy-btn" id="copybtn" onclick="copyLink()">&#128203; Copy</button>
    </div>
    {{% endif %}}
</div>
<p class="page-label">Page 1 of {{% if details.ceremonies %}}2{{% else %}}1{{% endif %}} — Main Invitation</p>'''


# ═══════════════════════════════════════════════════════
# SHARED DETAILS BOX + FOOTER SCRIPT
# ═══════════════════════════════════════════════════════
def details_box_and_footer(border1, border2, band_color, style_label):
    return f'''
<!-- WEDDING DETAILS BOX -->
<rect x="170" y="660" width="360" height="148" rx="6" fill="#fdf6e3" stroke="{border1}" stroke-width="1.2"/>
<rect x="170" y="660" width="360" height="8" rx="3" fill="{border1}"/>
<text x="350" y="682" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="9" fill="#8a6a20" letter-spacing="3">WEDDING DETAILS</text>
<line x1="190" y1="690" x2="510" y2="690" stroke="{border2}" stroke-width="0.5"/>
{{%  set fd = details.wedding_date.split('-') %}}
{{%  set months = ['','January','February','March','April','May','June','July','August','September','October','November','December'] %}}
<text x="200" y="714" font-family="'Cormorant Garamond',Georgia,serif" font-size="12" fill="#5a3a10">📅</text>
{{%  if fd|length == 3 %}}
<text x="222" y="714" font-family="'Cormorant Garamond',Georgia,serif" font-size="12" fill="#3a2000">{{{{ months[fd[1]|int] }}}} {{{{ fd[2] }}}}, {{{{ fd[0] }}}}</text>
{{%  else %}}
<text x="222" y="714" font-family="'Cormorant Garamond',Georgia,serif" font-size="12" fill="#3a2000">{{{{ details.wedding_date }}}}</text>
{{%  endif %}}
{{%  if details.ceremony_time %}}
<text x="200" y="734" font-family="'Cormorant Garamond',Georgia,serif" font-size="12" fill="#5a3a10">⏳ {{{{ details.ceremony_time }}}}</text>
{{%  endif %}}
<text x="200" y="756" font-family="'Cormorant Garamond',Georgia,serif" font-size="13" fill="#2a1800" font-weight="bold">🏛 {{{{ details.venue_name }}}}</text>
<text x="200" y="774" font-family="'Cormorant Garamond',Georgia,serif" font-size="11" fill="#7a5a20">   {{{{ details.venue_city }}}}</text>
<line x1="190" y1="784" x2="510" y2="784" stroke="{border2}" stroke-width="0.5"/>
<text x="350" y="800" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="9" fill="{border2}" letter-spacing="2">~ {{{{ details.style | upper }}}} STYLE ~</text>'''


SCRIPT = '''
<script>
function copyLink() {
    const el = document.getElementById('slink');
    el.select(); document.execCommand('copy');
    const btn = document.getElementById('copybtn');
    btn.textContent = 'Copied!';
    setTimeout(() => btn.textContent = '📋 Copy', 2000);
}
</script>
</body>
</html>'''


# ═══════════════════════════════════════════════════════════════════════
# CARD 2: PURPLE MAHARAJA
# Deep purple + marigold gold + Mughal arch + elephants
# ═══════════════════════════════════════════════════════════════════════
purple_card = html_wrapper("Purple Maharaja", "#1a0035", "#d4a843", "#1a0035") + '''
<div class="card-container">
<svg class="card-svg" viewBox="0 0 700 880" xmlns="http://www.w3.org/2000/svg">
<defs>
  <pattern id="bgp" patternUnits="userSpaceOnUse" width="30" height="30">
    <rect width="30" height="30" fill="#1a0035"/>
    <circle cx="15" cy="15" r="1" fill="#4a0080" opacity="0.5"/>
    <circle cx="0" cy="0" r="0.6" fill="#4a0080" opacity="0.3"/>
    <circle cx="30" cy="30" r="0.6" fill="#4a0080" opacity="0.3"/>
  </pattern>
  <pattern id="creamp" patternUnits="userSpaceOnUse" width="18" height="18">
    <rect width="18" height="18" fill="#fff8f0"/>
    <circle cx="9" cy="9" r="0.4" fill="#d4a843" opacity="0.2"/>
  </pattern>
</defs>
<rect width="700" height="880" fill="url(#bgp)"/>
<!-- TRIPLE BORDER -->
<rect x="8"  y="8"  width="684" height="864" rx="3" fill="none" stroke="#d4a843" stroke-width="2.5"/>
<rect x="14" y="14" width="672" height="852" rx="2" fill="none" stroke="#ffd700" stroke-width="0.8"/>
<rect x="18" y="18" width="664" height="844" rx="2" fill="none" stroke="#d4a843" stroke-width="0.5"/>
<!-- CORNER ORNAMENTS -->
<path d="M8 8 L62 8 L62 13 L18 13 L18 62 L8 62 Z" fill="#d4a843"/>
<circle cx="36" cy="36" r="10" fill="#d4a843"/><circle cx="36" cy="36" r="7" fill="#1a0035"/><circle cx="36" cy="36" r="3.5" fill="#ffd700"/>
<ellipse cx="36" cy="22" rx="3.5" ry="7" fill="#d4a843" opacity="0.8"/>
<ellipse cx="36" cy="50" rx="3.5" ry="7" fill="#d4a843" opacity="0.8"/>
<ellipse cx="22" cy="36" rx="7" ry="3.5" fill="#d4a843" opacity="0.8"/>
<ellipse cx="50" cy="36" rx="7" ry="3.5" fill="#d4a843" opacity="0.8"/>
<path d="M692 8 L638 8 L638 13 L682 13 L682 62 L692 62 Z" fill="#d4a843"/>
<circle cx="664" cy="36" r="10" fill="#d4a843"/><circle cx="664" cy="36" r="7" fill="#1a0035"/><circle cx="664" cy="36" r="3.5" fill="#ffd700"/>
<ellipse cx="664" cy="22" rx="3.5" ry="7" fill="#d4a843" opacity="0.8"/>
<ellipse cx="664" cy="50" rx="3.5" ry="7" fill="#d4a843" opacity="0.8"/>
<ellipse cx="650" cy="36" rx="7" ry="3.5" fill="#d4a843" opacity="0.8"/>
<ellipse cx="678" cy="36" rx="7" ry="3.5" fill="#d4a843" opacity="0.8"/>
<path d="M8 872 L62 872 L62 867 L18 867 L18 818 L8 818 Z" fill="#d4a843"/>
<circle cx="36" cy="844" r="10" fill="#d4a843"/><circle cx="36" cy="844" r="7" fill="#1a0035"/><circle cx="36" cy="844" r="3.5" fill="#ffd700"/>
<ellipse cx="36" cy="830" rx="3.5" ry="7" fill="#d4a843" opacity="0.8"/>
<ellipse cx="36" cy="858" rx="3.5" ry="7" fill="#d4a843" opacity="0.8"/>
<ellipse cx="22" cy="844" rx="7" ry="3.5" fill="#d4a843" opacity="0.8"/>
<ellipse cx="50" cy="844" rx="7" ry="3.5" fill="#d4a843" opacity="0.8"/>
<path d="M692 872 L638 872 L638 867 L682 867 L682 818 L692 818 Z" fill="#d4a843"/>
<circle cx="664" cy="844" r="10" fill="#d4a843"/><circle cx="664" cy="844" r="7" fill="#1a0035"/><circle cx="664" cy="844" r="3.5" fill="#ffd700"/>
<ellipse cx="664" cy="830" rx="3.5" ry="7" fill="#d4a843" opacity="0.8"/>
<ellipse cx="664" cy="858" rx="3.5" ry="7" fill="#d4a843" opacity="0.8"/>
<ellipse cx="650" cy="844" rx="7" ry="3.5" fill="#d4a843" opacity="0.8"/>
<ellipse cx="678" cy="844" rx="7" ry="3.5" fill="#d4a843" opacity="0.8"/>
<!-- TOP MARIGOLD BAND -->
<rect x="8" y="8" width="684" height="56" fill="#4a0080"/>
<rect x="8" y="61" width="684" height="3" fill="#d4a843"/>
<!-- marigold garland -->
<path d="M30 48 Q80 35 130 48 Q180 61 230 46 Q280 31 350 37 Q420 31 470 46 Q520 61 570 48 Q620 35 670 48" stroke="#ff8c00" stroke-width="2" fill="none"/>
{% for lx in [75,160,245,350,455,540,625] %}
<circle cx="{{ lx }}" cy="34" r="8" fill="#ff8c00"/>
<circle cx="{{ lx }}" cy="34" r="5" fill="#ffd700"/>
<circle cx="{{ lx }}" cy="34" r="2.5" fill="#ff6600"/>
<line x1="{{ lx }}" y1="42" x2="{{ lx }}" y2="54" stroke="#ff8c00" stroke-width="2"/>
<circle cx="{{ lx }}" cy="57" r="4" fill="#ffd700"/>
{% endfor %}
<!-- GANESH with purple theme -->
<circle cx="350" cy="90" r="32" fill="#d4a843"/>
<circle cx="350" cy="90" r="28" fill="#4a0080"/>
<circle cx="350" cy="90" r="23" fill="#d4a843"/>
<circle cx="350" cy="90" r="18" fill="#1a0035"/>
<text x="350" y="98" text-anchor="middle" font-size="22" fill="#d4a843" font-family="serif">ॐ</text>
<ellipse cx="350" cy="56"  rx="4.5" ry="9"  fill="#d4a843" opacity="0.8"/>
<ellipse cx="350" cy="124" rx="4.5" ry="9"  fill="#d4a843" opacity="0.8"/>
<ellipse cx="316" cy="90"  rx="9"   ry="4.5" fill="#d4a843" opacity="0.8"/>
<ellipse cx="384" cy="90"  rx="9"   ry="4.5" fill="#d4a843" opacity="0.8"/>
<line x1="100" y1="90" x2="316" y2="90" stroke="#d4a843" stroke-width="0.8"/>
<line x1="384" y1="90" x2="600" y2="90" stroke="#d4a843" stroke-width="0.8"/>
<polygon points="150,90 158,85 166,90 158,95" fill="#d4a843"/>
<polygon points="220,90 228,85 236,90 228,95" fill="#d4a843"/>
<polygon points="464,90 472,85 480,90 472,95" fill="#d4a843"/>
<polygon points="534,90 542,85 550,90 542,95" fill="#d4a843"/>
<!-- CREAM ARCH PANEL -->
<path d="M 162 830 L 162 234 Q 162 148 350 142 Q 538 148 538 234 L 538 830 Z" fill="url(#creamp)" stroke="#d4a843" stroke-width="1.5"/>
<path d="M 170 830 L 170 238 Q 170 160 350 155 Q 530 160 530 238 L 530 830 Z" fill="none" stroke="#ffd700" stroke-width="0.5"/>
<path d="M 182 238 Q 208 195 250 174 Q 296 155 350 153 Q 404 155 450 174 Q 492 195 518 238" fill="#d4a843" opacity="0.2" stroke="#d4a843" stroke-width="1"/>
<path d="M 186 232 Q 214 196 240 181 Q 253 173 266 181 Q 278 191 286 207 Q 298 186 315 173 Q 333 162 350 164 Q 367 162 385 173 Q 402 186 414 207 Q 422 191 434 181 Q 447 173 460 181 Q 472 191 490 208 Q 505 222 514 232" fill="none" stroke="#d4a843" stroke-width="1.2"/>
<!-- PILLARS purple tinted -->
<rect x="154" y="296" width="18" height="534" fill="#e8d5a0" stroke="#c9a96e" stroke-width="1"/>
<rect x="144" y="283" width="38" height="16" rx="2" fill="#d4a843"/>
<rect x="141" y="270" width="44" height="14" rx="2" fill="#ffd700"/>
<rect x="144" y="828" width="38" height="14" rx="2" fill="#d4a843"/>
<rect x="141" y="842" width="44" height="12" rx="2" fill="#ffd700"/>
<rect x="528" y="296" width="18" height="534" fill="#e8d5a0" stroke="#c9a96e" stroke-width="1"/>
<rect x="518" y="283" width="38" height="16" rx="2" fill="#d4a843"/>
<rect x="515" y="270" width="44" height="14" rx="2" fill="#ffd700"/>
<rect x="518" y="828" width="38" height="14" rx="2" fill="#d4a843"/>
<rect x="515" y="842" width="44" height="12" rx="2" fill="#ffd700"/>
<!-- LEFT ELEPHANT -->
<ellipse cx="90" cy="520" rx="55" ry="50" fill="#4a3070"/>
<ellipse cx="90" cy="505" rx="45" ry="40" fill="#5a4080"/>
<!-- head -->
<circle cx="90" cy="455" r="38" fill="#4a3070"/>
<circle cx="90" cy="448" r="30" fill="#5a4080"/>
<!-- ears -->
<ellipse cx="52" cy="458" rx="22" ry="28" fill="#3a2060"/>
<ellipse cx="128" cy="458" rx="22" ry="28" fill="#3a2060"/>
<!-- eye -->
<circle cx="74" cy="448" r="5" fill="#1a0035"/><circle cx="76" cy="446" r="2" fill="#ffd700"/>
<circle cx="106" cy="448" r="5" fill="#1a0035"/><circle cx="108" cy="446" r="2" fill="#ffd700"/>
<!-- trunk -->
<path d="M90 475 Q75 510 65 540 Q58 560 70 565 Q80 570 85 550 Q90 530 95 510" stroke="#4a3070" stroke-width="14" fill="none" stroke-linecap="round"/>
<path d="M90 475 Q75 510 65 540 Q58 560 70 565 Q80 570 85 550 Q90 530 95 510" stroke="#5a4080" stroke-width="8" fill="none" stroke-linecap="round"/>
<!-- tusk -->
<path d="M78 472 Q60 490 55 510" stroke="#ffd700" stroke-width="4" fill="none" stroke-linecap="round"/>
<!-- gold decoration on elephant -->
<ellipse cx="90" cy="435" rx="18" ry="8" fill="#d4a843" opacity="0.8"/>
<circle cx="90" cy="427" r="6" fill="#ffd700"/>
<ellipse cx="55" cy="458" rx="8" ry="12" fill="#d4a843" opacity="0.6"/>
<ellipse cx="125" cy="458" rx="8" ry="12" fill="#d4a843" opacity="0.6"/>
<!-- legs -->
<rect x="60" y="558" width="18" height="35" rx="4" fill="#4a3070"/>
<rect x="82" y="558" width="18" height="35" rx="4" fill="#4a3070"/>
<rect x="104" y="558" width="18" height="35" rx="4" fill="#3a2060"/>
<!-- RIGHT ELEPHANT (mirror) -->
<ellipse cx="610" cy="520" rx="55" ry="50" fill="#4a3070"/>
<ellipse cx="610" cy="505" rx="45" ry="40" fill="#5a4080"/>
<circle cx="610" cy="455" r="38" fill="#4a3070"/>
<circle cx="610" cy="448" r="30" fill="#5a4080"/>
<ellipse cx="572" cy="458" rx="22" ry="28" fill="#3a2060"/>
<ellipse cx="648" cy="458" rx="22" ry="28" fill="#3a2060"/>
<circle cx="594" cy="448" r="5" fill="#1a0035"/><circle cx="596" cy="446" r="2" fill="#ffd700"/>
<circle cx="626" cy="448" r="5" fill="#1a0035"/><circle cx="628" cy="446" r="2" fill="#ffd700"/>
<path d="M610 475 Q625 510 635 540 Q642 560 630 565 Q620 570 615 550 Q610 530 605 510" stroke="#4a3070" stroke-width="14" fill="none" stroke-linecap="round"/>
<path d="M610 475 Q625 510 635 540 Q642 560 630 565 Q620 570 615 550 Q610 530 605 510" stroke="#5a4080" stroke-width="8" fill="none" stroke-linecap="round"/>
<path d="M622 472 Q640 490 645 510" stroke="#ffd700" stroke-width="4" fill="none" stroke-linecap="round"/>
<ellipse cx="610" cy="435" rx="18" ry="8" fill="#d4a843" opacity="0.8"/>
<circle cx="610" cy="427" r="6" fill="#ffd700"/>
<ellipse cx="575" cy="458" rx="8" ry="12" fill="#d4a843" opacity="0.6"/>
<ellipse cx="645" cy="458" rx="8" ry="12" fill="#d4a843" opacity="0.6"/>
<rect x="578" y="558" width="18" height="35" rx="4" fill="#3a2060"/>
<rect x="600" y="558" width="18" height="35" rx="4" fill="#4a3070"/>
<rect x="622" y="558" width="18" height="35" rx="4" fill="#4a3070"/>
<!-- TEXT CONTENT -->
<text x="350" y="198" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11" fill="#8a6a20" letter-spacing="3">|| Shri Ganeshaya Namah ||</text>
<text x="350" y="220" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="10" fill="#9a7a30">The families joyfully invite you</text>
<line x1="215" y1="230" x2="485" y2="230" stroke="#d4a843" stroke-width="0.8"/>
<polygon points="350,226 356,230 350,234 344,230" fill="#d4a843"/>
<text x="350" y="268" text-anchor="middle" font-family="'Great Vibes',cursive,Georgia,serif" font-size="40" fill="#6a0060">{{ details.bride_name }}</text>
<line x1="215" y1="278" x2="485" y2="278" stroke="#d4a843" stroke-width="0.5"/>
<text x="350" y="308" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="16" fill="#d4a843" letter-spacing="5">~ weds ~</text>
<text x="350" y="348" text-anchor="middle" font-family="'Great Vibes',cursive,Georgia,serif" font-size="40" fill="#3a0060">{{ details.groom_name }}</text>
<line x1="215" y1="358" x2="485" y2="358" stroke="#d4a843" stroke-width="0.5"/>
<polygon points="350,354 356,358 350,362 344,358" fill="#d4a843"/>
{% set fd = details.wedding_date.split('-') %}
{% set months = ['','January','February','March','April','May','June','July','August','September','October','November','December'] %}
{% if fd|length == 3 %}
<text x="350" y="386" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="14" fill="#3a2000" font-weight="bold">{{ months[fd[1]|int] }} {{ fd[2] }}, {{ fd[0] }}</text>
{% else %}
<text x="350" y="386" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="14" fill="#3a2000">{{ details.wedding_date }}</text>
{% endif %}
{% if details.ceremony_time %}
<text x="350" y="406" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="13" fill="#5a3a10">{{ details.ceremony_time }}</text>
{% endif %}
<line x1="215" y1="420" x2="485" y2="420" stroke="#d4a843" stroke-width="0.5"/>
<text x="350" y="440" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="9" fill="#8a6a20" letter-spacing="3">VENUE</text>
<text x="350" y="462" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="16" fill="#2a1800" font-weight="bold">{{ details.venue_name }}</text>
<text x="350" y="480" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="12" fill="#5a3a10">{{ details.venue_city }}</text>
<line x1="215" y1="493" x2="485" y2="493" stroke="#d4a843" stroke-width="0.5"/>
<polygon points="350,489 356,493 350,497 344,493" fill="#d4a843"/>
{% set words = invitation_text.split() %}
{% set l1 = words[:8]   | join(' ') %}{% set l2 = words[8:16]  | join(' ') %}
{% set l3 = words[16:24] | join(' ') %}{% set l4 = words[24:32] | join(' ') %}
{% set l5 = words[32:40] | join(' ') %}
<text x="350" y="516" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#4a3010" font-style="italic">{{ l1 }}</text>
{% if l2 %}<text x="350" y="533" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#4a3010" font-style="italic">{{ l2 }}</text>{% endif %}
{% if l3 %}<text x="350" y="550" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#4a3010" font-style="italic">{{ l3 }}</text>{% endif %}
{% if l4 %}<text x="350" y="567" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#4a3010" font-style="italic">{{ l4 }}</text>{% endif %}
{% if l5 %}<text x="350" y="584" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#4a3010" font-style="italic">{{ l5 }}</text>{% endif %}
<line x1="215" y1="600" x2="485" y2="600" stroke="#d4a843" stroke-width="0.5"/>
<ellipse cx="350" cy="618" rx="95" ry="13" fill="#4a0080" opacity="0.9"/>
<text x="350" y="623" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11" fill="#ffd700" letter-spacing="1">We joyfully await your presence</text>
{% if details.ceremonies %}
<text x="350" y="648" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="10" fill="#8a6a20" font-style="italic">* Celebrations schedule on next page</text>
{% endif %}
''' + details_box_and_footer("#d4a843","#ffd700","#4a0080","purple") + '''
<!-- BOTTOM MARIGOLD BAND -->
<rect x="8" y="812" width="684" height="3" fill="#d4a843"/>
<rect x="8" y="815" width="684" height="49" fill="#4a0080"/>
<path d="M30 828 Q80 815 130 828 Q180 841 230 827 Q280 813 350 819 Q420 813 470 827 Q520 841 570 828 Q620 815 670 828" stroke="#ff8c00" stroke-width="1.5" fill="none"/>
{% for lx in [75,160,245,350,455,540,625] %}
<circle cx="{{ lx }}" cy="830" r="6" fill="#ff8c00"/>
<circle cx="{{ lx }}" cy="830" r="3.5" fill="#ffd700"/>
<line x1="{{ lx }}" y1="836" x2="{{ lx }}" y2="846" stroke="#ff8c00" stroke-width="1.5"/>
<circle cx="{{ lx }}" cy="849" r="3" fill="#ffd700"/>
{% endfor %}
<text x="350" y="858" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="9" fill="#ffd700" letter-spacing="3">~ Purple Maharaja · Royal Indian ~</text>
</svg>
</div>
''' + page2("#1a0035","#4a0080","#4a0080","#d4a843","#ffd700","#ffd700","#fff8f0") + SCRIPT


# ═══════════════════════════════════════════════════════════════════════
# CARD 3: SINDOOR RED
# Deep red + saffron + lotus motifs
# ═══════════════════════════════════════════════════════════════════════
sindoor_card = html_wrapper("Sindoor Red", "#1a0000", "#e8500a", "#fff8f0") + '''
<div class="card-container">
<svg class="card-svg" viewBox="0 0 700 880" xmlns="http://www.w3.org/2000/svg">
<defs>
  <pattern id="bgp" patternUnits="userSpaceOnUse" width="30" height="30">
    <rect width="30" height="30" fill="#1a0000"/>
    <circle cx="15" cy="15" r="1" fill="#5a0808" opacity="0.5"/>
    <circle cx="0" cy="0" r="0.6" fill="#5a0808" opacity="0.3"/>
    <circle cx="30" cy="30" r="0.6" fill="#5a0808" opacity="0.3"/>
  </pattern>
  <pattern id="creamp" patternUnits="userSpaceOnUse" width="18" height="18">
    <rect width="18" height="18" fill="#fff8f0"/>
    <circle cx="9" cy="9" r="0.4" fill="#e8500a" opacity="0.15"/>
  </pattern>
</defs>
<rect width="700" height="880" fill="url(#bgp)"/>
<rect x="8"  y="8"  width="684" height="864" rx="3" fill="none" stroke="#e8500a" stroke-width="2.5"/>
<rect x="14" y="14" width="672" height="852" rx="2" fill="none" stroke="#ffd700" stroke-width="0.8"/>
<rect x="18" y="18" width="664" height="844" rx="2" fill="none" stroke="#e8500a" stroke-width="0.5"/>
<!-- CORNER ORNAMENTS -->
<path d="M8 8 L62 8 L62 13 L18 13 L18 62 L8 62 Z" fill="#e8500a"/>
<circle cx="36" cy="36" r="10" fill="#e8500a"/><circle cx="36" cy="36" r="7" fill="#1a0000"/><circle cx="36" cy="36" r="3.5" fill="#ffd700"/>
<ellipse cx="36" cy="22" rx="3.5" ry="7" fill="#e8500a" opacity="0.8"/>
<ellipse cx="36" cy="50" rx="3.5" ry="7" fill="#e8500a" opacity="0.8"/>
<ellipse cx="22" cy="36" rx="7" ry="3.5" fill="#e8500a" opacity="0.8"/>
<ellipse cx="50" cy="36" rx="7" ry="3.5" fill="#e8500a" opacity="0.8"/>
<path d="M692 8 L638 8 L638 13 L682 13 L682 62 L692 62 Z" fill="#e8500a"/>
<circle cx="664" cy="36" r="10" fill="#e8500a"/><circle cx="664" cy="36" r="7" fill="#1a0000"/><circle cx="664" cy="36" r="3.5" fill="#ffd700"/>
<ellipse cx="664" cy="22" rx="3.5" ry="7" fill="#e8500a" opacity="0.8"/>
<ellipse cx="664" cy="50" rx="3.5" ry="7" fill="#e8500a" opacity="0.8"/>
<ellipse cx="650" cy="36" rx="7" ry="3.5" fill="#e8500a" opacity="0.8"/>
<ellipse cx="678" cy="36" rx="7" ry="3.5" fill="#e8500a" opacity="0.8"/>
<path d="M8 872 L62 872 L62 867 L18 867 L18 818 L8 818 Z" fill="#e8500a"/>
<circle cx="36" cy="844" r="10" fill="#e8500a"/><circle cx="36" cy="844" r="7" fill="#1a0000"/><circle cx="36" cy="844" r="3.5" fill="#ffd700"/>
<ellipse cx="36" cy="830" rx="3.5" ry="7" fill="#e8500a" opacity="0.8"/>
<ellipse cx="36" cy="858" rx="3.5" ry="7" fill="#e8500a" opacity="0.8"/>
<ellipse cx="22" cy="844" rx="7" ry="3.5" fill="#e8500a" opacity="0.8"/>
<ellipse cx="50" cy="844" rx="7" ry="3.5" fill="#e8500a" opacity="0.8"/>
<path d="M692 872 L638 872 L638 867 L682 867 L682 818 L692 818 Z" fill="#e8500a"/>
<circle cx="664" cy="844" r="10" fill="#e8500a"/><circle cx="664" cy="844" r="7" fill="#1a0000"/><circle cx="664" cy="844" r="3.5" fill="#ffd700"/>
<ellipse cx="664" cy="830" rx="3.5" ry="7" fill="#e8500a" opacity="0.8"/>
<ellipse cx="664" cy="858" rx="3.5" ry="7" fill="#e8500a" opacity="0.8"/>
<ellipse cx="650" cy="844" rx="7" ry="3.5" fill="#e8500a" opacity="0.8"/>
<ellipse cx="678" cy="844" rx="7" ry="3.5" fill="#e8500a" opacity="0.8"/>
<!-- TOP BAND with lotuses -->
<rect x="8" y="8" width="684" height="56" fill="#8a0000"/>
<rect x="8" y="61" width="684" height="3" fill="#e8500a"/>
<path d="M30 48 Q80 35 130 48 Q180 61 230 46 Q280 31 350 37 Q420 31 470 46 Q520 61 570 48 Q620 35 670 48" stroke="#e8500a" stroke-width="1.5" fill="none"/>
{% for lx in [75,160,245,350,455,540,625] %}
<ellipse cx="{{ lx }}" cy="34" rx="7" ry="10" fill="#ffd0a0"/>
<ellipse cx="{{ lx-7 }}" cy="39" rx="5" ry="8" fill="#e8500a"/>
<ellipse cx="{{ lx+7 }}" cy="39" rx="5" ry="8" fill="#e8500a"/>
<ellipse cx="{{ lx }}" cy="50" rx="9" ry="4" fill="#5a0000"/>
{% endfor %}
<!-- GANESH sindoor theme -->
<circle cx="350" cy="90" r="32" fill="#e8500a"/>
<circle cx="350" cy="90" r="28" fill="#8a0000"/>
<circle cx="350" cy="90" r="23" fill="#e8500a"/>
<circle cx="350" cy="90" r="18" fill="#1a0000"/>
<text x="350" y="98" text-anchor="middle" font-size="22" fill="#ffd700" font-family="serif">ॐ</text>
<ellipse cx="350" cy="56"  rx="4.5" ry="9"  fill="#e8500a" opacity="0.8"/>
<ellipse cx="350" cy="124" rx="4.5" ry="9"  fill="#e8500a" opacity="0.8"/>
<ellipse cx="316" cy="90"  rx="9"   ry="4.5" fill="#e8500a" opacity="0.8"/>
<ellipse cx="384" cy="90"  rx="9"   ry="4.5" fill="#e8500a" opacity="0.8"/>
<line x1="100" y1="90" x2="316" y2="90" stroke="#e8500a" stroke-width="0.8"/>
<line x1="384" y1="90" x2="600" y2="90" stroke="#e8500a" stroke-width="0.8"/>
<polygon points="150,90 158,85 166,90 158,95" fill="#e8500a"/>
<polygon points="220,90 228,85 236,90 228,95" fill="#e8500a"/>
<polygon points="464,90 472,85 480,90 472,95" fill="#e8500a"/>
<polygon points="534,90 542,85 550,90 542,95" fill="#e8500a"/>
<!-- CREAM ARCH -->
<path d="M 162 830 L 162 234 Q 162 148 350 142 Q 538 148 538 234 L 538 830 Z" fill="url(#creamp)" stroke="#e8500a" stroke-width="1.5"/>
<path d="M 170 830 L 170 238 Q 170 160 350 155 Q 530 160 530 238 L 530 830 Z" fill="none" stroke="#ffd700" stroke-width="0.5"/>
<path d="M 182 238 Q 208 195 250 174 Q 296 155 350 153 Q 404 155 450 174 Q 492 195 518 238" fill="#e8500a" opacity="0.15" stroke="#e8500a" stroke-width="1"/>
<path d="M 186 232 Q 214 196 240 181 Q 253 173 266 181 Q 278 191 286 207 Q 298 186 315 173 Q 333 162 350 164 Q 367 162 385 173 Q 402 186 414 207 Q 422 191 434 181 Q 447 173 460 181 Q 472 191 490 208 Q 505 222 514 232" fill="none" stroke="#e8500a" stroke-width="1.2"/>
<!-- PILLARS -->
<rect x="154" y="296" width="18" height="534" fill="#e8d5a0" stroke="#e8500a" stroke-width="1"/>
<rect x="144" y="283" width="38" height="16" rx="2" fill="#e8500a"/>
<rect x="141" y="270" width="44" height="14" rx="2" fill="#ffd700"/>
<rect x="144" y="828" width="38" height="14" rx="2" fill="#e8500a"/>
<rect x="141" y="842" width="44" height="12" rx="2" fill="#ffd700"/>
<rect x="528" y="296" width="18" height="534" fill="#e8d5a0" stroke="#e8500a" stroke-width="1"/>
<rect x="518" y="283" width="38" height="16" rx="2" fill="#e8500a"/>
<rect x="515" y="270" width="44" height="14" rx="2" fill="#ffd700"/>
<rect x="518" y="828" width="38" height="14" rx="2" fill="#e8500a"/>
<rect x="515" y="842" width="44" height="12" rx="2" fill="#ffd700"/>
<!-- LEFT LOTUS DECORATION (instead of peacock) -->
{% for i in range(5) %}
<ellipse cx="{{ 65 + i*6 }}" cy="{{ 430 - i*30 }}" rx="{{ 12 - i*1.5 }}" ry="{{ 20 - i*3 }}" fill="#e8500a" opacity="{{ 0.9 - i*0.1 }}" transform="rotate({{ -20 + i*5 }} 88 480)"/>
<ellipse cx="{{ 111 - i*6 }}" cy="{{ 430 - i*30 }}" rx="{{ 12 - i*1.5 }}" ry="{{ 20 - i*3 }}" fill="#8a0000" opacity="{{ 0.9 - i*0.1 }}" transform="rotate({{ 20 - i*5 }} 88 480)"/>
{% endfor %}
<circle cx="88" cy="400" r="20" fill="#e8500a"/>
<circle cx="88" cy="400" r="14" fill="#ffd700"/>
<circle cx="88" cy="400" r="8"  fill="#8a0000"/>
<!-- stem -->
<path d="M88 420 Q80 480 75 560" stroke="#8a0000" stroke-width="6" fill="none"/>
<path d="M88 420 Q80 480 75 560" stroke="#e8500a" stroke-width="3" fill="none"/>
<!-- leaf -->
<ellipse cx="65" cy="510" rx="25" ry="12" fill="#8a0000" opacity="0.7" transform="rotate(-20 65 510)"/>
<!-- RIGHT LOTUS (mirror) -->
{% for i in range(5) %}
<ellipse cx="{{ 635 - i*6 }}" cy="{{ 430 - i*30 }}" rx="{{ 12 - i*1.5 }}" ry="{{ 20 - i*3 }}" fill="#e8500a" opacity="{{ 0.9 - i*0.1 }}" transform="rotate({{ 20 - i*5 }} 612 480)"/>
<ellipse cx="{{ 589 + i*6 }}" cy="{{ 430 - i*30 }}" rx="{{ 12 - i*1.5 }}" ry="{{ 20 - i*3 }}" fill="#8a0000" opacity="{{ 0.9 - i*0.1 }}" transform="rotate({{ -20 + i*5 }} 612 480)"/>
{% endfor %}
<circle cx="612" cy="400" r="20" fill="#e8500a"/>
<circle cx="612" cy="400" r="14" fill="#ffd700"/>
<circle cx="612" cy="400" r="8"  fill="#8a0000"/>
<path d="M612 420 Q620 480 625 560" stroke="#8a0000" stroke-width="6" fill="none"/>
<path d="M612 420 Q620 480 625 560" stroke="#e8500a" stroke-width="3" fill="none"/>
<ellipse cx="635" cy="510" rx="25" ry="12" fill="#8a0000" opacity="0.7" transform="rotate(20 635 510)"/>
<!-- TEXT -->
<text x="350" y="198" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11" fill="#8a4a10" letter-spacing="3">|| Shri Ganeshaya Namah ||</text>
<text x="350" y="220" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="10" fill="#9a5a20">The families joyfully invite you</text>
<line x1="215" y1="230" x2="485" y2="230" stroke="#e8500a" stroke-width="0.8"/>
<polygon points="350,226 356,230 350,234 344,230" fill="#e8500a"/>
<text x="350" y="268" text-anchor="middle" font-family="'Great Vibes',cursive,Georgia,serif" font-size="40" fill="#8a0000">{{ details.bride_name }}</text>
<line x1="215" y1="278" x2="485" y2="278" stroke="#e8500a" stroke-width="0.5"/>
<text x="350" y="308" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="16" fill="#e8500a" letter-spacing="5">~ weds ~</text>
<text x="350" y="348" text-anchor="middle" font-family="'Great Vibes',cursive,Georgia,serif" font-size="40" fill="#5a0000">{{ details.groom_name }}</text>
<line x1="215" y1="358" x2="485" y2="358" stroke="#e8500a" stroke-width="0.5"/>
<polygon points="350,354 356,358 350,362 344,358" fill="#e8500a"/>
{% set fd = details.wedding_date.split('-') %}
{% set months = ['','January','February','March','April','May','June','July','August','September','October','November','December'] %}
{% if fd|length == 3 %}
<text x="350" y="386" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="14" fill="#3a2000" font-weight="bold">{{ months[fd[1]|int] }} {{ fd[2] }}, {{ fd[0] }}</text>
{% else %}
<text x="350" y="386" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="14" fill="#3a2000">{{ details.wedding_date }}</text>
{% endif %}
{% if details.ceremony_time %}
<text x="350" y="406" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="13" fill="#5a3a10">{{ details.ceremony_time }}</text>
{% endif %}
<line x1="215" y1="420" x2="485" y2="420" stroke="#e8500a" stroke-width="0.5"/>
<text x="350" y="440" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="9" fill="#8a4a20" letter-spacing="3">VENUE</text>
<text x="350" y="462" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="16" fill="#2a1800" font-weight="bold">{{ details.venue_name }}</text>
<text x="350" y="480" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="12" fill="#5a3a10">{{ details.venue_city }}</text>
<line x1="215" y1="493" x2="485" y2="493" stroke="#e8500a" stroke-width="0.5"/>
<polygon points="350,489 356,493 350,497 344,493" fill="#e8500a"/>
{% set words = invitation_text.split() %}
{% set l1 = words[:8]   | join(' ') %}{% set l2 = words[8:16]  | join(' ') %}
{% set l3 = words[16:24] | join(' ') %}{% set l4 = words[24:32] | join(' ') %}
{% set l5 = words[32:40] | join(' ') %}
<text x="350" y="516" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#4a3010" font-style="italic">{{ l1 }}</text>
{% if l2 %}<text x="350" y="533" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#4a3010" font-style="italic">{{ l2 }}</text>{% endif %}
{% if l3 %}<text x="350" y="550" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#4a3010" font-style="italic">{{ l3 }}</text>{% endif %}
{% if l4 %}<text x="350" y="567" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#4a3010" font-style="italic">{{ l4 }}</text>{% endif %}
{% if l5 %}<text x="350" y="584" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#4a3010" font-style="italic">{{ l5 }}</text>{% endif %}
<line x1="215" y1="600" x2="485" y2="600" stroke="#e8500a" stroke-width="0.5"/>
<ellipse cx="350" cy="618" rx="95" ry="13" fill="#8a0000" opacity="0.9"/>
<text x="350" y="623" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11" fill="#ffd0a0" letter-spacing="1">We joyfully await your presence</text>
{% if details.ceremonies %}
<text x="350" y="648" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="10" fill="#8a4a20" font-style="italic">* Celebrations schedule on next page</text>
{% endif %}
''' + details_box_and_footer("#e8500a","#ffd700","#8a0000","sindoor") + '''
<rect x="8" y="812" width="684" height="3" fill="#e8500a"/>
<rect x="8" y="815" width="684" height="49" fill="#8a0000"/>
<path d="M30 828 Q80 815 130 828 Q180 841 230 827 Q280 813 350 819 Q420 813 470 827 Q520 841 570 828 Q620 815 670 828" stroke="#e8500a" stroke-width="1.4" fill="none"/>
{% for lx in [75,160,245,350,455,540,625] %}
<ellipse cx="{{ lx }}" cy="830" rx="6" ry="10" fill="#ffd0a0"/>
<ellipse cx="{{ lx-6 }}" cy="835" rx="4.5" ry="7.5" fill="#e8500a"/>
<ellipse cx="{{ lx+6 }}" cy="835" rx="4.5" ry="7.5" fill="#e8500a"/>
<ellipse cx="{{ lx }}" cy="846" rx="8" ry="3.5" fill="#5a0000"/>
{% endfor %}
<text x="350" y="858" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="9" fill="#ffd0a0" letter-spacing="3">~ Sindoor Red · Sacred &amp; Traditional ~</text>
</svg>
</div>
''' + page2("#1a0000","#5a0808","#8a0000","#e8500a","#ffd700","#ffd0a0","#fff8f0") + SCRIPT


# ═══════════════════════════════════════════════════════════════════════
# CARD 4: MIDNIGHT LOTUS
# Navy + silver + lotus pattern
# ═══════════════════════════════════════════════════════════════════════
midnight_card = html_wrapper("Midnight Lotus", "#040820", "#6080c0", "#040820") + '''
<div class="card-container">
<svg class="card-svg" viewBox="0 0 700 880" xmlns="http://www.w3.org/2000/svg">
<defs>
  <pattern id="bgp" patternUnits="userSpaceOnUse" width="40" height="40">
    <rect width="40" height="40" fill="#040820"/>
    <circle cx="20" cy="20" r="1.2" fill="#0a1845" opacity="0.6"/>
    <circle cx="0" cy="0" r="0.8" fill="#0a1845" opacity="0.4"/>
    <circle cx="40" cy="40" r="0.8" fill="#0a1845" opacity="0.4"/>
    <path d="M0 20 L40 20" stroke="#0a1845" stroke-width="0.3" opacity="0.3"/>
    <path d="M20 0 L20 40" stroke="#0a1845" stroke-width="0.3" opacity="0.3"/>
  </pattern>
  <pattern id="creamp" patternUnits="userSpaceOnUse" width="18" height="18">
    <rect width="18" height="18" fill="#f0f4ff"/>
    <circle cx="9" cy="9" r="0.4" fill="#6080c0" opacity="0.15"/>
  </pattern>
</defs>
<rect width="700" height="880" fill="url(#bgp)"/>
<rect x="8"  y="8"  width="684" height="864" rx="3" fill="none" stroke="#6080c0" stroke-width="2.5"/>
<rect x="14" y="14" width="672" height="852" rx="2" fill="none" stroke="#a0c0f0" stroke-width="0.8"/>
<rect x="18" y="18" width="664" height="844" rx="2" fill="none" stroke="#6080c0" stroke-width="0.5"/>
<!-- CORNER ORNAMENTS -->
<path d="M8 8 L62 8 L62 13 L18 13 L18 62 L8 62 Z" fill="#6080c0"/>
<circle cx="36" cy="36" r="10" fill="#6080c0"/><circle cx="36" cy="36" r="7" fill="#040820"/><circle cx="36" cy="36" r="3.5" fill="#a0c0f0"/>
<ellipse cx="36" cy="22" rx="3.5" ry="7" fill="#6080c0" opacity="0.8"/>
<ellipse cx="36" cy="50" rx="3.5" ry="7" fill="#6080c0" opacity="0.8"/>
<ellipse cx="22" cy="36" rx="7" ry="3.5" fill="#6080c0" opacity="0.8"/>
<ellipse cx="50" cy="36" rx="7" ry="3.5" fill="#6080c0" opacity="0.8"/>
<path d="M692 8 L638 8 L638 13 L682 13 L682 62 L692 62 Z" fill="#6080c0"/>
<circle cx="664" cy="36" r="10" fill="#6080c0"/><circle cx="664" cy="36" r="7" fill="#040820"/><circle cx="664" cy="36" r="3.5" fill="#a0c0f0"/>
<ellipse cx="664" cy="22" rx="3.5" ry="7" fill="#6080c0" opacity="0.8"/>
<ellipse cx="664" cy="50" rx="3.5" ry="7" fill="#6080c0" opacity="0.8"/>
<ellipse cx="650" cy="36" rx="7" ry="3.5" fill="#6080c0" opacity="0.8"/>
<ellipse cx="678" cy="36" rx="7" ry="3.5" fill="#6080c0" opacity="0.8"/>
<path d="M8 872 L62 872 L62 867 L18 867 L18 818 L8 818 Z" fill="#6080c0"/>
<circle cx="36" cy="844" r="10" fill="#6080c0"/><circle cx="36" cy="844" r="7" fill="#040820"/><circle cx="36" cy="844" r="3.5" fill="#a0c0f0"/>
<ellipse cx="36" cy="830" rx="3.5" ry="7" fill="#6080c0" opacity="0.8"/>
<ellipse cx="36" cy="858" rx="3.5" ry="7" fill="#6080c0" opacity="0.8"/>
<ellipse cx="22" cy="844" rx="7" ry="3.5" fill="#6080c0" opacity="0.8"/>
<ellipse cx="50" cy="844" rx="7" ry="3.5" fill="#6080c0" opacity="0.8"/>
<path d="M692 872 L638 872 L638 867 L682 867 L682 818 L692 818 Z" fill="#6080c0"/>
<circle cx="664" cy="844" r="10" fill="#6080c0"/><circle cx="664" cy="844" r="7" fill="#040820"/><circle cx="664" cy="844" r="3.5" fill="#a0c0f0"/>
<ellipse cx="664" cy="830" rx="3.5" ry="7" fill="#6080c0" opacity="0.8"/>
<ellipse cx="664" cy="858" rx="3.5" ry="7" fill="#6080c0" opacity="0.8"/>
<ellipse cx="650" cy="844" rx="7" ry="3.5" fill="#6080c0" opacity="0.8"/>
<ellipse cx="678" cy="844" rx="7" ry="3.5" fill="#6080c0" opacity="0.8"/>
<!-- TOP BAND -->
<rect x="8" y="8" width="684" height="56" fill="#0a1845"/>
<rect x="8" y="61" width="684" height="3" fill="#6080c0"/>
<path d="M30 48 Q80 35 130 48 Q180 61 230 46 Q280 31 350 37 Q420 31 470 46 Q520 61 570 48 Q620 35 670 48" stroke="#6080c0" stroke-width="1.5" fill="none"/>
<!-- stars in band -->
{% for lx in [75,160,245,350,455,540,625] %}
<circle cx="{{ lx }}" cy="34" r="7" fill="#6080c0" opacity="0.8"/>
<circle cx="{{ lx }}" cy="34" r="4" fill="#a0c0f0"/>
<circle cx="{{ lx }}" cy="34" r="1.5" fill="#040820"/>
<!-- star points -->
<line x1="{{ lx }}" y1="24" x2="{{ lx }}" y2="44" stroke="#a0c0f0" stroke-width="1" opacity="0.6"/>
<line x1="{{ lx-10 }}" y1="34" x2="{{ lx+10 }}" y2="34" stroke="#a0c0f0" stroke-width="1" opacity="0.6"/>
<line x1="{{ lx-7 }}" y1="27" x2="{{ lx+7 }}" y2="41" stroke="#a0c0f0" stroke-width="0.8" opacity="0.4"/>
<line x1="{{ lx+7 }}" y1="27" x2="{{ lx-7 }}" y2="41" stroke="#a0c0f0" stroke-width="0.8" opacity="0.4"/>
{% endfor %}
<!-- GANESH midnight theme -->
<circle cx="350" cy="90" r="32" fill="#6080c0"/>
<circle cx="350" cy="90" r="28" fill="#0a1845"/>
<circle cx="350" cy="90" r="23" fill="#6080c0"/>
<circle cx="350" cy="90" r="18" fill="#040820"/>
<text x="350" y="98" text-anchor="middle" font-size="22" fill="#a0c0f0" font-family="serif">ॐ</text>
<ellipse cx="350" cy="56"  rx="4.5" ry="9"  fill="#6080c0" opacity="0.8"/>
<ellipse cx="350" cy="124" rx="4.5" ry="9"  fill="#6080c0" opacity="0.8"/>
<ellipse cx="316" cy="90"  rx="9"   ry="4.5" fill="#6080c0" opacity="0.8"/>
<ellipse cx="384" cy="90"  rx="9"   ry="4.5" fill="#6080c0" opacity="0.8"/>
<line x1="100" y1="90" x2="316" y2="90" stroke="#6080c0" stroke-width="0.8"/>
<line x1="384" y1="90" x2="600" y2="90" stroke="#6080c0" stroke-width="0.8"/>
<polygon points="150,90 158,85 166,90 158,95" fill="#6080c0"/>
<polygon points="220,90 228,85 236,90 228,95" fill="#6080c0"/>
<polygon points="464,90 472,85 480,90 472,95" fill="#6080c0"/>
<polygon points="534,90 542,85 550,90 542,95" fill="#6080c0"/>
<!-- PALE BLUE ARCH PANEL -->
<path d="M 162 830 L 162 234 Q 162 148 350 142 Q 538 148 538 234 L 538 830 Z" fill="url(#creamp)" stroke="#6080c0" stroke-width="1.5"/>
<path d="M 170 830 L 170 238 Q 170 160 350 155 Q 530 160 530 238 L 530 830 Z" fill="none" stroke="#a0c0f0" stroke-width="0.5"/>
<path d="M 182 238 Q 208 195 250 174 Q 296 155 350 153 Q 404 155 450 174 Q 492 195 518 238" fill="#6080c0" opacity="0.15" stroke="#6080c0" stroke-width="1"/>
<path d="M 186 232 Q 214 196 240 181 Q 253 173 266 181 Q 278 191 286 207 Q 298 186 315 173 Q 333 162 350 164 Q 367 162 385 173 Q 402 186 414 207 Q 422 191 434 181 Q 447 173 460 181 Q 472 191 490 208 Q 505 222 514 232" fill="none" stroke="#6080c0" stroke-width="1.2"/>
<!-- PILLARS -->
<rect x="154" y="296" width="18" height="534" fill="#d0d8f0" stroke="#6080c0" stroke-width="1"/>
<rect x="144" y="283" width="38" height="16" rx="2" fill="#6080c0"/>
<rect x="141" y="270" width="44" height="14" rx="2" fill="#a0c0f0"/>
<rect x="144" y="828" width="38" height="14" rx="2" fill="#6080c0"/>
<rect x="141" y="842" width="44" height="12" rx="2" fill="#a0c0f0"/>
<rect x="528" y="296" width="18" height="534" fill="#d0d8f0" stroke="#6080c0" stroke-width="1"/>
<rect x="518" y="283" width="38" height="16" rx="2" fill="#6080c0"/>
<rect x="515" y="270" width="44" height="14" rx="2" fill="#a0c0f0"/>
<rect x="518" y="828" width="38" height="14" rx="2" fill="#6080c0"/>
<rect x="515" y="842" width="44" height="12" rx="2" fill="#a0c0f0"/>
<!-- LEFT LOTUS (night blooming) -->
<path d="M88 590 Q85 520 88 460" stroke="#0a1845" stroke-width="8" fill="none"/>
<path d="M88 590 Q85 520 88 460" stroke="#6080c0" stroke-width="4" fill="none"/>
<ellipse cx="65" cy="530" rx="22" ry="10" fill="#0a1845" opacity="0.7" transform="rotate(-25 65 530)"/>
<ellipse cx="111" cy="530" rx="22" ry="10" fill="#0a1845" opacity="0.7" transform="rotate(25 111 530)"/>
{% for i in range(6) %}
<ellipse cx="{{ 88 }}" cy="{{ 430 - i*5 }}" rx="{{ 14 - i*1.5 }}" ry="{{ 22 - i*3 }}" fill="#6080c0" opacity="{{ 0.85 - i*0.08 }}" transform="rotate({{ -25 + i*8 }} 88 460)"/>
{% endfor %}
{% for i in range(6) %}
<ellipse cx="{{ 88 }}" cy="{{ 430 - i*5 }}" rx="{{ 14 - i*1.5 }}" ry="{{ 22 - i*3 }}" fill="#a0c0f0" opacity="{{ 0.6 - i*0.06 }}" transform="rotate({{ 25 - i*8 }} 88 460)"/>
{% endfor %}
<circle cx="88" cy="418" r="16" fill="#6080c0"/>
<circle cx="88" cy="418" r="11" fill="#a0c0f0"/>
<circle cx="88" cy="418" r="6"  fill="#040820"/>
<circle cx="88" cy="418" r="3"  fill="#a0c0f0"/>
<!-- right lotus mirror -->
<path d="M612 590 Q615 520 612 460" stroke="#0a1845" stroke-width="8" fill="none"/>
<path d="M612 590 Q615 520 612 460" stroke="#6080c0" stroke-width="4" fill="none"/>
<ellipse cx="589" cy="530" rx="22" ry="10" fill="#0a1845" opacity="0.7" transform="rotate(25 589 530)"/>
<ellipse cx="635" cy="530" rx="22" ry="10" fill="#0a1845" opacity="0.7" transform="rotate(-25 635 530)"/>
{% for i in range(6) %}
<ellipse cx="{{ 612 }}" cy="{{ 430 - i*5 }}" rx="{{ 14 - i*1.5 }}" ry="{{ 22 - i*3 }}" fill="#6080c0" opacity="{{ 0.85 - i*0.08 }}" transform="rotate({{ 25 - i*8 }} 612 460)"/>
{% endfor %}
{% for i in range(6) %}
<ellipse cx="{{ 612 }}" cy="{{ 430 - i*5 }}" rx="{{ 14 - i*1.5 }}" ry="{{ 22 - i*3 }}" fill="#a0c0f0" opacity="{{ 0.6 - i*0.06 }}" transform="rotate({{ -25 + i*8 }} 612 460)"/>
{% endfor %}
<circle cx="612" cy="418" r="16" fill="#6080c0"/>
<circle cx="612" cy="418" r="11" fill="#a0c0f0"/>
<circle cx="612" cy="418" r="6"  fill="#040820"/>
<circle cx="612" cy="418" r="3"  fill="#a0c0f0"/>
<!-- TEXT -->
<text x="350" y="198" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11" fill="#5060a0" letter-spacing="3">|| Shri Ganeshaya Namah ||</text>
<text x="350" y="220" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="10" fill="#6070b0">The families joyfully invite you</text>
<line x1="215" y1="230" x2="485" y2="230" stroke="#6080c0" stroke-width="0.8"/>
<polygon points="350,226 356,230 350,234 344,230" fill="#6080c0"/>
<text x="350" y="268" text-anchor="middle" font-family="'Great Vibes',cursive,Georgia,serif" font-size="40" fill="#3050a0">{{ details.bride_name }}</text>
<line x1="215" y1="278" x2="485" y2="278" stroke="#6080c0" stroke-width="0.5"/>
<text x="350" y="308" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="16" fill="#6080c0" letter-spacing="5">~ weds ~</text>
<text x="350" y="348" text-anchor="middle" font-family="'Great Vibes',cursive,Georgia,serif" font-size="40" fill="#204080">{{ details.groom_name }}</text>
<line x1="215" y1="358" x2="485" y2="358" stroke="#6080c0" stroke-width="0.5"/>
<polygon points="350,354 356,358 350,362 344,358" fill="#6080c0"/>
{% set fd = details.wedding_date.split('-') %}
{% set months = ['','January','February','March','April','May','June','July','August','September','October','November','December'] %}
{% if fd|length == 3 %}
<text x="350" y="386" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="14" fill="#2a3060" font-weight="bold">{{ months[fd[1]|int] }} {{ fd[2] }}, {{ fd[0] }}</text>
{% else %}
<text x="350" y="386" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="14" fill="#2a3060">{{ details.wedding_date }}</text>
{% endif %}
{% if details.ceremony_time %}
<text x="350" y="406" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="13" fill="#4050a0">{{ details.ceremony_time }}</text>
{% endif %}
<line x1="215" y1="420" x2="485" y2="420" stroke="#6080c0" stroke-width="0.5"/>
<text x="350" y="440" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="9" fill="#5060a0" letter-spacing="3">VENUE</text>
<text x="350" y="462" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="16" fill="#1a2050" font-weight="bold">{{ details.venue_name }}</text>
<text x="350" y="480" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="12" fill="#4050a0">{{ details.venue_city }}</text>
<line x1="215" y1="493" x2="485" y2="493" stroke="#6080c0" stroke-width="0.5"/>
<polygon points="350,489 356,493 350,497 344,493" fill="#6080c0"/>
{% set words = invitation_text.split() %}
{% set l1 = words[:8]   | join(' ') %}{% set l2 = words[8:16]  | join(' ') %}
{% set l3 = words[16:24] | join(' ') %}{% set l4 = words[24:32] | join(' ') %}
{% set l5 = words[32:40] | join(' ') %}
<text x="350" y="516" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#2a3060" font-style="italic">{{ l1 }}</text>
{% if l2 %}<text x="350" y="533" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#2a3060" font-style="italic">{{ l2 }}</text>{% endif %}
{% if l3 %}<text x="350" y="550" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#2a3060" font-style="italic">{{ l3 }}</text>{% endif %}
{% if l4 %}<text x="350" y="567" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#2a3060" font-style="italic">{{ l4 }}</text>{% endif %}
{% if l5 %}<text x="350" y="584" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#2a3060" font-style="italic">{{ l5 }}</text>{% endif %}
<line x1="215" y1="600" x2="485" y2="600" stroke="#6080c0" stroke-width="0.5"/>
<ellipse cx="350" cy="618" rx="95" ry="13" fill="#0a1845" opacity="0.9"/>
<text x="350" y="623" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11" fill="#a0c0f0" letter-spacing="1">We joyfully await your presence</text>
{% if details.ceremonies %}
<text x="350" y="648" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="10" fill="#5060a0" font-style="italic">* Celebrations schedule on next page</text>
{% endif %}
''' + details_box_and_footer("#6080c0","#a0c0f0","#0a1845","midnight") + '''
<rect x="8" y="812" width="684" height="3" fill="#6080c0"/>
<rect x="8" y="815" width="684" height="49" fill="#0a1845"/>
<path d="M30 828 Q80 815 130 828 Q180 841 230 827 Q280 813 350 819 Q420 813 470 827 Q520 841 570 828 Q620 815 670 828" stroke="#6080c0" stroke-width="1.4" fill="none"/>
{% for lx in [75,160,245,350,455,540,625] %}
<circle cx="{{ lx }}" cy="830" r="7" fill="#6080c0" opacity="0.8"/>
<circle cx="{{ lx }}" cy="830" r="4" fill="#a0c0f0"/>
<line x1="{{ lx }}" y1="820" x2="{{ lx }}" y2="840" stroke="#a0c0f0" stroke-width="0.8" opacity="0.5"/>
<line x1="{{ lx-10 }}" y1="830" x2="{{ lx+10 }}" y2="830" stroke="#a0c0f0" stroke-width="0.8" opacity="0.5"/>
{% endfor %}
<text x="350" y="858" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="9" fill="#a0c0f0" letter-spacing="3">~ Midnight Lotus · Elegant &amp; Serene ~</text>
</svg>
</div>
''' + page2("#040820","#0a1845","#0a1845","#6080c0","#a0c0f0","#a0c0f0","#f0f4ff") + SCRIPT


# ═══════════════════════════════════════════════════════════════════════
# CARD 5: ROSE MEHNDI
# Dusty rose + copper + mehndi vine patterns
# ═══════════════════════════════════════════════════════════════════════
rose_card = html_wrapper("Rose Mehndi", "#1a0810", "#e080a0", "#1a0810") + '''
<div class="card-container">
<svg class="card-svg" viewBox="0 0 700 880" xmlns="http://www.w3.org/2000/svg">
<defs>
  <pattern id="bgp" patternUnits="userSpaceOnUse" width="30" height="30">
    <rect width="30" height="30" fill="#1a0810"/>
    <circle cx="15" cy="15" r="1" fill="#4a1828" opacity="0.5"/>
    <circle cx="0" cy="0" r="0.6" fill="#4a1828" opacity="0.3"/>
    <circle cx="30" cy="30" r="0.6" fill="#4a1828" opacity="0.3"/>
  </pattern>
  <pattern id="creamp" patternUnits="userSpaceOnUse" width="18" height="18">
    <rect width="18" height="18" fill="#fff5f8"/>
    <circle cx="9" cy="9" r="0.4" fill="#e080a0" opacity="0.15"/>
  </pattern>
</defs>
<rect width="700" height="880" fill="url(#bgp)"/>
<rect x="8"  y="8"  width="684" height="864" rx="3" fill="none" stroke="#e080a0" stroke-width="2.5"/>
<rect x="14" y="14" width="672" height="852" rx="2" fill="none" stroke="#ffc0d0" stroke-width="0.8"/>
<rect x="18" y="18" width="664" height="844" rx="2" fill="none" stroke="#e080a0" stroke-width="0.5"/>
<!-- CORNER ORNAMENTS -->
<path d="M8 8 L62 8 L62 13 L18 13 L18 62 L8 62 Z" fill="#e080a0"/>
<circle cx="36" cy="36" r="10" fill="#e080a0"/><circle cx="36" cy="36" r="7" fill="#1a0810"/><circle cx="36" cy="36" r="3.5" fill="#ffc0d0"/>
<ellipse cx="36" cy="22" rx="3.5" ry="7" fill="#e080a0" opacity="0.8"/>
<ellipse cx="36" cy="50" rx="3.5" ry="7" fill="#e080a0" opacity="0.8"/>
<ellipse cx="22" cy="36" rx="7" ry="3.5" fill="#e080a0" opacity="0.8"/>
<ellipse cx="50" cy="36" rx="7" ry="3.5" fill="#e080a0" opacity="0.8"/>
<path d="M692 8 L638 8 L638 13 L682 13 L682 62 L692 62 Z" fill="#e080a0"/>
<circle cx="664" cy="36" r="10" fill="#e080a0"/><circle cx="664" cy="36" r="7" fill="#1a0810"/><circle cx="664" cy="36" r="3.5" fill="#ffc0d0"/>
<ellipse cx="664" cy="22" rx="3.5" ry="7" fill="#e080a0" opacity="0.8"/>
<ellipse cx="664" cy="50" rx="3.5" ry="7" fill="#e080a0" opacity="0.8"/>
<ellipse cx="650" cy="36" rx="7" ry="3.5" fill="#e080a0" opacity="0.8"/>
<ellipse cx="678" cy="36" rx="7" ry="3.5" fill="#e080a0" opacity="0.8"/>
<path d="M8 872 L62 872 L62 867 L18 867 L18 818 L8 818 Z" fill="#e080a0"/>
<circle cx="36" cy="844" r="10" fill="#e080a0"/><circle cx="36" cy="844" r="7" fill="#1a0810"/><circle cx="36" cy="844" r="3.5" fill="#ffc0d0"/>
<ellipse cx="36" cy="830" rx="3.5" ry="7" fill="#e080a0" opacity="0.8"/>
<ellipse cx="36" cy="858" rx="3.5" ry="7" fill="#e080a0" opacity="0.8"/>
<ellipse cx="22" cy="844" rx="7" ry="3.5" fill="#e080a0" opacity="0.8"/>
<ellipse cx="50" cy="844" rx="7" ry="3.5" fill="#e080a0" opacity="0.8"/>
<path d="M692 872 L638 872 L638 867 L682 867 L682 818 L692 818 Z" fill="#e080a0"/>
<circle cx="664" cy="844" r="10" fill="#e080a0"/><circle cx="664" cy="844" r="7" fill="#1a0810"/><circle cx="664" cy="844" r="3.5" fill="#ffc0d0"/>
<ellipse cx="664" cy="830" rx="3.5" ry="7" fill="#e080a0" opacity="0.8"/>
<ellipse cx="664" cy="858" rx="3.5" ry="7" fill="#e080a0" opacity="0.8"/>
<ellipse cx="650" cy="844" rx="7" ry="3.5" fill="#e080a0" opacity="0.8"/>
<ellipse cx="678" cy="844" rx="7" ry="3.5" fill="#e080a0" opacity="0.8"/>
<!-- TOP BAND with roses -->
<rect x="8" y="8" width="684" height="56" fill="#4a1828"/>
<rect x="8" y="61" width="684" height="3" fill="#e080a0"/>
<path d="M30 48 Q80 35 130 48 Q180 61 230 46 Q280 31 350 37 Q420 31 470 46 Q520 61 570 48 Q620 35 670 48" stroke="#e080a0" stroke-width="1.5" fill="none"/>
{% for lx in [75,160,245,350,455,540,625] %}
<circle cx="{{ lx }}" cy="34" r="9" fill="#e080a0" opacity="0.9"/>
<circle cx="{{ lx }}" cy="34" r="6" fill="#ff90b0"/>
<circle cx="{{ lx }}" cy="34" r="3" fill="#ffc0d0"/>
<ellipse cx="{{ lx-6 }}" cy="38" rx="5" ry="3" fill="#c06080" opacity="0.7"/>
<ellipse cx="{{ lx+6 }}" cy="38" rx="5" ry="3" fill="#c06080" opacity="0.7"/>
{% endfor %}
<!-- GANESH rose theme -->
<circle cx="350" cy="90" r="32" fill="#e080a0"/>
<circle cx="350" cy="90" r="28" fill="#4a1828"/>
<circle cx="350" cy="90" r="23" fill="#e080a0"/>
<circle cx="350" cy="90" r="18" fill="#1a0810"/>
<text x="350" y="98" text-anchor="middle" font-size="22" fill="#ffc0d0" font-family="serif">ॐ</text>
<ellipse cx="350" cy="56"  rx="4.5" ry="9"  fill="#e080a0" opacity="0.8"/>
<ellipse cx="350" cy="124" rx="4.5" ry="9"  fill="#e080a0" opacity="0.8"/>
<ellipse cx="316" cy="90"  rx="9"   ry="4.5" fill="#e080a0" opacity="0.8"/>
<ellipse cx="384" cy="90"  rx="9"   ry="4.5" fill="#e080a0" opacity="0.8"/>
<line x1="100" y1="90" x2="316" y2="90" stroke="#e080a0" stroke-width="0.8"/>
<line x1="384" y1="90" x2="600" y2="90" stroke="#e080a0" stroke-width="0.8"/>
<polygon points="150,90 158,85 166,90 158,95" fill="#e080a0"/>
<polygon points="220,90 228,85 236,90 228,95" fill="#e080a0"/>
<polygon points="464,90 472,85 480,90 472,95" fill="#e080a0"/>
<polygon points="534,90 542,85 550,90 542,95" fill="#e080a0"/>
<!-- PINK CREAM ARCH PANEL -->
<path d="M 162 830 L 162 234 Q 162 148 350 142 Q 538 148 538 234 L 538 830 Z" fill="url(#creamp)" stroke="#e080a0" stroke-width="1.5"/>
<path d="M 170 830 L 170 238 Q 170 160 350 155 Q 530 160 530 238 L 530 830 Z" fill="none" stroke="#ffc0d0" stroke-width="0.5"/>
<path d="M 182 238 Q 208 195 250 174 Q 296 155 350 153 Q 404 155 450 174 Q 492 195 518 238" fill="#e080a0" opacity="0.15" stroke="#e080a0" stroke-width="1"/>
<path d="M 186 232 Q 214 196 240 181 Q 253 173 266 181 Q 278 191 286 207 Q 298 186 315 173 Q 333 162 350 164 Q 367 162 385 173 Q 402 186 414 207 Q 422 191 434 181 Q 447 173 460 181 Q 472 191 490 208 Q 505 222 514 232" fill="none" stroke="#e080a0" stroke-width="1.2"/>
<!-- PILLARS -->
<rect x="154" y="296" width="18" height="534" fill="#f0d0d8" stroke="#e080a0" stroke-width="1"/>
<rect x="144" y="283" width="38" height="16" rx="2" fill="#e080a0"/>
<rect x="141" y="270" width="44" height="14" rx="2" fill="#ffc0d0"/>
<rect x="144" y="828" width="38" height="14" rx="2" fill="#e080a0"/>
<rect x="141" y="842" width="44" height="12" rx="2" fill="#ffc0d0"/>
<rect x="528" y="296" width="18" height="534" fill="#f0d0d8" stroke="#e080a0" stroke-width="1"/>
<rect x="518" y="283" width="38" height="16" rx="2" fill="#e080a0"/>
<rect x="515" y="270" width="44" height="14" rx="2" fill="#ffc0d0"/>
<rect x="518" y="828" width="38" height="14" rx="2" fill="#e080a0"/>
<rect x="515" y="842" width="44" height="12" rx="2" fill="#ffc0d0"/>
<!-- LEFT MEHNDI VINE -->
<path d="M88 600 Q75 540 80 480 Q85 420 88 360" stroke="#4a1828" stroke-width="5" fill="none" stroke-linecap="round"/>
<path d="M88 600 Q75 540 80 480 Q85 420 88 360" stroke="#e080a0" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<!-- rose buds on vine -->
{% for vy in [370, 420, 470, 520, 570] %}
<circle cx="{{ 82 + loop.index0 * 3 }}" cy="{{ vy }}" r="10" fill="#4a1828"/>
<circle cx="{{ 82 + loop.index0 * 3 }}" cy="{{ vy }}" r="7"  fill="#e080a0"/>
<circle cx="{{ 82 + loop.index0 * 3 }}" cy="{{ vy }}" r="4"  fill="#ff90b0"/>
<ellipse cx="{{ 70 + loop.index0 * 3 }}" cy="{{ vy + 5 }}" rx="8" ry="4" fill="#c06080" opacity="0.6"/>
<ellipse cx="{{ 94 + loop.index0 * 3 }}" cy="{{ vy + 5 }}" rx="8" ry="4" fill="#c06080" opacity="0.6"/>
{% endfor %}
<!-- RIGHT MEHNDI VINE -->
<path d="M612 600 Q625 540 620 480 Q615 420 612 360" stroke="#4a1828" stroke-width="5" fill="none" stroke-linecap="round"/>
<path d="M612 600 Q625 540 620 480 Q615 420 612 360" stroke="#e080a0" stroke-width="2.5" fill="none" stroke-linecap="round"/>
{% for vy in [370, 420, 470, 520, 570] %}
<circle cx="{{ 618 - loop.index0 * 3 }}" cy="{{ vy }}" r="10" fill="#4a1828"/>
<circle cx="{{ 618 - loop.index0 * 3 }}" cy="{{ vy }}" r="7"  fill="#e080a0"/>
<circle cx="{{ 618 - loop.index0 * 3 }}" cy="{{ vy }}" r="4"  fill="#ff90b0"/>
<ellipse cx="{{ 606 - loop.index0 * 3 }}" cy="{{ vy + 5 }}" rx="8" ry="4" fill="#c06080" opacity="0.6"/>
<ellipse cx="{{ 630 - loop.index0 * 3 }}" cy="{{ vy + 5 }}" rx="8" ry="4" fill="#c06080" opacity="0.6"/>
{% endfor %}
<!-- TEXT -->
<text x="350" y="198" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11" fill="#9a5070" letter-spacing="3">|| Shri Ganeshaya Namah ||</text>
<text x="350" y="220" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="10" fill="#b06080">The families joyfully invite you</text>
<line x1="215" y1="230" x2="485" y2="230" stroke="#e080a0" stroke-width="0.8"/>
<polygon points="350,226 356,230 350,234 344,230" fill="#e080a0"/>
<text x="350" y="268" text-anchor="middle" font-family="'Great Vibes',cursive,Georgia,serif" font-size="40" fill="#8a1840">{{ details.bride_name }}</text>
<line x1="215" y1="278" x2="485" y2="278" stroke="#e080a0" stroke-width="0.5"/>
<text x="350" y="308" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="16" fill="#e080a0" letter-spacing="5">~ weds ~</text>
<text x="350" y="348" text-anchor="middle" font-family="'Great Vibes',cursive,Georgia,serif" font-size="40" fill="#5a1030">{{ details.groom_name }}</text>
<line x1="215" y1="358" x2="485" y2="358" stroke="#e080a0" stroke-width="0.5"/>
<polygon points="350,354 356,358 350,362 344,358" fill="#e080a0"/>
{% set fd = details.wedding_date.split('-') %}
{% set months = ['','January','February','March','April','May','June','July','August','September','October','November','December'] %}
{% if fd|length == 3 %}
<text x="350" y="386" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="14" fill="#3a1828" font-weight="bold">{{ months[fd[1]|int] }} {{ fd[2] }}, {{ fd[0] }}</text>
{% else %}
<text x="350" y="386" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="14" fill="#3a1828">{{ details.wedding_date }}</text>
{% endif %}
{% if details.ceremony_time %}
<text x="350" y="406" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="13" fill="#5a2838">{{ details.ceremony_time }}</text>
{% endif %}
<line x1="215" y1="420" x2="485" y2="420" stroke="#e080a0" stroke-width="0.5"/>
<text x="350" y="440" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="9" fill="#9a5070" letter-spacing="3">VENUE</text>
<text x="350" y="462" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="16" fill="#2a1020" font-weight="bold">{{ details.venue_name }}</text>
<text x="350" y="480" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="12" fill="#5a2838">{{ details.venue_city }}</text>
<line x1="215" y1="493" x2="485" y2="493" stroke="#e080a0" stroke-width="0.5"/>
<polygon points="350,489 356,493 350,497 344,493" fill="#e080a0"/>
{% set words = invitation_text.split() %}
{% set l1 = words[:8]   | join(' ') %}{% set l2 = words[8:16]  | join(' ') %}
{% set l3 = words[16:24] | join(' ') %}{% set l4 = words[24:32] | join(' ') %}
{% set l5 = words[32:40] | join(' ') %}
<text x="350" y="516" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#3a1828" font-style="italic">{{ l1 }}</text>
{% if l2 %}<text x="350" y="533" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#3a1828" font-style="italic">{{ l2 }}</text>{% endif %}
{% if l3 %}<text x="350" y="550" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#3a1828" font-style="italic">{{ l3 }}</text>{% endif %}
{% if l4 %}<text x="350" y="567" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#3a1828" font-style="italic">{{ l4 }}</text>{% endif %}
{% if l5 %}<text x="350" y="584" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#3a1828" font-style="italic">{{ l5 }}</text>{% endif %}
<line x1="215" y1="600" x2="485" y2="600" stroke="#e080a0" stroke-width="0.5"/>
<ellipse cx="350" cy="618" rx="95" ry="13" fill="#4a1828" opacity="0.9"/>
<text x="350" y="623" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11" fill="#ffc0d0" letter-spacing="1">We joyfully await your presence</text>
{% if details.ceremonies %}
<text x="350" y="648" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="10" fill="#9a5070" font-style="italic">* Celebrations schedule on next page</text>
{% endif %}
''' + details_box_and_footer("#e080a0","#ffc0d0","#4a1828","rose") + '''
<rect x="8" y="812" width="684" height="3" fill="#e080a0"/>
<rect x="8" y="815" width="684" height="49" fill="#4a1828"/>
<path d="M30 828 Q80 815 130 828 Q180 841 230 827 Q280 813 350 819 Q420 813 470 827 Q520 841 570 828 Q620 815 670 828" stroke="#e080a0" stroke-width="1.4" fill="none"/>
{% for lx in [75,160,245,350,455,540,625] %}
<circle cx="{{ lx }}" cy="830" r="8" fill="#e080a0" opacity="0.9"/>
<circle cx="{{ lx }}" cy="830" r="5" fill="#ff90b0"/>
<circle cx="{{ lx }}" cy="830" r="2.5" fill="#ffc0d0"/>
<ellipse cx="{{ lx-5 }}" cy="835" rx="5" ry="2.5" fill="#c06080" opacity="0.6"/>
<ellipse cx="{{ lx+5 }}" cy="835" rx="5" ry="2.5" fill="#c06080" opacity="0.6"/>
{% endfor %}
<text x="350" y="858" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="9" fill="#ffc0d0" letter-spacing="3">~ Rose Mehndi · Romantic &amp; Beautiful ~</text>
</svg>
</div>
''' + page2("#1a0810","#4a1828","#4a1828","#e080a0","#ffc0d0","#ffc0d0","#fff5f8") + SCRIPT


# ═══════════════════════════════════════════════════════════════════════
# CARD 6: FOREST SAGE
# Sage green + ivory + botanical vines
# ═══════════════════════════════════════════════════════════════════════
forest_card = html_wrapper("Forest Sage", "#081808", "#60a860", "#081808") + '''
<div class="card-container">
<svg class="card-svg" viewBox="0 0 700 880" xmlns="http://www.w3.org/2000/svg">
<defs>
  <pattern id="bgp" patternUnits="userSpaceOnUse" width="30" height="30">
    <rect width="30" height="30" fill="#081808"/>
    <circle cx="15" cy="15" r="1" fill="#204820" opacity="0.5"/>
    <circle cx="0" cy="0" r="0.6" fill="#204820" opacity="0.3"/>
    <circle cx="30" cy="30" r="0.6" fill="#204820" opacity="0.3"/>
  </pattern>
  <pattern id="creamp" patternUnits="userSpaceOnUse" width="18" height="18">
    <rect width="18" height="18" fill="#f5fff5"/>
    <circle cx="9" cy="9" r="0.4" fill="#60a860" opacity="0.15"/>
  </pattern>
</defs>
<rect width="700" height="880" fill="url(#bgp)"/>
<rect x="8"  y="8"  width="684" height="864" rx="3" fill="none" stroke="#60a860" stroke-width="2.5"/>
<rect x="14" y="14" width="672" height="852" rx="2" fill="none" stroke="#c0e8c0" stroke-width="0.8"/>
<rect x="18" y="18" width="664" height="844" rx="2" fill="none" stroke="#60a860" stroke-width="0.5"/>
<!-- CORNER ORNAMENTS -->
<path d="M8 8 L62 8 L62 13 L18 13 L18 62 L8 62 Z" fill="#60a860"/>
<circle cx="36" cy="36" r="10" fill="#60a860"/><circle cx="36" cy="36" r="7" fill="#081808"/><circle cx="36" cy="36" r="3.5" fill="#c0e8c0"/>
<ellipse cx="36" cy="22" rx="3.5" ry="7" fill="#60a860" opacity="0.8"/>
<ellipse cx="36" cy="50" rx="3.5" ry="7" fill="#60a860" opacity="0.8"/>
<ellipse cx="22" cy="36" rx="7" ry="3.5" fill="#60a860" opacity="0.8"/>
<ellipse cx="50" cy="36" rx="7" ry="3.5" fill="#60a860" opacity="0.8"/>
<path d="M692 8 L638 8 L638 13 L682 13 L682 62 L692 62 Z" fill="#60a860"/>
<circle cx="664" cy="36" r="10" fill="#60a860"/><circle cx="664" cy="36" r="7" fill="#081808"/><circle cx="664" cy="36" r="3.5" fill="#c0e8c0"/>
<ellipse cx="664" cy="22" rx="3.5" ry="7" fill="#60a860" opacity="0.8"/>
<ellipse cx="664" cy="50" rx="3.5" ry="7" fill="#60a860" opacity="0.8"/>
<ellipse cx="650" cy="36" rx="7" ry="3.5" fill="#60a860" opacity="0.8"/>
<ellipse cx="678" cy="36" rx="7" ry="3.5" fill="#60a860" opacity="0.8"/>
<path d="M8 872 L62 872 L62 867 L18 867 L18 818 L8 818 Z" fill="#60a860"/>
<circle cx="36" cy="844" r="10" fill="#60a860"/><circle cx="36" cy="844" r="7" fill="#081808"/><circle cx="36" cy="844" r="3.5" fill="#c0e8c0"/>
<ellipse cx="36" cy="830" rx="3.5" ry="7" fill="#60a860" opacity="0.8"/>
<ellipse cx="36" cy="858" rx="3.5" ry="7" fill="#60a860" opacity="0.8"/>
<ellipse cx="22" cy="844" rx="7" ry="3.5" fill="#60a860" opacity="0.8"/>
<ellipse cx="50" cy="844" rx="7" ry="3.5" fill="#60a860" opacity="0.8"/>
<path d="M692 872 L638 872 L638 867 L682 867 L682 818 L692 818 Z" fill="#60a860"/>
<circle cx="664" cy="844" r="10" fill="#60a860"/><circle cx="664" cy="844" r="7" fill="#081808"/><circle cx="664" cy="844" r="3.5" fill="#c0e8c0"/>
<ellipse cx="664" cy="830" rx="3.5" ry="7" fill="#60a860" opacity="0.8"/>
<ellipse cx="664" cy="858" rx="3.5" ry="7" fill="#60a860" opacity="0.8"/>
<ellipse cx="650" cy="844" rx="7" ry="3.5" fill="#60a860" opacity="0.8"/>
<ellipse cx="678" cy="844" rx="7" ry="3.5" fill="#60a860" opacity="0.8"/>
<!-- TOP BAND botanical -->
<rect x="8" y="8" width="684" height="56" fill="#204820"/>
<rect x="8" y="61" width="684" height="3" fill="#60a860"/>
<path d="M30 40 Q80 28 130 40 Q180 52 230 38 Q280 24 350 32 Q420 24 470 38 Q520 52 570 40 Q620 28 670 40" stroke="#60a860" stroke-width="1.5" fill="none"/>
{% for lx in [75,160,245,350,455,540,625] %}
<!-- leaf -->
<ellipse cx="{{ lx }}" cy="34" rx="10" ry="6" fill="#60a860"/>
<ellipse cx="{{ lx }}" cy="34" rx="7"  ry="4" fill="#80c880"/>
<line x1="{{ lx }}" y1="28" x2="{{ lx }}" y2="40" stroke="#408040" stroke-width="1"/>
<!-- small flower -->
<circle cx="{{ lx }}" cy="34" r="3" fill="#c0e8c0"/>
{% endfor %}
<!-- GANESH forest theme -->
<circle cx="350" cy="90" r="32" fill="#60a860"/>
<circle cx="350" cy="90" r="28" fill="#204820"/>
<circle cx="350" cy="90" r="23" fill="#60a860"/>
<circle cx="350" cy="90" r="18" fill="#081808"/>
<text x="350" y="98" text-anchor="middle" font-size="22" fill="#c0e8c0" font-family="serif">ॐ</text>
<ellipse cx="350" cy="56"  rx="4.5" ry="9"  fill="#60a860" opacity="0.8"/>
<ellipse cx="350" cy="124" rx="4.5" ry="9"  fill="#60a860" opacity="0.8"/>
<ellipse cx="316" cy="90"  rx="9"   ry="4.5" fill="#60a860" opacity="0.8"/>
<ellipse cx="384" cy="90"  rx="9"   ry="4.5" fill="#60a860" opacity="0.8"/>
<line x1="100" y1="90" x2="316" y2="90" stroke="#60a860" stroke-width="0.8"/>
<line x1="384" y1="90" x2="600" y2="90" stroke="#60a860" stroke-width="0.8"/>
<polygon points="150,90 158,85 166,90 158,95" fill="#60a860"/>
<polygon points="220,90 228,85 236,90 228,95" fill="#60a860"/>
<polygon points="464,90 472,85 480,90 472,95" fill="#60a860"/>
<polygon points="534,90 542,85 550,90 542,95" fill="#60a860"/>
<!-- IVORY ARCH -->
<path d="M 162 830 L 162 234 Q 162 148 350 142 Q 538 148 538 234 L 538 830 Z" fill="url(#creamp)" stroke="#60a860" stroke-width="1.5"/>
<path d="M 170 830 L 170 238 Q 170 160 350 155 Q 530 160 530 238 L 530 830 Z" fill="none" stroke="#c0e8c0" stroke-width="0.5"/>
<path d="M 182 238 Q 208 195 250 174 Q 296 155 350 153 Q 404 155 450 174 Q 492 195 518 238" fill="#60a860" opacity="0.15" stroke="#60a860" stroke-width="1"/>
<path d="M 186 232 Q 214 196 240 181 Q 253 173 266 181 Q 278 191 286 207 Q 298 186 315 173 Q 333 162 350 164 Q 367 162 385 173 Q 402 186 414 207 Q 422 191 434 181 Q 447 173 460 181 Q 472 191 490 208 Q 505 222 514 232" fill="none" stroke="#60a860" stroke-width="1.2"/>
<!-- PILLARS -->
<rect x="154" y="296" width="18" height="534" fill="#d8ead8" stroke="#60a860" stroke-width="1"/>
<rect x="144" y="283" width="38" height="16" rx="2" fill="#60a860"/>
<rect x="141" y="270" width="44" height="14" rx="2" fill="#c0e8c0"/>
<rect x="144" y="828" width="38" height="14" rx="2" fill="#60a860"/>
<rect x="141" y="842" width="44" height="12" rx="2" fill="#c0e8c0"/>
<rect x="528" y="296" width="18" height="534" fill="#d8ead8" stroke="#60a860" stroke-width="1"/>
<rect x="518" y="283" width="38" height="16" rx="2" fill="#60a860"/>
<rect x="515" y="270" width="44" height="14" rx="2" fill="#c0e8c0"/>
<rect x="518" y="828" width="38" height="14" rx="2" fill="#60a860"/>
<rect x="515" y="842" width="44" height="12" rx="2" fill="#c0e8c0"/>
<!-- LEFT BOTANICAL ARRANGEMENT -->
<path d="M88 600 Q82 540 85 480 Q88 420 86 360" stroke="#204820" stroke-width="6" fill="none" stroke-linecap="round"/>
<path d="M88 600 Q82 540 85 480 Q88 420 86 360" stroke="#60a860" stroke-width="3" fill="none" stroke-linecap="round"/>
<!-- leaves branching off -->
<ellipse cx="60" cy="560" rx="22" ry="10" fill="#60a860" opacity="0.8" transform="rotate(-30 60 560)"/>
<ellipse cx="115" cy="540" rx="20" ry="9"  fill="#408040" opacity="0.7" transform="rotate(25 115 540)"/>
<ellipse cx="58" cy="490" rx="20" ry="9"  fill="#60a860" opacity="0.8" transform="rotate(-35 58 490)"/>
<ellipse cx="116" cy="470" rx="18" ry="8"  fill="#408040" opacity="0.7" transform="rotate(30 116 470)"/>
<ellipse cx="62" cy="420" rx="18" ry="8"  fill="#60a860" opacity="0.8" transform="rotate(-25 62 420)"/>
<ellipse cx="114" cy="400" rx="16" ry="7"  fill="#408040" opacity="0.7" transform="rotate(20 114 400)"/>
<!-- flower tops -->
{% for fy in [360, 390, 430] %}
<circle cx="86" cy="{{ fy }}" r="8" fill="#204820"/>
<circle cx="86" cy="{{ fy }}" r="5" fill="#c0e8c0"/>
<circle cx="86" cy="{{ fy }}" r="2.5" fill="#60a860"/>
{% endfor %}
<!-- RIGHT BOTANICAL (mirror) -->
<path d="M612 600 Q618 540 615 480 Q612 420 614 360" stroke="#204820" stroke-width="6" fill="none" stroke-linecap="round"/>
<path d="M612 600 Q618 540 615 480 Q612 420 614 360" stroke="#60a860" stroke-width="3" fill="none" stroke-linecap="round"/>
<ellipse cx="640" cy="560" rx="22" ry="10" fill="#60a860" opacity="0.8" transform="rotate(30 640 560)"/>
<ellipse cx="585" cy="540" rx="20" ry="9"  fill="#408040" opacity="0.7" transform="rotate(-25 585 540)"/>
<ellipse cx="642" cy="490" rx="20" ry="9"  fill="#60a860" opacity="0.8" transform="rotate(35 642 490)"/>
<ellipse cx="584" cy="470" rx="18" ry="8"  fill="#408040" opacity="0.7" transform="rotate(-30 584 470)"/>
<ellipse cx="638" cy="420" rx="18" ry="8"  fill="#60a860" opacity="0.8" transform="rotate(25 638 420)"/>
<ellipse cx="586" cy="400" rx="16" ry="7"  fill="#408040" opacity="0.7" transform="rotate(-20 586 400)"/>
{% for fy in [360, 390, 430] %}
<circle cx="614" cy="{{ fy }}" r="8" fill="#204820"/>
<circle cx="614" cy="{{ fy }}" r="5" fill="#c0e8c0"/>
<circle cx="614" cy="{{ fy }}" r="2.5" fill="#60a860"/>
{% endfor %}
<!-- TEXT -->
<text x="350" y="198" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11" fill="#408040" letter-spacing="3">|| Shri Ganeshaya Namah ||</text>
<text x="350" y="220" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="10" fill="#508050">The families joyfully invite you</text>
<line x1="215" y1="230" x2="485" y2="230" stroke="#60a860" stroke-width="0.8"/>
<polygon points="350,226 356,230 350,234 344,230" fill="#60a860"/>
<text x="350" y="268" text-anchor="middle" font-family="'Great Vibes',cursive,Georgia,serif" font-size="40" fill="#204820">{{ details.bride_name }}</text>
<line x1="215" y1="278" x2="485" y2="278" stroke="#60a860" stroke-width="0.5"/>
<text x="350" y="308" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="16" fill="#60a860" letter-spacing="5">~ weds ~</text>
<text x="350" y="348" text-anchor="middle" font-family="'Great Vibes',cursive,Georgia,serif" font-size="40" fill="#103010">{{ details.groom_name }}</text>
<line x1="215" y1="358" x2="485" y2="358" stroke="#60a860" stroke-width="0.5"/>
<polygon points="350,354 356,358 350,362 344,358" fill="#60a860"/>
{% set fd = details.wedding_date.split('-') %}
{% set months = ['','January','February','March','April','May','June','July','August','September','October','November','December'] %}
{% if fd|length == 3 %}
<text x="350" y="386" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="14" fill="#1a3020" font-weight="bold">{{ months[fd[1]|int] }} {{ fd[2] }}, {{ fd[0] }}</text>
{% else %}
<text x="350" y="386" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="14" fill="#1a3020">{{ details.wedding_date }}</text>
{% endif %}
{% if details.ceremony_time %}
<text x="350" y="406" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="13" fill="#3a5038">{{ details.ceremony_time }}</text>
{% endif %}
<line x1="215" y1="420" x2="485" y2="420" stroke="#60a860" stroke-width="0.5"/>
<text x="350" y="440" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="9" fill="#508050" letter-spacing="3">VENUE</text>
<text x="350" y="462" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="16" fill="#0a1808" font-weight="bold">{{ details.venue_name }}</text>
<text x="350" y="480" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="12" fill="#3a5038">{{ details.venue_city }}</text>
<line x1="215" y1="493" x2="485" y2="493" stroke="#60a860" stroke-width="0.5"/>
<polygon points="350,489 356,493 350,497 344,493" fill="#60a860"/>
{% set words = invitation_text.split() %}
{% set l1 = words[:8]   | join(' ') %}{% set l2 = words[8:16]  | join(' ') %}
{% set l3 = words[16:24] | join(' ') %}{% set l4 = words[24:32] | join(' ') %}
{% set l5 = words[32:40] | join(' ') %}
<text x="350" y="516" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#1a3020" font-style="italic">{{ l1 }}</text>
{% if l2 %}<text x="350" y="533" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#1a3020" font-style="italic">{{ l2 }}</text>{% endif %}
{% if l3 %}<text x="350" y="550" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#1a3020" font-style="italic">{{ l3 }}</text>{% endif %}
{% if l4 %}<text x="350" y="567" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#1a3020" font-style="italic">{{ l4 }}</text>{% endif %}
{% if l5 %}<text x="350" y="584" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11.5" fill="#1a3020" font-style="italic">{{ l5 }}</text>{% endif %}
<line x1="215" y1="600" x2="485" y2="600" stroke="#60a860" stroke-width="0.5"/>
<ellipse cx="350" cy="618" rx="95" ry="13" fill="#204820" opacity="0.9"/>
<text x="350" y="623" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="11" fill="#c0e8c0" letter-spacing="1">We joyfully await your presence</text>
{% if details.ceremonies %}
<text x="350" y="648" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="10" fill="#508050" font-style="italic">* Celebrations schedule on next page</text>
{% endif %}
''' + details_box_and_footer("#60a860","#c0e8c0","#204820","forest") + '''
<rect x="8" y="812" width="684" height="3" fill="#60a860"/>
<rect x="8" y="815" width="684" height="49" fill="#204820"/>
<path d="M30 828 Q80 815 130 828 Q180 841 230 827 Q280 813 350 819 Q420 813 470 827 Q520 841 570 828 Q620 815 670 828" stroke="#60a860" stroke-width="1.4" fill="none"/>
{% for lx in [75,160,245,350,455,540,625] %}
<ellipse cx="{{ lx }}" cy="828" rx="10" ry="6" fill="#60a860"/>
<ellipse cx="{{ lx }}" cy="828" rx="7"  ry="4" fill="#80c880"/>
<line x1="{{ lx }}" y1="822" x2="{{ lx }}" y2="834" stroke="#408040" stroke-width="1"/>
<circle cx="{{ lx }}" cy="828" r="3" fill="#c0e8c0"/>
{% endfor %}
<text x="350" y="858" text-anchor="middle" font-family="'Cormorant Garamond',Georgia,serif" font-size="9" fill="#c0e8c0" letter-spacing="3">~ Forest Sage · Natural &amp; Serene ~</text>
</svg>
</div>
''' + page2("#081808","#204820","#204820","#60a860","#c0e8c0","#c0e8c0","#f5fff5") + SCRIPT


# ═══════════════════════
# WRITE ALL FILES
# ═══════════════════════
files = {
    "card_purple.html":   purple_card,
    "card_sindoor.html":  sindoor_card,
    "card_midnight.html": midnight_card,
    "card_rose.html":     rose_card,
    "card_forest.html":   forest_card,
}

for filename, content in files.items():
    filepath = os.path.join(BASE, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {filename}")

print("\nAll 5 card templates created!")