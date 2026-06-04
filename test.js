const pptxgen = require("pptxgenjs");
const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.title  = "AI Wedding Invitation Generator";

// ── PALETTE ────────────────────────────────────────────
const DARK   = "1a0a08";
const GOLD   = "c9a96e";
const GOLD2  = "e8c97a";
const CREAM  = "fdf6e3";
const MID    = "2a1510";
const WHITE  = "FFFFFF";
const TEAL   = "1a5c3a";
const RED    = "8b1a4a";
const GRAY   = "9e8e85";

const makeShadow = () => ({ type:"outer", blur:8, offset:3, angle:135, color:"000000", opacity:0.25 });

// ── HELPERS ────────────────────────────────────────────
function darkSlide(s) {
  s.background = { color: DARK };
}

function goldBar(s, y=0, h=0.06) {
  s.addShape(pres.shapes.RECTANGLE, { x:0, y, w:10, h, fill:{ color:GOLD }, line:{ color:GOLD } });
}

function sectionTag(s, label, x=0.5, y=0.28) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x, y, w:1.6, h:0.28, fill:{ color:GOLD }, rectRadius:0.06,
    line:{ color:GOLD }
  });
  s.addText(label.toUpperCase(), {
    x, y, w:1.6, h:0.28, fontSize:8, bold:true,
    color:DARK, align:"center", valign:"middle", margin:0
  });
}

function card(s, x, y, w, h, fillColor=MID, radius=0.12) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x, y, w, h, fill:{ color:fillColor },
    line:{ color:GOLD, width:0.5 },
    rectRadius:radius, shadow: makeShadow()
  });
}

function goldDivider(s, y, xStart=0.5, xEnd=9.5) {
  s.addShape(pres.shapes.LINE, {
    x:xStart, y, w:xEnd-xStart, h:0,
    line:{ color:GOLD, width:0.4 }
  });
}

// ══════════════════════════════════════════════════════
// SLIDE 1 — TITLE
// ══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  darkSlide(s);

  // left gold accent bar
  s.addShape(pres.shapes.RECTANGLE, {
    x:0, y:0, w:0.06, h:5.625, fill:{ color:GOLD }, line:{ color:GOLD }
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x:9.94, y:0, w:0.06, h:5.625, fill:{ color:GOLD }, line:{ color:GOLD }
  });
  goldBar(s, 0, 0.06);
  goldBar(s, 5.565, 0.06);

  // Om symbol circle
  s.addShape(pres.shapes.OVAL, {
    x:4.6, y:0.55, w:0.8, h:0.8,
    fill:{ color:GOLD }, line:{ color:GOLD2 }
  });
  s.addText("ॐ", {
    x:4.6, y:0.55, w:0.8, h:0.8,
    fontSize:22, color:DARK, align:"center", valign:"middle", margin:0
  });

  // Main title
  s.addText("AI Wedding Invitation", {
    x:0.5, y:1.55, w:9, h:1.0,
    fontSize:54, bold:true, color:GOLD2,
    align:"center", fontFace:"Georgia"
  });
  s.addText("Generator", {
    x:0.5, y:2.5, w:9, h:0.75,
    fontSize:48, bold:false, color:GOLD,
    align:"center", fontFace:"Georgia", italic:true
  });

  goldDivider(s, 3.38, 2.5, 7.5);

  s.addText("Full-Stack AI Project  ·  Flask + Groq LLM + SVG Card Engine", {
    x:0.5, y:3.5, w:9, h:0.4,
    fontSize:13, color:GOLD, align:"center",
    charSpacing:2, fontFace:"Calibri"
  });

  s.addText("Built from scratch — Backend · Frontend · AI · PDF · Deployment", {
    x:0.5, y:4.0, w:9, h:0.35,
    fontSize:11, color:GRAY, align:"center",
    fontFace:"Calibri", italic:true
  });

  // decorative dots
  for (let i=0; i<5; i++) {
    s.addShape(pres.shapes.OVAL, {
      x: 4.0 + i*0.45, y:4.55, w:0.12, h:0.12,
      fill:{ color: i===2 ? GOLD : "4a3020" }, line:{ color:GOLD }
    });
  }
}

