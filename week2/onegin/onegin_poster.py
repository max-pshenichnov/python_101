from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 4320, 7680
MARGIN = 260
LINE_HEIGHT = 21
FONT = ImageFont.truetype("C:/Windows/Fonts/georgia.ttf", 16)

with open("data/onegin.txt", encoding="utf-8") as file:
    words = file.read().split()

print(f"колво слов: {len(words)}")

lines = []
line = words[0]

for word in words[1:]:
    longer = line + " " + word
    if FONT.getlength(longer) <= WIDTH - 2 * MARGIN:
        line = longer
    else:
        lines.append(line)
        line = word

lines.append(line)
print(f"колво строк на изображении: {len(lines)}")

image = Image.new("RGB", (WIDTH, HEIGHT), "#FFFFFF")
draw = ImageDraw.Draw(image)
y = MARGIN

for line in lines:
    draw.text((MARGIN, y), line, font=FONT, fill="#383838")
    y += LINE_HEIGHT

image.save("onegin_poster.png")
print("гатова")


print("")