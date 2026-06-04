import os
import io
import uuid
import json
import urllib.parse
from datetime import datetime

from flask import (Flask, render_template, request,
                   send_file, session, abort)
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "wedding-secret-2024")

# ── DATABASE SETUP ─────────────────────────────────────────
# SQLite database — stores each generated invitation
# so we can retrieve it via a unique share link
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///invitations.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

db_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "instance",
    "invitations.db"
)
os.makedirs(os.path.dirname(db_path), exist_ok=True)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
# ── DATABASE MODEL ──────────────────────────────────────────
class Invitation(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    share_id        = db.Column(db.String(12), unique=True, nullable=False)
    bride_name      = db.Column(db.String(100))
    groom_name      = db.Column(db.String(100))
    wedding_date    = db.Column(db.String(20))
    ceremony_time   = db.Column(db.String(10))
    venue_name      = db.Column(db.String(200))
    venue_city      = db.Column(db.String(100))
    style           = db.Column(db.String(20))
    card_design     = db.Column(db.String(30))
    guest_priority  = db.Column(db.String(20))
    special_msg     = db.Column(db.Text)
    invitation_text = db.Column(db.Text)
    ceremonies_json = db.Column(db.Text)       # stored as JSON string
    created_at      = db.Column(db.DateTime, default=datetime.utcnow)


# Map card design names to their template files
CARD_TEMPLATES = {
    "peacock_royal":   "card_peacock.html",
    "purple_maharaja": "card_purple.html",
    "sindoor_red":     "card_sindoor.html",
    "midnight_lotus":  "card_midnight.html",
    "rose_mehndi":     "card_rose.html",
    "forest_sage":     "card_forest.html",
    "royal_gold":      "invitation.html",
}

def get_card_template(card_design):
    return CARD_TEMPLATES.get(card_design, "invitation.html")


# Create tables if they don't exist
with app.app_context():
    db.create_all()


# ── GROQ CLIENT ─────────────────────────────────────────────
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


@app.route("/debug-session")
def debug_session():
    import json
    details = session.get("wedding_details", {})
    return f"<pre>{json.dumps(details, indent=2, default=str)}</pre>"
# ── PROMPT BUILDER ──────────────────────────────────────────
def build_prompt(details):
    style_instructions = {
        "traditional": (
            "Write in a warm, formal, traditional Indian style. "
            "Use respectful language, include blessings from elders, "
            "mention family honor and joy. Use phrases like "
            "With the blessings of the Almighty and With great joy. "
            "Tone should feel like a formal family announcement."
        ),
        "modern": (
            "Write in a clean, modern, minimalist style. "
            "Short sentences. Elegant and sophisticated tone. "
            "No religious references unless specified. "
            "Feel like a premium luxury invitation."
        ),
        "funny": (
            "Write in a fun, witty, casual style. "
            "Add light humor and keep it warm. "
            "Make guests smile and excited to attend. "
            "Keep it joyful and personal."
        )
    }

    # Priority changes the emotional depth — invisible to guest
    priority_instructions = {
        "vip": (
            "This invitation is for a very close elder or VIP guest. "
            "Use deeply respectful, warm, and honorific language. "
            "Make them feel their presence is irreplaceable."
        ),
        "family": (
            "This is for a family member. "
            "Use warm, loving, and personal language. "
            "Make it feel like a heartfelt family call."
        ),
        "friends": (
            "This is for a close friend. "
            "Keep it warm, personal, and slightly casual. "
            "Make them feel excited and included."
        ),
        "general": (
            "This is a general invitation. "
            "Keep it warm, welcoming and gracious."
        )
    }

    style_text    = style_instructions.get(
        details["style"], style_instructions["modern"]
    )
    priority_text = priority_instructions.get(
        details.get("guest_priority", "general"),
        priority_instructions["general"]
    )

    try:
        date_obj       = datetime.strptime(details["wedding_date"], "%Y-%m-%d")
        formatted_date = date_obj.strftime("%B %d, %Y")
    except Exception:
        formatted_date = details["wedding_date"]

    try:
        raw_time = details["ceremony_time"]
        if raw_time:
            time_obj       = datetime.strptime(raw_time, "%H:%M")
            formatted_time = time_obj.strftime("%I:%M %p")
        else:
            formatted_time = "Time to be announced"
    except Exception:
        formatted_time = "Time to be announced"

    special_note_section = ""
    if details.get("special_msg"):
        special_note_section = f"\nSpecial instruction: {details['special_msg']}"

    prompt = f"""You are an expert wedding invitation writer with 20 years of experience.

Your task: Write a beautiful wedding invitation based on these details.

WEDDING DETAILS:
- Bride Name: {details['bride_name']}
- Groom Name: {details['groom_name']}
- Wedding Date: {formatted_date}
- Ceremony Time: {formatted_time}
- Venue: {details['venue_name']}
- City: {details['venue_city']}{special_note_section}

STYLE INSTRUCTION:
{style_text}

GUEST TONE INSTRUCTION (do not mention this in the text):
{priority_text}

RULES:
1. Length: MAXIMUM 100 words. Be concise and beautiful.
2. Include couple names, date, time, venue, city
3. End with a warm closing line
4. Write ONLY the invitation text, no headings, no extra commentary
5. Make it emotionally warm and memorable

Write the invitation now:"""

    return prompt


# ── AI GENERATION ────────────────────────────────────────────
def generate_invitation_text(details):
    try:
        prompt = build_prompt(details)
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a professional wedding invitation writer. "
                        "You write beautiful, emotional, and memorable invitations. "
                        "You follow instructions precisely."
                    )
                },
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile",
            max_tokens=300,
            temperature=0.8,
        )
        return chat_completion.choices[0].message.content.strip(), None
    except Exception as e:
        print(f"Groq Error: {e}")
        return None, str(e)


