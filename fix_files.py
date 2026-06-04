import os

# This script force-writes all project files correctly

BASE = r"C:\PROJECTS\AI wedding card"

# ── app.py ──────────────────────────────────────────────
app_py = '''from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    bride_name    = request.form.get("bride_name", "").strip()
    groom_name    = request.form.get("groom_name", "").strip()
    wedding_date  = request.form.get("wedding_date", "").strip()
    venue_name    = request.form.get("venue_name", "").strip()
    venue_city    = request.form.get("venue_city", "").strip()
    ceremony_time = request.form.get("ceremony_time", "").strip()
    style         = request.form.get("style", "traditional")
    special_msg   = request.form.get("special_msg", "").strip()

    errors = []
    if not bride_name:   errors.append("Bride name is required.")
    if not groom_name:   errors.append("Groom name is required.")
    if not wedding_date: errors.append("Wedding date is required.")
    if not venue_name:   errors.append("Venue name is required.")
    if not venue_city:   errors.append("Venue city is required.")

    if errors:
        return render_template("index.html", errors=errors)

    wedding_details = {
        "bride_name":    bride_name,
        "groom_name":    groom_name,
        "wedding_date":  wedding_date,
        "venue_name":    venue_name,
        "venue_city":    venue_city,
        "ceremony_time": ceremony_time,
        "style":         style,
        "special_msg":   special_msg
    }
    return render_template("invitation.html", details=wedding_details)

if __name__ == "__main__":
    app.run(debug=True)
'''

# ── index.html ───────────────────────────────────────────
index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Wedding Invitation Generator</title>
    <link rel="stylesheet" href="{{ url_for(\'static\', filename=\'css/style.css\') }}">
</head>
<body>
<div class="page-wrapper">
  <div class="container">

    <div class="header">
      <h1>&#128141; AI Wedding Invitation Generator</h1>
      <p class="subtitle">Fill in your wedding details and let AI craft the perfect invitation</p>
    </div>

    {% if errors %}
    <div class="error-box">
      <p><strong>Please fix the following:</strong></p>
      <ul>{% for e in errors %}<li>{{ e }}</li>{% endfor %}</ul>
    </div>
    {% endif %}

    <form action="/generate" method="POST" class="wedding-form">

      <div class="form-section">
        <h2 class="section-title">The Couple</h2>
        <div class="form-row">
          <div class="form-group">
            <label for="bride_name">Bride Full Name *</label>
            <input type="text" id="bride_name" name="bride_name" placeholder="e.g. Priya Sharma" required>
          </div>
          <div class="form-group">
            <label for="groom_name">Groom Full Name *</label>
            <input type="text" id="groom_name" name="groom_name" placeholder="e.g. Arjun Mehta" required>
          </div>
        </div>
      </div>

      <div class="form-section">
        <h2 class="section-title">Event Details</h2>
        <div class="form-row">
          <div class="form-group">
            <label for="wedding_date">Wedding Date *</label>
            <input type="date" id="wedding_date" name="wedding_date" required>
          </div>
          <div class="form-group">
            <label for="ceremony_time">Ceremony Time</label>
            <input type="time" id="ceremony_time" name="ceremony_time">
          </div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label for="venue_name">Venue Name *</label>
            <input type="text" id="venue_name" name="venue_name" placeholder="e.g. The Grand Ballroom" required>
          </div>
          <div class="form-group">
            <label for="venue_city">Venue City *</label>
            <input type="text" id="venue_city" name="venue_city" placeholder="e.g. Mumbai" required>
          </div>
        </div>
      </div>

      <div class="form-section">
        <h2 class="section-title">Invitation Style</h2>
        <p class="section-hint">This controls the tone the AI will use</p>
        <div class="style-grid">
          <label class="style-card" for="style_traditional">
            <input type="radio" id="style_traditional" name="style" value="traditional" checked>
            <div class="style-content">
              <span class="style-icon">&#128686;</span>
              <span class="style-name">Traditional Indian</span>
              <span class="style-desc">Formal, family-oriented</span>
            </div>
          </label>
          <label class="style-card" for="style_modern">
            <input type="radio" id="style_modern" name="style" value="modern">
            <div class="style-content">
              <span class="style-icon">&#10024;</span>
              <span class="style-name">Modern Minimal</span>
              <span class="style-desc">Clean, elegant</span>
            </div>
          </label>
          <label class="style-card" for="style_funny">
            <input type="radio" id="style_funny" name="style" value="funny">
            <div class="style-content">
              <span class="style-icon">&#128514;</span>
              <span class="style-name">Funny and Casual</span>
              <span class="style-desc">Witty and fun</span>
            </div>
          </label>
        </div>
      </div>

      <div class="form-section">
        <h2 class="section-title">Personal Touch</h2>
        <div class="form-group">
          <label for="special_msg">Special Note (optional)</label>
          <textarea id="special_msg" name="special_msg" rows="3"
            placeholder="e.g. We met in college, mention dress code..."></textarea>
        </div>
      </div>

      <button type="submit" class="submit-btn">Generate My Invitation</button>

    </form>
  </div>