// ══════════════════════════════════════════════════════
// SLIDE 2 — PROJECT OVERVIEW
// ══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  darkSlide(s);
  goldBar(s, 0, 0.05);
  goldBar(s, 5.575, 0.05);

  sectionTag(s, "Overview");
  s.addText("What We Built", {
    x:0.5, y:0.55, w:9, h:0.6,
    fontSize:32, bold:true, color:GOLD2, fontFace:"Georgia"
  });

  goldDivider(s, 1.22, 0.5, 9.5);

  s.addText(
    "A complete production-level web application where users enter their wedding details and receive a professionally designed, AI-written invitation — instantly.",
    {
      x:0.5, y:1.3, w:9, h:0.7,
      fontSize:13, color:CREAM, fontFace:"Calibri",
      align:"left", italic:true
    }
  );

  // 4 feature cards
  const features = [
    { icon:"🤖", title:"AI Text Generation",  desc:"Groq LLM (LLaMA 3.3 70B) writes unique invitation text based on style, tone and details" },
    { icon:"🎨", title:"6 Illustrated Themes", desc:"Hand-crafted SVG card designs — Peacock, Purple Maharaja, Sindoor Red, Midnight Lotus, Rose Mehndi, Forest Sage" },
    { icon:"📄", title:"2-Page PDF Card",      desc:"Page 1: Main invitation with AI text. Page 2: Ceremonies schedule in staggered grid layout" },
    { icon:"🔗", title:"Shareable Links",      desc:"Every generated invitation gets a unique URL stored in SQLite — share on WhatsApp or Email instantly" },
  ];

  features.forEach((f, i) => {
    const col = i % 2, row = Math.floor(i / 2);
    const x = 0.4 + col * 4.85, y = 2.15 + row * 1.55;
    card(s, x, y, 4.65, 1.35);
    s.addText(f.icon + "  " + f.title, {
      x: x+0.2, y: y+0.12, w:4.25, h:0.4,
      fontSize:13, bold:true, color:GOLD2, fontFace:"Calibri"
    });
    s.addText(f.desc, {
      x: x+0.2, y: y+0.52, w:4.25, h:0.72,
      fontSize:10.5, color:CREAM, fontFace:"Calibri", wrap:true
    });
  });
}

// ══════════════════════════════════════════════════════
// SLIDE 3 — TECH STACK
// ══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  darkSlide(s);
  goldBar(s, 0, 0.05);
  goldBar(s, 5.575, 0.05);

  sectionTag(s, "Tech Stack");
  s.addText("Technology Stack", {
    x:0.5, y:0.55, w:9, h:0.6,
    fontSize:32, bold:true, color:GOLD2, fontFace:"Georgia"
  });
  goldDivider(s, 1.22, 0.5, 9.5);

  const stack = [
    { layer:"Backend",       color:"1a5c3a", items:["Python 3.13", "Flask 3.x", "Flask-SQLAlchemy", "Gunicorn (production)"] },
    { layer:"AI / LLM",      color:"4a0080", items:["Groq API (free)", "LLaMA 3.3 70B Versatile", "Prompt Engineering", "3 writing styles"] },
    { layer:"Frontend",      color:"8a0000", items:["HTML5 + CSS3", "Jinja2 Templates", "Vanilla JavaScript", "Google Fonts (Great Vibes, Cormorant)"] },
    { layer:"Card Engine",   color:"0a3828", items:["Pure SVG illustration", "6 hand-crafted themes", "Dynamic Jinja injection", "Print-ready 2-page layout"] },
    { layer:"Database",      color:"3a2000", items:["SQLite (local)", "Unique share IDs (UUID)", "Session storage", "Invitation history"] },
    { layer:"Deployment",    color:"204820", items:["Render.com (free tier)", "GitHub CI/CD", "Environment variables", ".env secret management"] },
  ];

  stack.forEach((st, i) => {
    const col = i % 3, row = Math.floor(i / 3);
    const x = 0.35 + col * 3.12, y = 1.38 + row * 1.98;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x, y, w:2.98, h:1.85,
      fill:{ color:st.color }, line:{ color:GOLD, width:0.5 }, rectRadius:0.1,
      shadow: makeShadow()
    });
    s.addText(st.layer.toUpperCase(), {
      x: x+0.15, y: y+0.12, w:2.68, h:0.3,
      fontSize:10, bold:true, color:GOLD2, fontFace:"Calibri", charSpacing:1
    });
    s.addShape(pres.shapes.LINE, {
      x: x+0.15, y: y+0.44, w:2.68, h:0,
      line:{ color:GOLD, width:0.3 }
    });
    st.items.forEach((item, j) => {
      s.addText("▸  " + item, {
        x: x+0.15, y: y+0.52 + j*0.29, w:2.68, h:0.28,
        fontSize:9.5, color:CREAM, fontFace:"Calibri"
      });
    });
  });
}