# ── HELPER: format details dict from DB row ──────────────────
def invitation_to_details(inv):
    import json
    details = {
        "bride_name":     inv.bride_name,
        "groom_name":     inv.groom_name,
        "wedding_date":   inv.wedding_date,
        "ceremony_time":  inv.ceremony_time,
        "venue_name":     inv.venue_name,
        "venue_city":     inv.venue_city,
        "style":          inv.style,
        "card_design":    inv.card_design   or "royal_gold",
        "guest_priority": inv.guest_priority or "general",
        "special_msg":    inv.special_msg   or "",
        "ceremonies":     json.loads(inv.ceremonies_json) if inv.ceremonies_json else {},
    }
    return details


# ── HELPER: build share URLs ─────────────────────────────────
def build_share_urls(inv, share_link):
    bride = inv.bride_name
    groom = inv.groom_name
    date  = inv.wedding_date
    venue = inv.venue_name
    city  = inv.venue_city

    share_text = (
        f"You're invited! {bride} & {groom} are getting married!\n"
        f"Date: {date}\n"
        f"Venue: {venue}, {city}\n\n"
        f"View the full invitation card here:\n{share_link}"
    )

    whatsapp_url = (
        f"https://wa.me/?text={urllib.parse.quote(share_text)}"
    )

    email_subject = f"Wedding Invitation — {bride} & {groom}"
    email_url = (
        f"mailto:?subject={urllib.parse.quote(email_subject)}"
        f"&body={urllib.parse.quote(share_text)}"
    )

    return whatsapp_url, email_url


# ── ROUTES ───────────────────────────────────────────────────

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    # Basic fields
    bride_name    = request.form.get("bride_name", "").strip()
    groom_name    = request.form.get("groom_name", "").strip()
    wedding_date  = request.form.get("wedding_date", "").strip()
    venue_name    = request.form.get("venue_name", "").strip()
    venue_city    = request.form.get("venue_city", "").strip()
    ceremony_time = request.form.get("ceremony_time", "").strip()
    style         = request.form.get("style", "traditional")
    special_msg   = request.form.get("special_msg", "").strip()
    card_design   = request.form.get("card_design", "royal_gold")

    # Ceremony fields
    ceremonies = {}
    for name, emoji, label in [
        ("haldi",     "🌼", "Haldi Ceremony"),
        ("mehendi",   "🌿", "Mehendi Ceremony"),
        ("reception", "🥂", "Wedding Reception"),
    ]:
        if request.form.get(f"{name}_enabled"):
            ceremonies[name] = {
                "label": label,
                "emoji": emoji,
                "date":  request.form.get(f"{name}_date", ""),
                "time":  request.form.get(f"{name}_time", ""),
                "venue": request.form.get(f"{name}_venue", ""),
            }

    errors = []
    if not bride_name:   errors.append("Bride name is required.")
    if not groom_name:   errors.append("Groom name is required.")
    if not wedding_date: errors.append("Wedding date is required.")
    if not venue_name:   errors.append("Venue name is required.")
    if not venue_city:   errors.append("Venue city is required.")

    if errors:
        return render_template("index.html", errors=errors)

    wedding_details = {
        "bride_name":     bride_name,
        "groom_name":     groom_name,
        "wedding_date":   wedding_date,
        "venue_name":     venue_name,
        "venue_city":     venue_city,
        "ceremony_time":  ceremony_time,
        "style":          style,
        "special_msg":    special_msg,
        "card_design":    card_design,
        "ceremonies":     ceremonies,
    }

    invitation_text, ai_error = generate_invitation_text(wedding_details)

    if ai_error:
        return render_template(
            "invitation.html",
            details=wedding_details,
            invitation_text=None,
            ai_error=ai_error,
            share_link=None,
            whatsapp_url="#",
            email_url="#"
        )

    share_id = uuid.uuid4().hex[:10]
    import json
    inv = Invitation(
        share_id        = share_id,
        bride_name      = bride_name,
        groom_name      = groom_name,
        wedding_date    = wedding_date,
        ceremony_time   = ceremony_time,
        venue_name      = venue_name,
        venue_city      = venue_city,
        style           = style,
        card_design     = card_design,
        special_msg     = special_msg,
        invitation_text = invitation_text,
        ceremonies_json = json.dumps(ceremonies)   # ← save ceremonies as JSON
    )
    db.session.add(inv)
    db.session.commit()

    base_url   = request.host_url.rstrip("/")
    share_link = f"{base_url}/invitation/{share_id}"

    session["wedding_details"]  = wedding_details
    session["invitation_text"]  = invitation_text

    whatsapp_url, email_url = build_share_urls(inv, share_link)

    template = get_card_template(card_design)

    return render_template(
        template,
        details=wedding_details,
        invitation_text=invitation_text,
        ai_error=None,
        share_link=share_link,
        whatsapp_url=whatsapp_url,
        email_url=email_url
    )