</div>
<script src="{{ url_for(\'static\', filename=\'js/main.js\') }}"></script>
</body>
</html>'''

# ── invitation.html ──────────────────────────────────────
invitation_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wedding Details Preview</title>
    <link rel="stylesheet" href="{{ url_for(\'static\', filename=\'css/style.css\') }}">
</head>
<body>
<div class="page-wrapper">
  <div class="container">
    <div class="header">
      <h1>&#128141; Details Received!</h1>
      <p class="subtitle">Step 2 complete. AI generation coming next.</p>
    </div>
    <div class="details-preview">
      <h2>Here is what we received:</h2>
      <table class="details-table">
        <tr><td class="label">Bride</td><td>{{ details.bride_name }}</td></tr>
        <tr><td class="label">Groom</td><td>{{ details.groom_name }}</td></tr>
        <tr><td class="label">Date</td><td>{{ details.wedding_date }}</td></tr>
        <tr><td class="label">Time</td><td>{{ details.ceremony_time if details.ceremony_time else "Not specified" }}</td></tr>
        <tr><td class="label">Venue</td><td>{{ details.venue_name }}</td></tr>
        <tr><td class="label">City</td><td>{{ details.venue_city }}</td></tr>
        <tr><td class="label">Style</td><td>{{ details.style | capitalize }}</td></tr>
        <tr><td class="label">Note</td><td>{{ details.special_msg if details.special_msg else "None" }}</td></tr>
      </table>
      <a href="/" class="back-btn">Edit Details</a>
    </div>
  </div>
</div>
</body>
</html>'''