// ══════════════════════════════════════════════════════
// SLIDE 4 — ARCHITECTURE / HOW IT WORKS
// ══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  darkSlide(s);
  goldBar(s, 0, 0.05);
  goldBar(s, 5.575, 0.05);

  sectionTag(s, "Architecture");
  s.addText("How It Works", {
    x:0.5, y:0.55, w:9, h:0.6,
    fontSize:32, bold:true, color:GOLD2, fontFace:"Georgia"
  });
  goldDivider(s, 1.22, 0.5, 9.5);

  // Flow steps
  const steps = [
    { n:"1", label:"User fills form",      sub:"Names, date, venue,\nceremonies, theme" },
    { n:"2", label:"Flask receives POST",  sub:"Validates input\nBuilds prompt" },
    { n:"3", label:"Groq API called",      sub:"LLaMA 3.3 generates\npersonalized text" },
    { n:"4", label:"SVG card rendered",    sub:"Jinja injects data\ninto SVG template" },
    { n:"5", label:"Saved + shared",       sub:"UUID link stored\nin SQLite DB" },
  ];

  steps.forEach((st, i) => {
    const x = 0.3 + i * 1.88;

    // number circle
    s.addShape(pres.shapes.OVAL, {
      x: x+0.54, y:1.42, w:0.55, h:0.55,
      fill:{ color:GOLD }, line:{ color:GOLD2 }
    });
    s.addText(st.n, {
      x: x+0.54, y:1.42, w:0.55, h:0.55,
      fontSize:14, bold:true, color:DARK,
      align:"center", valign:"middle", margin:0
    });

    // step box
    card(s, x, 2.05, 1.65, 2.5, MID);
    s.addText(st.label, {
      x: x+0.1, y:2.15, w:1.45, h:0.6,
      fontSize:10.5, bold:true, color:GOLD2,
      fontFace:"Calibri", align:"center", wrap:true
    });
    s.addText(st.sub, {
      x: x+0.1, y:2.82, w:1.45, h:0.7,
      fontSize:9, color:CREAM,
      fontFace:"Calibri", align:"center", wrap:true
    });

    // arrow between steps
    if (i < steps.length - 1) {
      s.addShape(pres.shapes.LINE, {
        x: x+1.68, y:1.695, w:0.2, h:0,
        line:{ color:GOLD, width:1.5 }
      });
    }
  });

  goldDivider(s, 4.68, 0.5, 9.5);

  // Bottom note
  s.addText("Each invitation gets a unique shareable URL  ·  Anyone with the link sees the full illustrated card", {
    x:0.5, y:4.78, w:9, h:0.35,
    fontSize:10.5, color:GOLD, align:"center",
    fontFace:"Calibri", italic:true
  });

  // PDF note
  card(s, 0.4, 5.05, 9.2, 0.42, "1a3020");
  s.addText("📄  PDF Download: Browser print API renders exact card colors → user clicks once → styled PDF saved", {
    x:0.6, y:5.1, w:8.8, h:0.3,
    fontSize:10, color:CREAM, fontFace:"Calibri"
  });
}

