from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 4320, 7680
MARGIN = 260
LINE_HEIGHT = 21
FONT = ImageFont.truetype("C:/Windows/Fonts/georgia.ttf", 16)

with open("data/onegin.txt", encoding="utf-8") as file:
    text = file.read()
    words = text.split()

    
    # print(f"букв а: {text.count('а')}")
    # print(f"букв б: {text.count('б')}")
    # print(f"связей: {text.count('а') * text.count('б')}")

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
#######################################################
evgenys = []
tatianas = []
offset_x = 5 # сдвиг точек по x
offset_y = -12 # сдвиг точек по y
#######################################################
y = MARGIN

for line in lines:
    draw.text((MARGIN, y), line, font=FONT, fill="#383838")
    ##################################################
    x = MARGIN
    for word in line.split(' '):
        if "Евген" in word or "Онеги" in word:
            evgenys.append((x + offset_x, y + offset_y + LINE_HEIGHT))
        if "Татьян" in word or "Тан" in word:
                    tatianas.append((x + offset_x, y + offset_y + LINE_HEIGHT))
        x += FONT.getlength(word + " ")
    ##################################################
    y += LINE_HEIGHT
############################
print(f"колво евгениев: {len(evgenys)}")
print(f"колво татьян: {len(tatianas)}")

pen = ImageDraw.Draw(image, "RGBA")
for evgeny in evgenys:
     for tatiana in tatianas:
          pen.line([evgeny, tatiana], fill=(190, 40, 40, 40), width=3)

############################

image.save("onegin_poster.png")
print("гатова")


print("")