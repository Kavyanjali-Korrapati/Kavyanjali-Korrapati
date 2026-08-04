from pathlib import Path
from html import escape

FONT_SIZE = 10
LINE_HEIGHT = 12
CHAR_WIDTH = 6

BACKGROUND = "#0d1117"
FOREGROUND = "#d7d7d7"

FONT = "'JetBrains Mono','Cascadia Code','Consolas',monospace"


def build_svg(lines, output_path):

    longest = max(len(x) for x in lines)

    width = longest * CHAR_WIDTH + 40
    height = len(lines) * LINE_HEIGHT + 30

    svg = []

    svg.append(f"""<svg xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">
""")

    svg.append(f"""
<style>
text{{
font-family:{FONT};
font-size:{FONT_SIZE}px;
fill:{FOREGROUND};
white-space:pre;
}}

.cursor{{
fill:{FOREGROUND};
}}

.bg{{
fill:{BACKGROUND};
}}
</style>
""")

    svg.append(
        f'<rect class="bg" x="0" y="0" width="{width}" height="{height}"/>'
    )

    total_delay = 0

    for i, line in enumerate(lines):

        line = escape(line)

        y = 20 + i * LINE_HEIGHT

        clip_id = f"clip{i}"

        line_width = len(line) * CHAR_WIDTH

        svg.append(f"""
<defs>
<clipPath id="{clip_id}">
<rect x="20"
      y="{y-10}"
      width="0"
      height="{LINE_HEIGHT+2}">
<animate attributeName="width"
begin="{total_delay}s"
dur="0.25s"
fill="freeze"
to="{line_width}"/>
</rect>
</clipPath>
</defs>
""")

        svg.append(f"""
<text
x="20"
y="{y}"
clip-path="url(#{clip_id})">
{line}
</text>
""")

        cursor_x = 20 + line_width

        svg.append(f"""
<rect
class="cursor"
x="{cursor_x}"
y="{y-9}"
width="2"
height="{LINE_HEIGHT}">
<animate attributeName="opacity"
values="1;0;1"
dur="0.8s"
repeatCount="indefinite"/>
<animate attributeName="x"
begin="{total_delay}s"
dur="0.25s"
from="20"
to="{cursor_x}"
fill="freeze"/>
</rect>
""")

        total_delay += 0.06

    svg.append("</svg>")

    Path(output_path).write_text(
        "".join(svg),
        encoding="utf-8"
    )