// ══════════════════════════════════════════════════════
// SLIDE 5 — FEATURES DEEP DIVE
// ══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  darkSlide(s);
  goldBar(s, 0, 0.05);
  goldBar(s, 5.575, 0.05);

  sectionTag(s, "Features");
  s.addText("Core Features in Detail", {
    x:0.5, y:0.55, w:9, h:0.6,
    fontSize:32, bold:true, color:GOLD2, fontFace:"Georgia"
  });
  goldDivider(s, 1.22, 0.5, 9.5);

  const features = [
    {
      title:"🤖  AI Prompt Engineering",
      points:[
        "3 styles: Traditional Indian / Modern / Casual",
        "100-word max constraint for card fit",
        "Style-specific vocabulary in system prompt",
        "Groq free tier — no credit card needed",
      ]
    },
    {
      title:"🎨  SVG Card Engine",
      points:[
        "6 full illustrated SVG themes from scratch",
        "Peacock, Elephant, Lotus, Rose, Sage, Purple",
        "Dynamic Jinja2 variable injection into SVG",
        "2-page: Main card + Ceremonies grid",
      ]
    },
    {
      title:"📅  Indian Ceremonies System",
      points:[
        "Toggle on/off: Haldi, Mehendi, Reception",
        "Each has separate date, time, venue fields",
        "Staggered grid layout on page 2",
        "Personal message section at bottom",
      ]
    },
    {
      title:"🔗  Share & Export",
      points:[
        "UUID-based shareable links per invitation",
        "WhatsApp share with pre-filled text + link",
        "Email share with subject + body pre-filled",
        "Copy-to-clipboard button for instant sharing",
      ]
    },
  ];

  features.forEach((f, i) => {
    const col = i % 2, row = Math.floor(i / 2);
    const x = 0.35 + col * 4.85, y = 1.35 + row * 1.95;
    card(s, x, y, 4.65, 1.82, MID);
    s.addText(f.title, {
      x: x+0.18, y: y+0.12, w:4.3, h:0.38,
      fontSize:12, bold:true, color:GOLD2, fontFace:"Calibri"
    });
    s.addShape(pres.shapes.LINE, {
      x: x+0.18, y: y+0.52, w:4.3, h:0,
      line:{ color:GOLD, width:0.3 }
    });
    f.points.forEach((p, j) => {
      s.addText([
        { text:"◆  ", options:{ color:GOLD, bold:true } },
        { text:p,    options:{ color:CREAM } }
      ], {
        x: x+0.18, y: y+0.6 + j*0.28, w:4.3, h:0.27,
        fontSize:10, fontFace:"Calibri"
      });
    });
  });
}

// ══════════════════════════════════════════════════════
// SLIDE 6 — CARD DESIGNS SHOWCASE
// ══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  darkSlide(s);
  goldBar(s, 0, 0.05);
  goldBar(s, 5.575, 0.05);

  sectionTag(s, "Card Designs");
  s.addText("6 Illustrated Card Themes", {
    x:0.5, y:0.55, w:9, h:0.6,
    fontSize:32, bold:true, color:GOLD2, fontFace:"Georgia"
  });
  goldDivider(s, 1.22, 0.5, 9.5);

  const designs = [
    { name:"Peacock Royal",    icon:"🦚", color:"0a3828", accent:"d4a843", sub:"Teal + Gold\nTwo peacocks, Mughal arch" },
    { name:"Purple Maharaja",  icon:"👑", color:"1a0035", accent:"d4a843", sub:"Purple + Marigold\nTwo elephants, marigold garland" },
    { name:"Sindoor Red",      icon:"❤️", color:"1a0000", accent:"e8500a", sub:"Deep Red + Saffron\nLotus flowers, temple arch" },
    { name:"Midnight Lotus",   icon:"✦",  color:"040820", accent:"6080c0", sub:"Navy + Silver\nNight-bloom lotus, star motifs" },
    { name:"Rose Mehndi",      icon:"🌹", color:"1a0810", accent:"e080a0", sub:"Rose + Copper\nMehndi vine rose buds" },
    { name:"Forest Sage",      icon:"🌿", color:"081808", accent:"60a860", sub:"Sage Green + Ivory\nBotanical arrangement" },
  ];

  designs.forEach((d, i) => {
    const col = i % 3, row = Math.floor(i / 3);
    const x = 0.35 + col * 3.12, y = 1.35 + row * 1.95;

    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x, y, w:2.95, h:1.8,
      fill:{ color:d.color },
      line:{ color:d.accent, width:1.2 },
      rectRadius:0.1, shadow: makeShadow()
    });

    s.addText(d.icon + "  " + d.name, {
      x: x+0.15, y: y+0.15, w:2.65, h:0.45,
      fontSize:12, bold:true, color:"" + d.accent,
      fontFace:"Calibri"
    });
    s.addShape(pres.shapes.LINE, {
      x: x+0.15, y: y+0.62, w:2.65, h:0,
      line:{ color:d.accent, width:0.4 }
    });
    s.addText(d.sub, {
      x: x+0.15, y: y+0.72, w:2.65, h:0.95,
      fontSize:9.5, color:CREAM, fontFace:"Calibri", wrap:true
    });
  });
}

