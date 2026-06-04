import re

path = r"C:\PROJECTS\AI wedding card\app.py"
c = open(path, encoding="utf-8").read()

# Remove priority_display block
c = re.sub(
    r'\s*priority_display\s*=\s*\{.*?\}\s*\n\s*pd\s*=\s*priority_display\.get\([^\n]+\)\n',
    '\n',
    c, flags=re.DOTALL
)

# Remove pd lines from wedding_details
c = re.sub(r'\s*"priority_title"\s*:\s*pd\[0\][^\n]*\n', '\n', c)
c = re.sub(r'\s*"priority_tagline"\s*:\s*pd\[1\][^\n]*\n', '\n', c)

# Remove guest_priority variable if still there
c = re.sub(r'\s*guest_priority\s*=\s*request\.form\.get\([^\n]+\)\n', '\n', c)

# Remove from wedding_details dict
c = re.sub(r'\s*"guest_priority"\s*:\s*guest_priority[^\n]*\n', '\n', c)

open(path, "w", encoding="utf-8").write(c)
print("Fixed! Check app.py around line 300")