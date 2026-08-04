from pathlib import Path
from github_api import get_contributions

USERNAME = "Kavyanjali-Korrapati"

OUTPUT = Path("assets/contrib-heatmap.svg")

CELL = 12
GAP = 3
RADIUS = 2

BG = "#0d1117"


weeks = get_contributions(USERNAME)

cols = len(weeks)
rows = 7

width = cols * (CELL + GAP) + 20
height = rows * (CELL + GAP) + 20

svg = []

svg.append(f"""
<svg xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">
""")

svg.append(f"""
<style>
.bg {{
fill:{BG};
}}

rect.cell {{
stroke:none;
}}
</style>
""")

svg.append(
f'<rect class="bg" x="0" y="0" width="{width}" height="{height}"/>'
)

delay = 0

for x, week in enumerate(weeks):

    for y, day in enumerate(week["contributionDays"]):

        px = 10 + x * (CELL + GAP)
        py = 10 + y * (CELL + GAP)

        color = day["color"]

        svg.append(f"""
<rect
class="cell"
x="{px}"
y="{py}"
width="{CELL}"
height="{CELL}"
rx="{RADIUS}"
fill="{color}"
opacity="0">

<animate
attributeName="opacity"
begin="{delay:.2f}s"
dur="0.20s"
fill="freeze"
from="0"
to="1"/>

<animateTransform
attributeName="transform"
type="translate"
begin="{delay:.2f}s"
dur="0.20s"
from="-5 -5"
to="0 0"
fill="freeze"/>

</rect>
""")

        delay += 0.01

svg.append("</svg>")

OUTPUT.write_text(
    "".join(svg),
    encoding="utf-8"
)

print("Generated:", OUTPUT)