// ══════════════════════════════════════════════════════
// SLIDE 7 — DEVELOPMENT JOURNEY
// ══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  darkSlide(s);
  goldBar(s, 0, 0.05);
  goldBar(s, 5.575, 0.05);

  sectionTag(s, "Journey");
  s.addText("Development Journey", {
    x:0.5, y:0.55, w:9, h:0.6,
    fontSize:32, bold:true, color:GOLD2, fontFace:"Georgia"
  });
  goldDivider(s, 1.22, 0.5, 9.5);

  const timeline = [
    { phase:"Phase 1",  label:"Foundation",        color:"1a5c3a", items:["Flask server setup","Project folder structure","Virtual environment","Basic HTML form"] },
    { phase:"Phase 2",  label:"Form & Validation",  color:"4a3000", items:["Wedding details form","Server-side validation","Form CSS styling","Data flow testing"] },
    { phase:"Phase 3",  label:"AI Integration",     color:"4a0080", items:["OpenAI → Groq switch","Prompt engineering","3 writing styles","Error handling"] },
    { phase:"Phase 4",  label:"Card Design Engine", color:"8a0000", items:["SVG card architecture","6 illustrated themes","2-page layout","Dynamic Jinja injection"] },
    { phase:"Phase 5",  label:"Share & Export",     color:"0a3828", items:["UUID shareable links","SQLite database","WhatsApp/Email share","PDF download"] },
    { phase:"Phase 6",  label:"Polish & Deploy",    color:"204820", items:["Form redesign (dark theme)","Loading animations","Ceremonies system","Render.com deploy"] },
  ];

  timeline.forEach((t, i) => {
    const col = i % 3, row = Math.floor(i / 3);
    const x = 0.35 + col * 3.12, y = 1.38 + row * 1.98;

    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x, y, w:2.95, h:1.85,
      fill:{ color:t.color }, line:{ color:GOLD, width:0.5 },
      rectRadius:0.1, shadow: makeShadow()
    });

    s.addText(t.phase.toUpperCase(), {
      x: x+0.15, y: y+0.1, w:2.65, h:0.22,
      fontSize:7.5, color:GOLD, fontFace:"Calibri",
      charSpacing:2, bold:true
    });
    s.addText(t.label, {
      x: x+0.15, y: y+0.3, w:2.65, h:0.3,
      fontSize:12, bold:true, color:GOLD2, fontFace:"Calibri"
    });
    s.addShape(pres.shapes.LINE, {
      x: x+0.15, y: y+0.62, w:2.65, h:0,
      line:{ color:GOLD, width:0.3 }
    });
    t.items.forEach((item, j) => {
      s.addText("▸  " + item, {
        x: x+0.15, y: y+0.7 + j*0.27, w:2.65, h:0.26,
        fontSize:9.5, color:CREAM, fontFace:"Calibri"
      });
    });
  });
}

