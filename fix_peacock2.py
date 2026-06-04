path = r"C:\PROJECTS\AI wedding card\templates\card_peacock.html"

content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ details.bride_name }} &amp; {{ details.groom_name }} — Wedding Invitation</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400;1,600&family=Great+Vibes&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body {
            background: #0a2818;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 30px 20px 60px;
            font-family: \'Cormorant Garamond\', Georgia, serif;
        }
        .action-bar {
            display: flex; gap: 14px; margin-bottom: 20px;
            flex-wrap: wrap; justify-content: center;
        }
        .btn-primary {
            padding: 13px 32px;
            background: linear-gradient(135deg, #d4a843, #e8c97a);
            color: #0a2818; border: none; border-radius: 8px;
            font-family: \'Montserrat\', sans-serif; font-size: 0.9rem;
            font-weight: 600; cursor: pointer; text-decoration: none;
            display: inline-block; transition: transform 0.2s, box-shadow 0.2s;
        }
        .btn-primary:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(212,168,67,0.4); }
        .btn-secondary {
            padding: 13px 32px; background: transparent; color: #d4a843;
            border: 2px solid #d4a843; border-radius: 8px;
            font-family: \'Montserrat\', sans-serif; font-size: 0.9rem;
            font-weight: 500; text-decoration: none; transition: all 0.2s; display: inline-block;
        }
        .btn-secondary:hover { background: #d4a843; color: #0a2818; }
        .share-row {
            display: flex; flex-direction: column; align-items: center;
            gap: 10px; margin-bottom: 28px; width: 100%; max-width: 720px;
        }
        .share-label {
            font-family: \'Montserrat\', sans-serif; font-size: 0.7rem;
            letter-spacing: 3px; text-transform: uppercase; color: #d4a843; opacity: 0.75;
        }
        .share-btns { display: flex; gap: 12px; flex-wrap: wrap; justify-content: center; }
        .share-btn {
            display: flex; align-items: center; gap: 8px; padding: 10px 22px;
            border-radius: 8px; font-family: \'Montserrat\', sans-serif;
            font-size: 0.85rem; font-weight: 500; text-decoration: none; transition: transform 0.2s;
        }
        .share-btn:hover { transform: translateY(-2px); }
        .wa { background: #25D366; color: white; }
        .em { background: #4a90d9; color: white; }
        .share-link-row { display: flex; gap: 8px; width: 100%; max-width: 500px; }
        .share-link-row input {
            flex: 1; padding: 9px 14px;
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(212,168,67,0.4);
            border-radius: 8px; color: #e8c97a; font-size: 0.82rem; outline: none;
            font-family: \'Montserrat\', sans-serif;
        }
        .copy-btn {
            padding: 9px 16px; background: #d4a843; color: #0a2818;
            border: none; border-radius: 8px; cursor: pointer;
            font-family: \'Montserrat\', sans-serif; font-size: 0.82rem;
            font-weight: 600; white-space: nowrap;
        }
        .page-label {
            font-family: \'Montserrat\', sans-serif; font-size: 0.7rem;
            letter-spacing: 3px; text-transform: uppercase;
            color: #d4a843; opacity: 0.6; margin: 20px 0 8px;
        }
        .card-container { width: 100%; max-width: 720px; position: relative; }
        .card-svg {
            width: 100%; height: auto; display: block;
            border-radius: 4px; box-shadow: 0 8px 60px rgba(0,0,0,0.6);
        }
        @media print {
            body { background: white; padding: 0; }
            .action-bar, .share-row, .page-label { display: none !important; }
            .card-container { max-width: 100%; page-break-after: always; }
            .card-container:last-child { page-break-after: auto; }
            .card-svg { box-shadow: none; width: 100%; }
            @page { size: A4 portrait; margin: 5mm; }
        }
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
        <a href="{{ whatsapp_url }}" target="_blank" class="share-btn wa">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
            </svg>
            WhatsApp
        </a>
        <a href="{{ email_url }}" class="share-btn em">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                <polyline points="22,6 12,12 2,6"/>
            </svg>
            Email
        </a>
    </div>
    {% if share_link %}
    <div class="share-link-row">
        <input type="text" value="{{ share_link }}" id="slink" readonly>
        <button class="copy-btn" id="copybtn" onclick="copyLink()">&#128203; Copy</button>
    </div>
    {% endif %}
</div>

<p class="page-label">Page 1 of {% if details.ceremonies %}2{% else %}1{% endif %} — Main Invitation</p>

<div class="card-container">
<svg class="card-svg" viewBox="0 0 700 880" xmlns="http://www.w3.org/2000/svg">
<defs>
  <pattern id="bgp" patternUnits="userSpaceOnUse" width="28" height="28">
    <rect width="28" height="28" fill="#0a3828"/>
    <circle cx="14" cy="14" r="1.1" fill="#1a6a48" opacity="0.45"/>
    <circle cx="0"  cy="0"  r="0.7" fill="#1a6a48" opacity="0.25"/>
    <circle cx="28" cy="28" r="0.7" fill="#1a6a48" opacity="0.25"/>
  </pattern>
  <pattern id="creamp" patternUnits="userSpaceOnUse" width="18" height="18">
    <rect width="18" height="18" fill="#fdf6e3"/>
    <circle cx="9" cy="9" r="0.5" fill="#d4a843" opacity="0.2"/>
  </pattern>
</defs>
<rect width="700" height="880" fill="url(#bgp)"/>
<rect x="8"  y="8"  width="684" height="864" rx="3" fill="none" stroke="#d4a843" stroke-width="2.5"/>
<rect x="14" y="14" width="672" height="852" rx="2" fill="none" stroke="#e8c97a" stroke-width="0.8"/>
<rect x="18" y="18" width="664" height="844" rx="2" fill="none" stroke="#c49030" stroke-width="0.5"/>
<path d="M8 8 L62 8 L62 13 L18 13 L18 62 L8 62 Z" fill="#d4a843"/>
<circle cx="36" cy="36" r="10" fill="#d4a843"/><circle cx="36" cy="36" r="7" fill="#0a3828"/><circle cx="36" cy="36" r="3.5" fill="#e8c97a"/>
<ellipse cx="36" cy="22" rx="3.5" ry="7" fill="#d4a843" opacity="0.75"/>
<ellipse cx="36" cy="50" rx="3.5" ry="7" fill="#d4a843" opacity="0.75"/>
<ellipse cx="22" cy="36" rx="7" ry="3.5" fill="#d4a843" opacity="0.75"/>
<ellipse cx="50" cy="36" rx="7" ry="3.5" fill="#d4a843" opacity="0.75"/>
<path d="M692 8 L638 8 L638 13 L682 13 L682 62 L692 62 Z" fill="#d4a843"/>
<circle cx="664" cy="36" r="10" fill="#d4a843"/><circle cx="664" cy="36" r="7" fill="#0a3828"/><circle cx="664" cy="36" r="3.5" fill="#e8c97a"/>
<ellipse cx="664" cy="22" rx="3.5" ry="7" fill="#d4a843" opacity="0.75"/>
<ellipse cx="664" cy="50" rx="3.5" ry="7" fill="#d4a843" opacity="0.75"/>
<ellipse cx="650" cy="36" rx="7" ry="3.5" fill="#d4a843" opacity="0.75"/>
<ellipse cx="678" cy="36" rx="7" ry="3.5" fill="#d4a843" opacity="0.75"/>
<path d="M8 872 L62 872 L62 867 L18 867 L18 818 L8 818 Z" fill="#d4a843"/>
<circle cx="36" cy="844" r="10" fill="#d4a843"/><circle cx="36" cy="844" r="7" fill="#0a3828"/><circle cx="36" cy="844" r="3.5" fill="#e8c97a"/>
<ellipse cx="36" cy="830" rx="3.5" ry="7" fill="#d4a843" opacity="0.75"/>
<ellipse cx="36" cy="858" rx="3.5" ry="7" fill="#d4a843" opacity="0.75"/>
<ellipse cx="22" cy="844" rx="7" ry="3.5" fill="#d4a843" opacity="0.75"/>
<ellipse cx="50" cy="844" rx="7" ry="3.5" fill="#d4a843" opacity="0.75"/>
<path d="M692 872 L638 872 L638 867 L682 867 L682 818 L692 818 Z" fill="#d4a843"/>
<circle cx="664" cy="844" r="10" fill="#d4a843"/><circle cx="664" cy="844" r="7" fill="#0a3828"/><circle cx="664" cy="844" r="3.5" fill="#e8c97a"/>
<ellipse cx="664" cy="830" rx="3.5" ry="7" fill="#d4a843" opacity="0.75"/>
<ellipse cx="664" cy="858" rx="3.5" ry="7" fill="#d4a843" opacity="0.75"/>
<ellipse cx="650" cy="844" rx="7" ry="3.5" fill="#d4a843" opacity="0.75"/>
<ellipse cx="678" cy="844" rx="7" ry="3.5" fill="#d4a843" opacity="0.75"/>
<rect x="8" y="8" width="684" height="56" fill="#1a5c3a"/>
<rect x="8" y="61" width="684" height="3" fill="#d4a843"/>
<path d="M30 48 Q80 35 130 48 Q180 61 230 46 Q280 31 350 37 Q420 31 470 46 Q520 61 570 48 Q620 35 670 48" stroke="#2a8a50" stroke-width="1.5" fill="none"/>
{% for lx in [75,160,245,350,455,540,625] %}
<ellipse cx="{{ lx }}" cy="34" rx="7" ry="10" fill="#e8c97a"/>
<ellipse cx="{{ lx-7 }}" cy="39" rx="5" ry="8" fill="#d4a843"/>
<ellipse cx="{{ lx+7 }}" cy="39" rx="5" ry="8" fill="#d4a843"/>
<ellipse cx="{{ lx }}" cy="50" rx="9" ry="4" fill="#0f4a2a"/>
{% endfor %}
<circle cx="350" cy="90" r="32" fill="#d4a843"/>
<circle cx="350" cy="90" r="28" fill="#1a5c3a"/>
<circle cx="350" cy="90" r="23" fill="#d4a843"/>
<circle cx="350" cy="90" r="18" fill="#0a3828"/>
<text x="350" y="98" text-anchor="middle" font-size="22" fill="#d4a843" font-family="serif">&#2384;</text>
<ellipse cx="350" cy="56"  rx="4.5" ry="9"  fill="#d4a843" opacity="0.8"/>
<ellipse cx="350" cy="124" rx="4.5" ry="9"  fill="#d4a843" opacity="0.8"/>
<ellipse cx="316" cy="90"  rx="9"   ry="4.5" fill="#d4a843" opacity="0.8"/>
<ellipse cx="384" cy="90"  rx="9"   ry="4.5" fill="#d4a843" opacity="0.8"/>
<line x1="100" y1="90" x2="316" y2="90" stroke="#d4a843" stroke-width="0.8"/>
<line x1="384" y1="90" x2="600" y2="90" stroke="#d4a843" stroke-width="0.8"/>
<polygon points="148,90 156,85 164,90 156,95" fill="#d4a843" opacity="0.85"/>
<polygon points="214,90 222,85 230,90 222,95" fill="#d4a843" opacity="0.85"/>
<polygon points="470,90 478,85 486,90 478,95" fill="#d4a843" opacity="0.85"/>
<polygon points="536,90 544,85 552,90 544,95" fill="#d4a843" opacity="0.85"/>
<path d="M 162 830 L 162 234 Q 162 148 350 142 Q 538 148 538 234 L 538 830 Z" fill="url(#creamp)" stroke="#d4a843" stroke-width="1.5"/>
<path d="M 170 830 L 170 238 Q 170 160 350 155 Q 530 160 530 238 L 530 830 Z" fill="none" stroke="#e8c97a" stroke-width="0.5"/>
<path d="M 182 238 Q 208 195 250 174 Q 296 155 350 153 Q 404 155 450 174 Q 492 195 518 238" fill="#d4a843" opacity="0.2" stroke="#d4a843" stroke-width="1"/>
<path d="M 186 232 Q 214 196 240 181 Q 253 173 266 181 Q 278 191 286 207 Q 298 186 315 173 Q 333 162 350 164 Q 367 162 385 173 Q 402 186 414 207 Q 422 191 434 181 Q 447 173 460 181 Q 472 191 490 208 Q 505 222 514 232" fill="none" stroke="#d4a843" stroke-width="1.2"/>
<rect x="154" y="296" width="18" height="534" fill="#e8d5a0" stroke="#c9a96e" stroke-width="1"/>
<rect x="149" y="296" width="7"  height="534" fill="#d4b870" opacity="0.35"/>
<rect x="174" y="296" width="7"  height="534" fill="#c49030" opacity="0.25"/>
<rect x="144" y="283" width="38" height="16" rx="2" fill="#d4a843"/>
<rect x="141" y="270" width="44" height="14" rx="2" fill="#e8c97a"/>
<rect x="138" y="259" width="50" height="13" rx="2" fill="#d4a843"/>
<rect x="144" y="828" width="38" height="14" rx="2" fill="#d4a843"/>
<rect x="141" y="842" width="44" height="12" rx="2" fill="#e8c97a"/>
<rect x="528" y="296" width="18" height="534" fill="#e8d5a0" stroke="#c9a96e" stroke-width="1"/>
<rect x="525" y="296" width="7"  height="534" fill="#d4b870" opacity="0.35"/>
<rect x="540" y="296" width="7"  height="534" fill="#c49030" opacity="0.25"/>
<rect x="518" y="283" width="38" height="16" rx="2" fill="#d4a843"/>
<rect x="515" y="270" width="44" height="14" rx="2" fill="#e8c97a"/>
<rect x="512" y="259" width="50" height="13" rx="2" fill="#d4a843"/>
<rect x="518" y="828" width="38" height="14" rx="2" fill="#d4a843"/>
<rect x="515" y="842" width="44" height="12" rx="2" fill="#e8c97a"/>
<ellipse cx="88" cy="490" rx="50" ry="65" fill="#1a7a52"/>
<ellipse cx="88" cy="478" rx="40" ry="53" fill="#228a5e"/>
<path d="M88 428 Q81 403 85 376 Q88 360 94 350" stroke="#1a7a52" stroke-width="17" fill="none" stroke-linecap="round"/>
<path d="M88 428 Q81 403 85 376 Q88 360 94 350" stroke="#2a9a6a" stroke-width="10" fill="none" stroke-linecap="round"/>
<circle cx="96"  cy="338" r="22" fill="#1a7a52"/>
<circle cx="96"  cy="338" r="15" fill="#2a9a6a"/>
<circle cx="103" cy="333" r="5"  fill="#082818"/>
<circle cx="105" cy="331" r="2"  fill="#d4a843"/>
<line x1="89"  y1="316" x2="80" y2="294" stroke="#2a9a6a" stroke-width="2"/>
<circle cx="80" cy="290" r="4.5" fill="#d4a843"/>
<line x1="96"  y1="314" x2="94" y2="290" stroke="#2a9a6a" stroke-width="2"/>
<circle cx="94" cy="286" r="4.5" fill="#d4a843"/>
<line x1="103" y1="316" x2="110" y2="294" stroke="#2a9a6a" stroke-width="2"/>
<circle cx="110" cy="290" r="4.5" fill="#d4a843"/>
<path d="M112 336 L128 339 L112 342 Z" fill="#c49030"/>
<path d="M50 516 Q16 435 26 342 Q31 300 42 270" stroke="#0d5a38" stroke-width="3.8" fill="none" stroke-linecap="round"/>
<path d="M62 530 Q24 446 40 353 Q46 310 60 278" stroke="#1a7a52" stroke-width="3.2" fill="none" stroke-linecap="round"/>
<path d="M76 542 Q48 460 66 368 Q74 325 90 294" stroke="#0d5a38" stroke-width="2.8" fill="none" stroke-linecap="round"/>
<path d="M40 494 Q8 416 14 324 Q18 282 28 254" stroke="#1a7a52" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<path d="M28 468 Q4 394 10 306 Q14 268 22 244" stroke="#0a4a30" stroke-width="2.2" fill="none" stroke-linecap="round"/>
<circle cx="42" cy="270" r="11" fill="#1a7a52"/><circle cx="42" cy="270" r="8"  fill="#d4a843"/><circle cx="42" cy="270" r="5"  fill="#0a2818"/><circle cx="42" cy="270" r="2.2" fill="#e8c97a"/>
<circle cx="60" cy="278" r="10" fill="#1a7a52"/><circle cx="60" cy="278" r="7"  fill="#d4a843"/><circle cx="60" cy="278" r="4.5" fill="#0a2818"/><circle cx="60" cy="278" r="2"   fill="#e8c97a"/>
<circle cx="90" cy="294" r="9"  fill="#228a5e"/><circle cx="90" cy="294" r="6.5" fill="#d4a843"/><circle cx="90" cy="294" r="4"  fill="#0a2818"/><circle cx="90" cy="294" r="1.8" fill="#e8c97a"/>
<circle cx="28" cy="254" r="9"  fill="#1a7a52"/><circle cx="28" cy="254" r="6"  fill="#e8c97a"/><circle cx="28" cy="254" r="3.5" fill="#0a2818"/>
<circle cx="22" cy="244" r="8"  fill="#228a5e"/><circle cx="22" cy="244" r="5.5" fill="#d4a843"/><circle cx="22" cy="244" r="3"  fill="#0a2818"/>
<line x1="72"  y1="550" x2="58"  y2="574" stroke="#0a4a30" stroke-width="2.8"/>
<line x1="58"  y1="574" x2="44"  y2="584" stroke="#0a4a30" stroke-width="2"/>
<line x1="58"  y1="574" x2="58"  y2="586" stroke="#0a4a30" stroke-width="2"/>
<line x1="58"  y1="574" x2="72"  y2="584" stroke="#0a4a30" stroke-width="2"/>
<line x1="106" y1="553" x2="108" y2="577" stroke="#0a4a30" stroke-width="2.8"/>
<line x1="108" y1="577" x2="95"  y2="588" stroke="#0a4a30" stroke-width="2"/>
<line x1="108" y1="577" x2="108" y2="590" stroke="#0a4a30" stroke-width="2"/>
<line x1="108" y1="577" x2="121" y2="588" stroke="#0a4a30" stroke-width="2"/>
<ellipse cx="612" cy="490" rx="50" ry="65" fill="#1a7a52"/>
<ellipse cx="612" cy="478" rx="40" ry="53" fill="#228a5e"/>
<path d="M612 428 Q619 403 615 376 Q612 360 606 350" stroke="#1a7a52" stroke-width="17" fill="none" stroke-linecap="round"/>
<path d="M612 428 Q619 403 615 376 Q612 360 606 350" stroke="#2a9a6a" stroke-width="10" fill="none" stroke-linecap="round"/>
<circle cx="604" cy="338" r="22" fill="#1a7a52"/>
<circle cx="604" cy="338" r="15" fill="#2a9a6a"/>
<circle cx="597" cy="333" r="5"  fill="#082818"/>
<circle cx="595" cy="331" r="2"  fill="#d4a843"/>
<line x1="611" y1="316" x2="620" y2="294" stroke="#2a9a6a" stroke-width="2"/>
<circle cx="620" cy="290" r="4.5" fill="#d4a843"/>
<line x1="604" y1="314" x2="606" y2="290" stroke="#2a9a6a" stroke-width="2"/>
<circle cx="606" cy="286" r="4.5" fill="#d4a843"/>
<line x1="597" y1="316" x2="590" y2="294" stroke="#2a9a6a" stroke-width="2"/>
<circle cx="590" cy="290" r="4.5" fill="#d4a843"/>
<path d="M588 336 L572 339 L588 342 Z" fill="#c49030"/>
<path d="M650 516 Q684 435 674 342 Q669 300 658 270" stroke="#0d5a38" stroke-width="3.8" fill="none" stroke-linecap="round"/>
<path d="M638 530 Q676 446 660 353 Q654 310 640 278" stroke="#1a7a52" stroke-width="3.2" fill="none" stroke-linecap="round"/>
<path d="M624 542 Q652 460 634 368 Q626 325 610 294" stroke="#0d5a38" stroke-width="2.8" fill="none" stroke-linecap="round"/>
<path d="M660 494 Q692 416 686 324 Q682 282 672 254" stroke="#1a7a52" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<path d="M672 468 Q696 394 690 306 Q686 268 678 244" stroke="#0a4a30" stroke-width="2.2" fill="none" stroke-linecap="round"/>
<circle cx="658" cy="270" r="11" fill="#1a7a52"/><circle cx="658" cy="270" r="8"   fill="#d4a843"/><circle cx="658" cy="270" r="5"   fill="#0a2818"/><circle cx="658" cy="270" r="2.2" fill="#e8c97a"/>
<circle cx="640" cy="278" r="10" fill="#1a7a52"/><circle cx="640" cy="278" r="7"   fill="#d4a843"/><circle cx="640" cy="278" r="4.5" fill="#0a2818"/><circle cx="640" cy="278" r="2"   fill="#e8c97a"/>
<circle cx="610" cy="294" r="9"  fill="#228a5e"/><circle cx="610" cy="294" r="6.5" fill="#d4a843"/><circle cx="610" cy="294" r="4"   fill="#0a2818"/><circle cx="610" cy="294" r="1.8" fill="#e8c97a"/>
<circle cx="672" cy="254" r="9"  fill="#1a7a52"/><circle cx="672" cy="254" r="6"   fill="#e8c97a"/><circle cx="672" cy="254" r="3.5" fill="#0a2818"/>
<circle cx="678" cy="244" r="8"  fill="#228a5e"/><circle cx="678" cy="244" r="5.5" fill="#d4a843"/><circle cx="678" cy="244" r="3"   fill="#0a2818"/>
<line x1="628" y1="550" x2="642" y2="574" stroke="#0a4a30" stroke-width="2.8"/>
<line x1="642" y1="574" x2="656" y2="584" stroke="#0a4a30" stroke-width="2"/>
<line x1="642" y1="574" x2="642" y2="586" stroke="#0a4a30" stroke-width="2"/>
<line x1="642" y1="574" x2="628" y2="584" stroke="#0a4a30" stroke-width="2"/>
<line x1="594" y1="553" x2="592" y2="577" stroke="#0a4a30" stroke-width="2.8"/>
<line x1="592" y1="577" x2="605" y2="588" stroke="#0a4a30" stroke-width="2"/>
<line x1="592" y1="577" x2="592" y2="590" stroke="#0a4a30" stroke-width="2"/>
<line x1="592" y1="577" x2="579" y2="588" stroke="#0a4a30" stroke-width="2"/>
<text x="350" y="198" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="11" fill="#7a5a10" letter-spacing="3">|| Shri Ganeshaya Namah ||</text>
<text x="350" y="220" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="10" fill="#8a6a20">The families joyfully invite you to celebrate</text>
<line x1="215" y1="230" x2="485" y2="230" stroke="#c9a96e" stroke-width="0.8"/>
<polygon points="350,226 356,230 350,234 344,230" fill="#c9a96e"/>
<text x="350" y="268" text-anchor="middle" font-family="\'Great Vibes\',cursive,Georgia,serif" font-size="40" fill="#7a1030">{{ details.bride_name }}</text>
<line x1="215" y1="278" x2="485" y2="278" stroke="#c9a96e" stroke-width="0.5"/>
<text x="350" y="308" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="16" fill="#c9a96e" letter-spacing="5">~ weds ~</text>
<text x="350" y="348" text-anchor="middle" font-family="\'Great Vibes\',cursive,Georgia,serif" font-size="40" fill="#1a3a70">{{ details.groom_name }}</text>
<line x1="215" y1="358" x2="485" y2="358" stroke="#c9a96e" stroke-width="0.5"/>
<polygon points="350,354 356,358 350,362 344,358" fill="#c9a96e"/>
{% set fd = details.wedding_date.split(\'-\') %}
{% set months = [\'\',\'January\',\'February\',\'March\',\'April\',\'May\',\'June\',\'July\',\'August\',\'September\',\'October\',\'November\',\'December\'] %}
{% if fd|length == 3 %}
<text x="350" y="386" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="14" fill="#3a2000" font-weight="bold">{{ months[fd[1]|int] }} {{ fd[2] }}, {{ fd[0] }}</text>
{% else %}
<text x="350" y="386" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="14" fill="#3a2000">{{ details.wedding_date }}</text>
{% endif %}
{% if details.ceremony_time %}
<text x="350" y="406" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="13" fill="#5a3a10">{{ details.ceremony_time }}</text>
{% endif %}
<line x1="215" y1="420" x2="485" y2="420" stroke="#c9a96e" stroke-width="0.5"/>
<text x="350" y="440" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="9" fill="#8a6a20" letter-spacing="3">VENUE</text>
<text x="350" y="462" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="16" fill="#2a1800" font-weight="bold">{{ details.venue_name }}</text>
<text x="350" y="480" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="12" fill="#5a3a10">{{ details.venue_city }}</text>
<line x1="215" y1="493" x2="485" y2="493" stroke="#c9a96e" stroke-width="0.5"/>
<polygon points="350,489 356,493 350,497 344,493" fill="#c9a96e"/>
{% set words = invitation_text.split() %}
{% set l1 = words[:8]   | join(\' \') %}
{% set l2 = words[8:16]  | join(\' \') %}
{% set l3 = words[16:24] | join(\' \') %}
{% set l4 = words[24:32] | join(\' \') %}
{% set l5 = words[32:40] | join(\' \') %}
<text x="350" y="516" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="11.5" fill="#4a3010" font-style="italic">{{ l1 }}</text>
{% if l2 %}<text x="350" y="533" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="11.5" fill="#4a3010" font-style="italic">{{ l2 }}</text>{% endif %}
{% if l3 %}<text x="350" y="550" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="11.5" fill="#4a3010" font-style="italic">{{ l3 }}</text>{% endif %}
{% if l4 %}<text x="350" y="567" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="11.5" fill="#4a3010" font-style="italic">{{ l4 }}</text>{% endif %}
{% if l5 %}<text x="350" y="584" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="11.5" fill="#4a3010" font-style="italic">{{ l5 }}</text>{% endif %}
<line x1="215" y1="600" x2="485" y2="600" stroke="#c9a96e" stroke-width="0.5"/>
<ellipse cx="350" cy="618" rx="95" ry="13" fill="#1a5c3a" opacity="0.9"/>
<text x="350" y="623" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="11" fill="#e8c97a" letter-spacing="1">We joyfully await your presence</text>
{% if details.ceremonies %}
<text x="350" y="648" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="10" fill="#8a6a20" font-style="italic">* Celebrations schedule on next page</text>
{% endif %}
<rect x="8" y="820" width="684" height="3" fill="#d4a843"/>
<rect x="8" y="823" width="684" height="49" fill="#1a5c3a"/>
<path d="M30 836 Q80 822 130 836 Q180 850 230 835 Q280 820 350 826 Q420 820 470 835 Q520 850 570 836 Q620 822 670 836" stroke="#2a8a50" stroke-width="1.4" fill="none"/>
{% for lx in [75,160,245,350,455,540,625] %}
<ellipse cx="{{ lx }}" cy="838" rx="6" ry="10" fill="#e8c97a"/>
<ellipse cx="{{ lx-6 }}" cy="843" rx="4.5" ry="7.5" fill="#d4a843"/>
<ellipse cx="{{ lx+6 }}" cy="843" rx="4.5" ry="7.5" fill="#d4a843"/>
<ellipse cx="{{ lx }}" cy="854" rx="8" ry="3.5" fill="#0f4a2a"/>
{% endfor %}
<text x="350" y="866" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="9" fill="#e8c97a" letter-spacing="3">~ Peacock Royal · Teal &amp; Gold ~</text>
</svg>
</div>

{% if details.ceremonies %}
<p class="page-label">Page 2 of 2 — Celebrations Schedule</p>
<div class="card-container">
{% set months2 = [\'\',\'January\',\'February\',\'March\',\'April\',\'May\',\'June\',\'July\',\'August\',\'September\',\'October\',\'November\',\'December\'] %}
{% set num_cer = details.ceremonies | length %}
{% set p2h = 880 %}
<svg class="card-svg" viewBox="0 0 700 {{ p2h }}" xmlns="http://www.w3.org/2000/svg">
<defs>
  <pattern id="bgp2" patternUnits="userSpaceOnUse" width="28" height="28">
    <rect width="28" height="28" fill="#0a3828"/>
    <circle cx="14" cy="14" r="1.1" fill="#1a6a48" opacity="0.45"/>
    <circle cx="0" cy="0" r="0.7" fill="#1a6a48" opacity="0.25"/>
    <circle cx="28" cy="28" r="0.7" fill="#1a6a48" opacity="0.25"/>
  </pattern>
</defs>
<rect width="700" height="{{ p2h }}" fill="url(#bgp2)"/>
<rect x="8" y="8" width="684" height="{{ p2h-16 }}" rx="3" fill="none" stroke="#d4a843" stroke-width="2.5"/>
<rect x="14" y="14" width="672" height="{{ p2h-28 }}" rx="2" fill="none" stroke="#e8c97a" stroke-width="0.8"/>
<circle cx="36"  cy="36"           r="9" fill="#d4a843"/><circle cx="36"  cy="36"           r="6" fill="#0a3828"/><circle cx="36"  cy="36"           r="3" fill="#e8c97a"/>
<circle cx="664" cy="36"           r="9" fill="#d4a843"/><circle cx="664" cy="36"           r="6" fill="#0a3828"/><circle cx="664" cy="36"           r="3" fill="#e8c97a"/>
<circle cx="36"  cy="{{ p2h-36 }}" r="9" fill="#d4a843"/><circle cx="36"  cy="{{ p2h-36 }}" r="6" fill="#0a3828"/><circle cx="36"  cy="{{ p2h-36 }}" r="3" fill="#e8c97a"/>
<circle cx="664" cy="{{ p2h-36 }}" r="9" fill="#d4a843"/><circle cx="664" cy="{{ p2h-36 }}" r="6" fill="#0a3828"/><circle cx="664" cy="{{ p2h-36 }}" r="3" fill="#e8c97a"/>
<rect x="8" y="8" width="684" height="56" fill="#1a5c3a"/>
<rect x="8" y="61" width="684" height="3" fill="#d4a843"/>
{% for lx in [75,160,245,350,455,540,625] %}
<ellipse cx="{{ lx }}" cy="34" rx="7" ry="10" fill="#e8c97a"/>
<ellipse cx="{{ lx-7 }}" cy="39" rx="5" ry="8" fill="#d4a843"/>
<ellipse cx="{{ lx+7 }}" cy="39" rx="5" ry="8" fill="#d4a843"/>
<ellipse cx="{{ lx }}" cy="50" rx="9" ry="4" fill="#0f4a2a"/>
{% endfor %}
<text x="350" y="92" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="12" fill="#d4a843" letter-spacing="4">CELEBRATIONS SCHEDULE</text>
<text x="350" y="120" text-anchor="middle" font-family="\'Great Vibes\',cursive,Georgia,serif" font-size="34" fill="#e8c97a">{{ details.bride_name }} &amp; {{ details.groom_name }}</text>
<line x1="100" y1="134" x2="600" y2="134" stroke="#d4a843" stroke-width="0.8"/>
<polygon points="350,130 357,134 350,138 343,134" fill="#d4a843"/>
<rect x="50" y="150" width="600" height="90" rx="8" fill="#fdf6e3" stroke="#d4a843" stroke-width="2"/>
<rect x="50" y="150" width="10" height="90" rx="4" fill="#d4a843"/>
<circle cx="50" cy="150" r="6" fill="#d4a843"/>
<circle cx="650" cy="150" r="6" fill="#d4a843"/>
<circle cx="50" cy="240" r="6" fill="#d4a843"/>
<circle cx="650" cy="240" r="6" fill="#d4a843"/>
<text x="80" y="178" font-family="\'Great Vibes\',cursive,Georgia,serif" font-size="22" fill="#7a1030">&#128149; Wedding Ceremony</text>
{% set fd2 = details.wedding_date.split(\'-\') %}
{% if fd2|length == 3 %}
<text x="80" y="202" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="13" fill="#3a2000">&#128197; {{ months2[fd2[1]|int] }} {{ fd2[2] }}, {{ fd2[0] }}{% if details.ceremony_time %}   &#8987; {{ details.ceremony_time }}{% endif %}</text>
{% endif %}
<text x="80" y="224" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="12" fill="#6a4010">&#127963; {{ details.venue_name }}, {{ details.venue_city }}</text>
{% set all_cers = details.ceremonies.items() | list %}
{% for key, cer in all_cers %}
  {% if loop.index0 % 2 == 0 %}
    {% set cx3 = 50 %}
    {% set cy3 = 260 + (loop.index0 // 2) * 150 %}
    {% set cw3 = 295 %}
  {% else %}
    {% set cx3 = 355 %}
    {% set cy3 = 320 + ((loop.index0 - 1) // 2) * 150 %}
    {% set cw3 = 295 %}
  {% endif %}
  {% if key == \'haldi\' %}
    {% set accent = \'#e8a020\' %}
    {% set icon = \'&#127774;\' %}
  {% elif key == \'mehendi\' %}
    {% set accent = \'#2a8a40\' %}
    {% set icon = \'&#127807;\' %}
  {% else %}
    {% set accent = \'#9a2060\' %}
    {% set icon = \'&#127870;\' %}
  {% endif %}
<rect x="{{ cx3 }}" y="{{ cy3 }}" width="{{ cw3 }}" height="120" rx="10" fill="#fdf6e3" stroke="{{ accent }}" stroke-width="1.5"/>
<rect x="{{ cx3 }}" y="{{ cy3 }}" width="8" height="120" rx="4" fill="{{ accent }}"/>
<circle cx="{{ cx3 }}" cy="{{ cy3 }}" r="5" fill="{{ accent }}"/>
<circle cx="{{ cx3 + cw3 }}" cy="{{ cy3 }}" r="5" fill="{{ accent }}"/>
<circle cx="{{ cx3 }}" cy="{{ cy3 + 120 }}" r="5" fill="{{ accent }}"/>
<circle cx="{{ cx3 + cw3 }}" cy="{{ cy3 + 120 }}" r="5" fill="{{ accent }}"/>
<text x="{{ cx3 + 22 }}" y="{{ cy3 + 28 }}" font-family="\'Great Vibes\',cursive,Georgia,serif" font-size="20" fill="{{ accent }}">{{ icon }} {{ cer.label if cer.label else key | capitalize }}</text>
{% if cer.date %}
  {% set cfd = cer.date.split(\'-\') %}
  {% if cfd|length == 3 %}
<text x="{{ cx3 + 22 }}" y="{{ cy3 + 52 }}" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="12" fill="#3a2000">&#128197; {{ months2[cfd[1]|int] }} {{ cfd[2] }}, {{ cfd[0] }}</text>
  {% else %}
<text x="{{ cx3 + 22 }}" y="{{ cy3 + 52 }}" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="12" fill="#3a2000">&#128197; {{ cer.date }}</text>
  {% endif %}
{% endif %}
{% if cer.time %}
<text x="{{ cx3 + 22 }}" y="{{ cy3 + 72 }}" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="12" fill="#5a3a10">&#8987; {{ cer.time }}</text>
{% endif %}
{% if cer.venue %}
<text x="{{ cx3 + 22 }}" y="{{ cy3 + 92 }}" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="11" fill="#7a5a20">&#127963; {{ cer.venue }}</text>
{% endif %}
{% endfor %}
{% set pt_y = 260 + ((num_cer + 1) // 2) * 150 + 20 %}
{% if details.special_msg %}
<rect x="50" y="{{ pt_y }}" width="600" height="80" rx="30" fill="#1a5c3a" stroke="#d4a843" stroke-width="1.5"/>
<text x="350" y="{{ pt_y + 24 }}" text-anchor="middle" font-family="\'Montserrat\',sans-serif" font-size="8" fill="#e8c97a" letter-spacing="3">PERSONAL MESSAGE</text>
<text x="350" y="{{ pt_y + 48 }}" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="12" fill="#fdf6e3" font-style="italic">{{ details.special_msg[:80] }}</text>
{% else %}
<rect x="150" y="{{ pt_y }}" width="400" height="50" rx="25" fill="#1a5c3a" stroke="#d4a843" stroke-width="1"/>
<text x="350" y="{{ pt_y + 20 }}" text-anchor="middle" font-family="\'Cormorant Garamond\',Georgia,serif" font-size="11" fill="#e8c97a" letter-spacing="1">Your presence is our greatest blessing</text>
<text x="350" y="{{ pt_y + 38 }}" text-anchor="middle" font-family="\'Montserrat\',sans-serif" font-size="8" fill="#d4a843" letter-spacing="2">~ WE JOYFULLY AWAIT YOU ~</text>
{% endif %}
<rect x="8" y="{{ p2h - 48 }}" width="684" height="3" fill="#d4a843"/>
<rect x="8" y="{{ p2h - 45 }}" width="684" height="40" fill="#1a5c3a"/>
{% for lx in [75,160,245,350,455,540,625] %}
<ellipse cx="{{ lx }}" cy="{{ p2h - 28 }}" rx="6" ry="9" fill="#e8c97a"/>
<ellipse cx="{{ lx-6 }}" cy="{{ p2h - 23 }}" rx="4.5" ry="7" fill="#d4a843"/>
<ellipse cx="{{ lx+6 }}" cy="{{ p2h - 23 }}" rx="4.5" ry="7" fill="#d4a843"/>
{% endfor %}
</svg>
</div>
{% endif %}

<script>
function copyLink() {
    const el = document.getElementById(\'slink\');
    el.select();
    document.execCommand(\'copy\');
    const btn = document.getElementById(\'copybtn\');
    btn.textContent = \'Copied!\';
    setTimeout(() => btn.textContent = \'&#128203; Copy\', 2000);
}
</script>
</body>
</html>'''

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done! File written cleanly.")