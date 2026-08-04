from pathlib import Path

OUTPUT = Path("assets/info-card.svg")

WIDTH = 520
HEIGHT = 300

BG = "#0d1117"
BORDER = "#30363d"
TEXT = "#c9d1d9"
ACCENT = "#58a6ff"

lines = [
    ("👤 Name", "Kavyanjali Korrapati"),
    ("🎓 Degree", "B.Tech CSE"),
    ("💻 Role", "Full Stack Developer"),
    ("⚛ Frontend", "React • Tailwind CSS"),
    ("⚙ Backend", "Node.js • Express"),
    ("🗄 Database", "MongoDB"),
    ("🤖 AI", "Python • IBM watsonx"),
    ("🌱 Learning", "DSA • MERN • GenAI"),
    ("📍 Location", "India"),
]

svg = []

svg.append(f"""
<svg xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}"
height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}">
""")

svg.append(f"""
<style>

.bg{{
fill:{BG};
stroke:{BORDER};
stroke-width:2;
}}

.title{{
fill:{ACCENT};
font-family:Consolas,monospace;
font-size:20px;
font-weight:bold;
}}

.label{{
fill:#8b949e;
font-family:Consolas,monospace;
font-size:15px;
}}

.value{{
fill:{TEXT};
font-family:Consolas,monospace;
font-size:15px;
}}

</style>
""")

svg.append(f"""
<rect
class="bg"
x="1"
y="1"
width="{WIDTH-2}"
height="{HEIGHT-2}"
rx="12"/>
""")

svg.append("""
<text class="title"
x="25"
y="35">

$ Hi from Kavyanjali Korrapati

</text>
""")

y = 70

for i, (label, value) in enumerate(lines):

    delay = i * 0.15

    svg.append(f"""
<g opacity="0">

<animate
attributeName="opacity"
begin="{delay}s"
dur="0.25s"
fill="freeze"
to="1"/>

<text class="label"
x="30"
y="{y}">
{label}
</text>

<text class="value"
x="180"
y="{y}">
{value}
</text>

</g>
""")

    y += 25

svg.append("</svg>")

OUTPUT.write_text("".join(svg), encoding="utf-8")

print("Generated:", OUTPUT)