def invitation_to_details(inv):
    import json
    priority_display = {
        "vip":     ("Special Invitation", "With deepest respect and honour"),
        "family":  ("Family Invitation",  "With love from our family to yours"),
        "friends": ("Personal Invitation","You are cordially invited"),
        "general": ("Invitation",         "We request the pleasure of your company"),
    }
    gp = inv.guest_priority or "general"
    pd = priority_display.get(gp, priority_display["general"])

    return {
        "bride_name":       inv.bride_name,
        "groom_name":       inv.groom_name,
        "wedding_date":     inv.wedding_date,
        "ceremony_time":    inv.ceremony_time,
        "venue_name":       inv.venue_name,
        "venue_city":       inv.venue_city,
        "style":            inv.style,
        "card_design":      inv.card_design   or "royal_gold",
        "guest_priority":   gp,
        "special_msg":      inv.special_msg   or "",
        "ceremonies":       json.loads(inv.ceremonies_json) if inv.ceremonies_json else {},
    }

@app.route("/invitation/<share_id>")
def view_invitation(share_id):
    inv = Invitation.query.filter_by(share_id=share_id).first()
    if not inv:
        abort(404)
    details    = invitation_to_details(inv)
    share_link = request.url
    whatsapp_url, email_url = build_share_urls(inv, share_link)
    template = get_card_template(details.get("card_design", "royal_gold"))
    return render_template(
        template,
        details=details,
        invitation_text=inv.invitation_text,
        ai_error=None,
        share_link=share_link,
        whatsapp_url=whatsapp_url,
        email_url=email_url
    )