# ── style.css ────────────────────────────────────────────
style_css = '''* { margin:0; padding:0; box-sizing:border-box; }
body { font-family: Georgia, serif; background:#fdf6f0; color:#3d2b1f; min-height:100vh; }
.page-wrapper { min-height:100vh; padding:40px 20px; display:flex; justify-content:center; }
.container { width:100%; max-width:780px; }
.header { text-align:center; margin-bottom:36px; }
h1 { font-size:2.2rem; color:#8b1a4a; margin-bottom:10px; }
.subtitle { font-size:1rem; color:#7a6a62; }
.error-box { background:#fff0f0; border:1.5px solid #e57373; border-radius:10px;
  padding:16px 20px; margin-bottom:24px; color:#b71c1c; }
.error-box ul { margin-top:8px; padding-left:20px; }
.wedding-form { display:flex; flex-direction:column; gap:24px; }
.form-section { background:white; border:1.5px solid #e8d5c4; border-radius:14px;
  padding:28px; box-shadow:0 2px 12px rgba(139,26,74,0.06); }
.section-title { font-size:1.1rem; color:#8b1a4a; margin-bottom:16px; font-weight:bold; }
.section-hint { font-size:0.88rem; color:#9e8e85; margin-bottom:12px; margin-top:-10px; }
.form-row { display:grid; grid-template-columns:1fr 1fr; gap:18px; margin-bottom:16px; }
.form-row:last-child { margin-bottom:0; }
.form-group { display:flex; flex-direction:column; gap:6px; }
label { font-size:0.9rem; font-weight:bold; color:#5a3e35; }
input[type=text], input[type=date], input[type=time], textarea {
  width:100%; padding:10px 14px; border:1.5px solid #d4b8a8; border-radius:8px;
  font-size:0.95rem; font-family:inherit; background:#fffaf7; color:#3d2b1f;
  transition:border-color 0.2s; outline:none; }
input:focus, textarea:focus { border-color:#8b1a4a; background:white; }
textarea { resize:vertical; min-height:80px; }
.style-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:14px; margin-top:10px; }
.style-card input[type=radio] { display:none; }
.style-card { cursor:pointer; border:2px solid #e0cfc6; border-radius:12px;
  padding:16px 12px; text-align:center; background:#fffaf7; transition:all 0.2s; }
.style-card:hover { border-color:#c47e9a; background:#fff0f5; }
.style-card.selected { border-color:#8b1a4a; background:#fff0f5;
  box-shadow:0 0 0 3px rgba(139,26,74,0.15); }
.style-content { display:flex; flex-direction:column; gap:4px; pointer-events:none; }
.style-icon { font-size:1.8rem; }
.style-name { font-weight:bold; font-size:0.9rem; color:#5a3e35; }
.style-desc { font-size:0.78rem; color:#9e8e85; }
.submit-btn { width:100%; padding:16px;
  background:linear-gradient(135deg,#8b1a4a,#c2185b); color:white;
  font-size:1.1rem; font-family:inherit; border:none; border-radius:12px;
  cursor:pointer; transition:transform 0.2s, box-shadow 0.2s; }
.submit-btn:hover { transform:translateY(-2px); box-shadow:0 6px 20px rgba(139,26,74,0.35); }
.details-preview { background:white; border:1.5px solid #e8d5c4; border-radius:14px;
  padding:32px; box-shadow:0 2px 12px rgba(139,26,74,0.06); }
.details-preview h2 { color:#8b1a4a; margin-bottom:20px; }
.details-table { width:100%; border-collapse:collapse; margin-bottom:24px; }
.details-table tr { border-bottom:1px solid #f0e4db; }
.details-table td { padding:12px 8px; font-size:0.95rem; }
.details-table .label { font-weight:bold; color:#8b1a4a; width:120px; }
.back-btn { display:inline-block; padding:10px 22px; background:white; color:#8b1a4a;
  border:2px solid #8b1a4a; border-radius:8px; text-decoration:none; transition:all 0.2s; }
.back-btn:hover { background:#8b1a4a; color:white; }
@media(max-width:580px) { h1{font-size:1.8rem;} .form-row{grid-template-columns:1fr;}
  .style-grid{grid-template-columns:1fr;} }'''

# ── main.js ──────────────────────────────────────────────
main_js = '''document.addEventListener("DOMContentLoaded", function() {
  const cards = document.querySelectorAll(".style-card");
  cards.forEach(function(card) {
    card.addEventListener("click", function() {
      cards.forEach(function(c) { c.classList.remove("selected"); });
      card.classList.add("selected");
    });
  });
  const def = document.querySelector(".style-card input[type=\'radio\']:checked");
  if (def) def.closest(".style-card").classList.add("selected");

  const form = document.querySelector(".wedding-form");
  const btn  = document.querySelector(".submit-btn");
  if (form && btn) {
    form.addEventListener("submit", function() {
      btn.textContent = "Generating...";
      btn.disabled = true;
    });
  }
});'''

# ── Write all files ──────────────────────────────────────
files = {
    os.path.join(BASE, "app.py"):                          app_py,
    os.path.join(BASE, "templates", "index.html"):         index_html,
    os.path.join(BASE, "templates", "invitation.html"):    invitation_html,
    os.path.join(BASE, "static", "css", "style.css"):      style_css,
    os.path.join(BASE, "static", "js", "main.js"):         main_js,
}

for path, content in files.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {path}")

print("\nAll files written successfully! Now run: python app.py")