// ══════════════════════════════════════════════════════
// SLIDE 8 — CHALLENGES & SOLUTIONS
// ══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  darkSlide(s);
  goldBar(s, 0, 0.05);
  goldBar(s, 5.575, 0.05);

  sectionTag(s, "Problem Solving");
  s.addText("Challenges & How We Solved Them", {
    x:0.5, y:0.55, w:9, h:0.6,
    fontSize:30, bold:true, color:GOLD2, fontFace:"Georgia"
  });
  goldDivider(s, 1.22, 0.5, 9.5);

  const challenges = [
    {
      prob:"❌  OpenAI quota exceeded",
      sol:"✅  Switched to Groq API (free, faster, LLaMA 3.3 70B)",
    },
    {
      prob:"❌  Gemini API deprecated library",
      sol:"✅  Upgraded to new google-genai SDK, then moved to Groq",
    },
    {
      prob:"❌  SVG text overflowing arch panel",
      sol:"✅  Split invitation_text by words into 8-word lines with Jinja",
    },
    {
      prob:"❌  PDF losing colors (browser default B&W)",
      sol:"✅  print-color-adjust: exact + user enables background graphics once",
    },
    {
      prob:"❌  Jinja variable 'page2_height' undefined error",
      sol:"✅  Moved all {% set %} declarations outside of SVG tag scope",
    },
    {
      prob:"❌  Emoji HTML entities showing as code in SVG",
      sol:"✅  Used actual Unicode emoji characters instead of &#127774; entities",
    },
  ];

  challenges.forEach((c, i) => {
    const y = 1.38 + i * 0.67;
    card(s, 0.35, y, 9.3, 0.58, i % 2 === 0 ? MID : "1e0c0a");

    s.addText(c.prob, {
      x:0.55, y: y+0.06, w:4.3, h:0.22,
      fontSize:10, bold:true, color:"e05050", fontFace:"Calibri"
    });
    s.addText(c.sol, {
      x:4.95, y: y+0.06, w:4.5, h:0.22,
      fontSize:10, bold:true, color:"50c050", fontFace:"Calibri"
    });

    s.addShape(pres.shapes.LINE, {
      x:4.9, y: y+0.05, w:0, h:0.48,
      line:{ color:GOLD, width:0.5 }
    });
  });
}

// ══════════════════════════════════════════════════════
// SLIDE 9 — PROJECT STATS
// ══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  darkSlide(s);
  goldBar(s, 0, 0.05);
  goldBar(s, 5.575, 0.05);

  sectionTag(s, "Stats");
  s.addText("Project By The Numbers", {
    x:0.5, y:0.55, w:9, h:0.6,
    fontSize:32, bold:true, color:GOLD2, fontFace:"Georgia"
  });
  goldDivider(s, 1.22, 0.5, 9.5);

  const stats = [
    { n:"6",    label:"Card Themes",        sub:"All hand-crafted in SVG" },
    { n:"3",    label:"AI Writing Styles",  sub:"Traditional · Modern · Casual" },
    { n:"4",    label:"Ceremonies",         sub:"Haldi · Mehendi · Wedding · Reception" },
    { n:"2",    label:"Card Pages",         sub:"Main invitation + Ceremonies schedule" },
    { n:"100%", label:"Free to Run",        sub:"Groq free tier + Render free hosting" },
    { n:"∞",    label:"Shareable Links",    sub:"Every invitation gets a unique URL" },
  ];

  stats.forEach((st, i) => {
    const col = i % 3, row = Math.floor(i / 3);
    const x = 0.35 + col * 3.12, y = 1.38 + row * 1.92;

    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x, y, w:2.95, h:1.78,
      fill:{ color:MID }, line:{ color:GOLD, width:0.8 },
      rectRadius:0.12, shadow: makeShadow()
    });

    s.addText(st.n, {
      x: x+0.15, y: y+0.18, w:2.65, h:0.8,
      fontSize:52, bold:true, color:GOLD2,
      fontFace:"Georgia", align:"center"
    });
    s.addShape(pres.shapes.LINE, {
      x: x+0.5, y: y+0.98, w:1.95, h:0,
      line:{ color:GOLD, width:0.4 }
    });
    s.addText(st.label, {
      x: x+0.15, y: y+1.04, w:2.65, h:0.3,
      fontSize:10.5, bold:true, color:GOLD2,
      fontFace:"Calibri", align:"center"
    });
    s.addText(st.sub, {
      x: x+0.15, y: y+1.34, w:2.65, h:0.32,
      fontSize:8.5, color:GRAY,
      fontFace:"Calibri", align:"center", italic:true
    });
  });
}

