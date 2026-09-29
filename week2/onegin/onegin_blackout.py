from PIL import Image, ImageDraw, ImageFont
from random import random

CENSOR = 0.72
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
    #######################################################
    x = MARGIN
    for word in line.split(" "):
        word_width_in_pixels = FONT.getlength(word)
        if random() < CENSOR:
            draw.rectangle(
                [(x, y + 2), (x + word_width_in_pixels + 3, y + LINE_HEIGHT - 2)],
                fill = "black"
            )
        x = x + FONT.getlength(word + " ")
    #######################################################
    y += LINE_HEIGHT

image.save("week2/onegin/onegin_blackout.png")
print("гатова")


print("")