@app.route("/download-pdf")
def download_pdf():
    details         = session.get("wedding_details")
    invitation_text = session.get("invitation_text")

    if not details or not invitation_text:
        return "Session expired. Please generate your invitation again.", 400

    html_content = build_pdf_html(details, invitation_text)

    try:
        from xhtml2pdf import pisa
        pdf_buffer = io.BytesIO()
        result = pisa.CreatePDF(html_content, dest=pdf_buffer)
        if result.err:
            return "PDF generation failed.", 500
        pdf_bytes = pdf_buffer.getvalue()
        bride     = details.get("bride_name", "bride").split()[0]
        groom     = details.get("groom_name", "groom").split()[0]
        filename  = f"{bride}_and_{groom}_Wedding_Invitation.pdf"
        return send_file(
            io.BytesIO(pdf_bytes),
            mimetype="application/pdf",
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return f"PDF error: {str(e)}", 500


def build_pdf_html(details, invitation_text):
    if details["style"] == "traditional":
        primary_color = "#8b1a4a"
        accent_color  = "#c9a96e"
        bg_color      = "#fffdf5"
        border_color  = "#c9a96e"
        text_color    = "#3d2b1f"
    elif details["style"] == "modern":
        primary_color = "#1a1a1a"
        accent_color  = "#888888"
        bg_color      = "#ffffff"
        border_color  = "#2c2c2c"
        text_color    = "#1a1a1a"
    else:
        primary_color = "#e91e8c"
        accent_color  = "#ff9800"
        bg_color      = "#fff9f0"
        border_color  = "#e91e8c"
        text_color    = "#3d2b1f"

    try:
        date_obj       = datetime.strptime(details["wedding_date"], "%Y-%m-%d")
        formatted_date = date_obj.strftime("%B %d, %Y")
    except Exception:
        formatted_date = details["wedding_date"]

    try:
        raw_time = details["ceremony_time"]
        if raw_time:
            time_obj       = datetime.strptime(raw_time, "%H:%M")
            formatted_time = time_obj.strftime("%I:%M %p")
        else:
            formatted_time = ""
    except Exception:
        formatted_time = ""

    time_block = ""
    if formatted_time:
        time_block = f"""
        <td width="33%" style="text-align:center; padding:10px 20px;
            border-left:1px solid {accent_color};">
            <p style="font-size:8px;letter-spacing:3px;color:{primary_color};
               margin:0 0 4px 0;font-family:Helvetica;">TIME</p>
            <p style="font-size:13px;font-weight:bold;color:{text_color};
               margin:0;font-family:Georgia;">{formatted_time}</p>
        </td>"""

    return f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<style>
@page {{ size:A4 portrait; margin:15mm; }}
body {{ background:{bg_color}; margin:0; padding:20px;
       font-family:Georgia,serif; }}
.outer {{ border:3px double {border_color}; padding:6px; }}
.card  {{ background:{bg_color}; border:1px solid {border_color};
          padding:40px 50px; text-align:center; }}
.inner {{ border:1px solid {accent_color}; padding:30px 40px; }}
.together {{ font-family:Helvetica; font-size:8px; letter-spacing:5px;
             color:{accent_color}; margin:0 0 14px; text-transform:uppercase; }}
.bride {{ font-family:Georgia,serif; font-size:38px;
          color:{primary_color}; margin:0; line-height:1.3; }}
.amp   {{ font-family:Georgia,serif; font-size:28px;
          color:{accent_color}; margin:2px 0; }}
.groom {{ font-family:Georgia,serif; font-size:38px;
          color:{primary_color}; margin:0; line-height:1.3; }}
.orn   {{ font-size:14px; color:{accent_color};
          letter-spacing:10px; margin:14px 0; }}
.req   {{ font-family:Helvetica; font-size:9px; letter-spacing:2px;
          color:#7a6a62; margin:0 0 18px; }}
hr     {{ border:none; border-top:1px solid {accent_color};
          margin:14px auto; width:60%; }}
.body  {{ font-family:Georgia,serif; font-size:12px; line-height:1.9;
          color:{text_color}; font-style:italic; margin:14px 10px; }}
.dtbl  {{ width:70%; margin:14px auto; border-collapse:collapse; }}
.dlbl  {{ font-family:Helvetica; font-size:8px; letter-spacing:3px;
          text-transform:uppercase; color:{primary_color}; margin:0 0 4px; }}
.dval  {{ font-size:13px; font-weight:bold; color:{text_color}; margin:0; }}
.dsub  {{ font-family:Helvetica; font-size:9px;
          color:#7a6a62; margin:2px 0 0; }}
.rsvp  {{ font-family:Helvetica; font-size:8px; letter-spacing:3px;
          color:#9e8e85; text-transform:uppercase; margin:10px 0 0; }}
.ctbl  {{ width:100%; border-collapse:collapse; }}
</style></head><body>
<div class="outer"><div class="card"><div class="inner">
<table class="ctbl"><tr>
  <td style="text-align:left;color:{accent_color};font-size:14px;">&#10022;</td>
  <td style="text-align:right;color:{accent_color};font-size:14px;">&#10022;</td>
</tr></table>
<p class="together">&#10022; &nbsp; Together Forever &nbsp; &#10022;</p>
<p class="bride">{details['bride_name']}</p>
<p class="amp">&amp;</p>
<p class="groom">{details['groom_name']}</p>
<p class="orn">&#10040; &nbsp; &#10040; &nbsp; &#10040;</p>
<p class="req">joyfully request the pleasure of your company</p>
<hr>
<p class="body">{invitation_text}</p>
<hr>
<table class="dtbl"><tr>
  <td width="{'33%' if formatted_time else '50%'}"
      style="text-align:center;padding:10px 20px;">
    <p class="dlbl">Date</p>
    <p class="dval">{formatted_date}</p>
  </td>
  {time_block}
  <td width="{'33%' if formatted_time else '50%'}"
      style="text-align:center;padding:10px 20px;
             border-left:1px solid {accent_color};">
    <p class="dlbl">Venue</p>
    <p class="dval">{details['venue_name']}</p>
    <p class="dsub">{details['venue_city']}</p>
  </td>
</tr></table>
<p class="orn">&#10040;</p>
<table class="ctbl"><tr>
  <td style="text-align:left;color:{accent_color};font-size:14px;">&#10022;</td>
  <td style="text-align:right;color:{accent_color};font-size:14px;">&#10022;</td>
</tr></table>
<p class="rsvp">We joyfully await your presence &#10022;</p>
</div></div></div>
</body></html>"""


if __name__ == "__main__":
    app.run(debug=True)