// ══════════════════════════════════════════════════════
// SLIDE 10 — FUTURE ROADMAP
// ══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  darkSlide(s);
  goldBar(s, 0, 0.05);
  goldBar(s, 5.575, 0.05);

  sectionTag(s, "Roadmap");
  s.addText("What's Next", {
    x:0.5, y:0.55, w:9, h:0.6,
    fontSize:32, bold:true, color:GOLD2, fontFace:"Georgia"
  });
  goldDivider(s, 1.22, 0.5, 9.5);

  const road = [
    {
      phase:"🔜  Immediate",
      color:"1a5c3a",
      items:[
        "12 more card designs (Modern × 6, Casual × 6)",
        "Different visual styles per category",
        "Deploy to Render.com live URL",
      ]
    },
    {
      phase:"📅  Short Term",
      color:"4a3000",
      items:[
        "Multi-language support (Hindi + English)",
        "Custom family names on card",
        "RSVP count field",
      ]
    },
    {
      phase:"🚀  Long Term",
      color:"4a0080",
      items:[
        "React + Tailwind frontend rebuild",
        "Voice invitation (text-to-speech)",
        "AI image generation for card backgrounds",
      ]
    },
  ];

  road.forEach((r, i) => {
    const x = 0.35 + i * 3.12, y = 1.38;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x, y, w:2.95, h:3.8,
      fill:{ color:r.color }, line:{ color:GOLD, width:0.5 },
      rectRadius:0.12, shadow: makeShadow()
    });
    s.addText(r.phase, {
      x: x+0.15, y: y+0.15, w:2.65, h:0.38,
      fontSize:12, bold:true, color:GOLD2, fontFace:"Calibri"
    });
    s.addShape(pres.shapes.LINE, {
      x: x+0.15, y: y+0.55, w:2.65, h:0,
      line:{ color:GOLD, width:0.3 }
    });
    r.items.forEach((item, j) => {
      s.addText([
        { text:"◆  ", options:{ color:GOLD, bold:true } },
        { text:item,  options:{ color:CREAM } }
      ], {
        x: x+0.15, y: y+0.65 + j*0.55, w:2.65, h:0.48,
        fontSize:10.5, fontFace:"Calibri", wrap:true
      });
    });
  });

  // Current status bar
  goldDivider(s, 5.32, 0.5, 9.5);
  card(s, 0.4, 5.36, 9.2, 0.18, TEAL);
  s.addText("Current Status: MVP Complete & Fully Functional  ·  Ready for Deployment  ·  Active Development", {
    x:0.5, y:5.38, w:9, h:0.14,
    fontSize:9.5, color:GOLD2, align:"center",
    fontFace:"Calibri", bold:true
  });
}

