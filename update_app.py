import os

BASE = r"C:\PROJECTS\AI wedding card"

app_py = '''import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = Flask(__name__)

# Groq client - free tier, no credit card needed
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


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

    style_text = style_instructions.get(
        details["style"], style_instructions["modern"]
    )

    try:
        from datetime import datetime
        date_obj = datetime.strptime(details["wedding_date"], "%Y-%m-%d")
        formatted_date = date_obj.strftime("%B %d, %Y")
    except Exception:
        formatted_date = details["wedding_date"]

    try:
        from datetime import datetime
        raw_time = details["ceremony_time"]
        if raw_time:
            time_obj = datetime.strptime(raw_time, "%H:%M")
            formatted_time = time_obj.strftime("%I:%M %p")
        else:
            formatted_time = "Time to be announced"
    except Exception:
        formatted_time = details.get("ceremony_time", "Time to be announced")

    special_note_section = ""
    if details.get("special_msg"):
        special_note_section = f"\\nSpecial instruction: {details[\'special_msg\']}"

    prompt = f"""You are an expert wedding invitation writer with 20 years of experience.

Your task: Write a beautiful wedding invitation based on these details.

WEDDING DETAILS:
- Bride Name: {details[\'bride_name\']}
- Groom Name: {details[\'groom_name\']}
- Wedding Date: {formatted_date}
- Ceremony Time: {formatted_time}
- Venue: {details[\'venue_name\']}
- City: {details[\'venue_city\']}{special_note_section}

STYLE INSTRUCTION:
{style_text}

RULES:
1. Length: 120 to 180 words
2. Include couple names, date, time, venue, city
3. End with a warm closing line or RSVP note
4. Write ONLY the invitation text, no headings, no extra commentary
5. Make it emotionally warm and memorable

Write the invitation now:"""

    return prompt


def generate_invitation_text(details):
    """
    Calls Groq API (free) to generate invitation.
    Returns (invitation_text, error_message)
    """
    try:
        prompt = build_prompt(details)

        # Groq uses OpenAI-compatible API format
        # llama-3.3-70b-versatile is free and very powerful
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a professional wedding invitation writer. "
                        "You write beautiful, emotional, and memorable invitations. "
                        "You follow instructions precisely and write ONLY the invitation text."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.3-70b-versatile",
            max_tokens=400,
            temperature=0.8,
        )

        invitation_text = chat_completion.choices[0].message.content.strip()
        return invitation_text, None

    except Exception as e:
        error_msg = str(e)
        print(f"Groq Error: {error_msg}")
        return None, error_msg


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

    invitation_text, ai_error = generate_invitation_text(wedding_details)

    return render_template(
        "invitation.html",
        details=wedding_details,
        invitation_text=invitation_text,
        ai_error=ai_error
    )


if __name__ == "__main__":
    app.run(debug=True)
'''

path = os.path.join(BASE, "app.py")
with open(path, "w", encoding="utf-8") as f:
    f.write(app_py)
print("app.py updated with Groq!")
print("Now run: python app.py")