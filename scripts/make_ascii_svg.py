from pathlib import Path
from PIL import Image

# Bright -> Dark
RAMP = " .`:-=+*cs#%@"

INPUT = Path("assets/source-prepped.png")
OUTPUT = Path("assets/avi-ascii.svg")

COLS = 105
ROWS = 50

FONT_SIZE = 9
LINE_HEIGHT = 10
FONT_FAMILY = "monospace"


def pixel_to_char(value):
    idx = int(value / 255 * (len(RAMP) - 1))
    return RAMP[idx]


img = Image.open(INPUT).convert("L")
img = img.resize((COLS, ROWS))

pixels = img.load()

lines = []

for y in range(ROWS):
    row = ""
    for x in range(COLS):
        row += pixel_to_char(pixels[x, y])
    lines.append(row)

svg_width = COLS * 6.2
svg_height = ROWS * LINE_HEIGHT + 20

svg = []

svg.append(f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{svg_width}"
height="{svg_height}"
viewBox="0 0 {svg_width} {svg_height}">
''')

svg.append("""
<style>
text{
fill:#d0d0d0;
font-family:monospace;
font-size:9px;
white-space:pre;
}
</style>
""")

for i, line in enumerate(lines):

    delay = i * 0.08

    svg.append(f'''
<g opacity="0">
<animate attributeName="opacity"
begin="{delay}s"
dur="0.01s"
fill="freeze"
to="1"/>
<text x="0" y="{15+i*LINE_HEIGHT}">
{line}
</text>
</g>
''')

svg.append("</svg>")

OUTPUT.write_text("".join(svg), encoding="utf-8")

print("Generated:", OUTPUT)