// ══════════════════════════════════════════════════════
// SLIDE 11 — RESUME / HOW TO EXPLAIN
// ══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  darkSlide(s);
  goldBar(s, 0, 0.05);
  goldBar(s, 5.575, 0.05);

  sectionTag(s, "Resume");
  s.addText("How to Present This Project", {
    x:0.5, y:0.55, w:9, h:0.6,
    fontSize:32, bold:true, color:GOLD2, fontFace:"Georgia"
  });
  goldDivider(s, 1.22, 0.5, 9.5);

  // One-liner
  card(s, 0.4, 1.32, 9.2, 0.65, "1a3020");
  s.addText("One-Liner for Resume:", {
    x:0.6, y:1.38, w:2.5, h:0.22,
    fontSize:9, color:GOLD, fontFace:"Calibri", bold:true, charSpacing:1
  });
  s.addText(
    '"Built a full-stack AI web application that generates personalized Indian wedding invitations using Groq LLM, rendered as illustrated SVG cards with PDF export and shareable links."',
    {
      x:0.6, y:1.6, w:8.8, h:0.3,
      fontSize:10.5, color:CREAM, fontFace:"Calibri", italic:true
    }
  );

  // Talking points
  const points = [
    { q:"What problem does it solve?",    a:"Creating beautiful, personalized wedding invitations is expensive and time-consuming. This app does it in under 10 seconds for free." },
    { q:"What's the hardest part?",       a:"Building the SVG card engine — hand-crafting 6 illustrated Indian designs using pure SVG with dynamic data injection via Jinja2." },
    { q:"What AI concepts did you use?",  a:"Prompt engineering — structuring system + user prompts to control tone, length and style. Model selection for cost vs quality trade-off." },
    { q:"How is it production-ready?",    a:"Error handling, input validation, session management, database storage, environment variables, and deployment on Render.com." },
  ];

  points.forEach((p, i) => {
    const y = 2.1 + i * 0.8;
    card(s, 0.35, y, 9.3, 0.7, i % 2 === 0 ? MID : "1e0c0a");
    s.addText("Q: " + p.q, {
      x:0.55, y: y+0.06, w:9, h:0.24,
      fontSize:10, bold:true, color:GOLD2, fontFace:"Calibri"
    });
    s.addText("A: " + p.a, {
      x:0.55, y: y+0.32, w:9, h:0.3,
      fontSize:9.5, color:CREAM, fontFace:"Calibri", italic:true
    });
  });
}

// ══════════════════════════════════════════════════════
// SLIDE 12 — THANK YOU / CLOSING
// ══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  darkSlide(s);

  s.addShape(pres.shapes.RECTANGLE, {
    x:0, y:0, w:0.06, h:5.625, fill:{ color:GOLD }, line:{ color:GOLD }
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x:9.94, y:0, w:0.06, h:5.625, fill:{ color:GOLD }, line:{ color:GOLD }
  });
  goldBar(s, 0, 0.06);
  goldBar(s, 5.565, 0.06);

  s.addShape(pres.shapes.OVAL, {
    x:4.6, y:0.6, w:0.8, h:0.8,
    fill:{ color:GOLD }, line:{ color:GOLD2 }
  });
  s.addText("ॐ", {
    x:4.6, y:0.6, w:0.8, h:0.8,
    fontSize:22, color:DARK, align:"center", valign:"middle", margin:0
  });

  s.addText("Thank You", {
    x:0.5, y:1.6, w:9, h:0.9,
    fontSize:60, bold:true, color:GOLD2,
    align:"center", fontFace:"Georgia"
  });

  goldDivider(s, 2.68, 2.5, 7.5);

  s.addText("AI Wedding Invitation Generator", {
    x:0.5, y:2.82, w:9, h:0.45,
    fontSize:16, color:GOLD,
    align:"center", fontFace:"Georgia", italic:true
  });

  const techLine = "Flask  ·  Groq LLM  ·  SVG Engine  ·  SQLite  ·  Render.com";
  s.addText(techLine, {
    x:0.5, y:3.35, w:9, h:0.35,
    fontSize:11, color:GRAY,
    align:"center", fontFace:"Calibri", charSpacing:1
  });

  // decorative dots
  for (let i=0; i<7; i++) {
    s.addShape(pres.shapes.OVAL, {
      x: 3.5 + i*0.45, y:3.88, w:0.14, h:0.14,
      fill:{ color: i===3 ? GOLD : "3a2010" }, line:{ color:GOLD }
    });
  }

  s.addText("Built with dedication, debugged with patience, deployed with pride.", {
    x:0.5, y:4.2, w:9, h:0.35,
    fontSize:11, color:GOLD, align:"center",
    fontFace:"Georgia", italic:true
  });
}

pres.writeFile({ fileName: "/mnt/user-data/outputs/AI_Wedding_Invitation_Generator.pptx" })
  .then(() => console.log("PPT written!"))
  .catch(e => console.error(e));