import turtle
from random import random, randint, choice

colors = ["red", "green", "blue", "yellow"]
for _ in range(10):
    # random_number = random() # от нуля до единицы
    random_number = randint(0, 255)
    random_color = choice(colors)
    print(f"случайное число: {random_number}")
    print(f"случайный цвет: {random_color}")
    print()

print("---" * 10)

# настройка окна черепахи
screen = turtle.Screen()
screen.setup(1000, 1000)
screen.bgcolor("#47005B") # можно использовать палитру. предварительно введя любой цвет! нпример #000000
screen.tracer(0)

# настройка черепахи
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
#t.color(choice(["#B52121", "#E79E0D", "#CE4800"]))

size = 5

for row in range(200):
    for col in range(200):
        t.color(choice(["#FF0000", "#E79E0D", "#FFF700", "#1EFF00", "#00FFE5", "#2600FF", "#B700FF"]))
        x = -500 + col * size
        y = 500 - row * size

        if random() < 0.5:
            t.penup()
            t.goto(x, y)
            #t.goto(random() * 1000 - 500, random() * 1000 - 500,)
            t.pendown()

            t.begin_fill()

            for _ in range(4):
                t.forward(size)
                #t.forward(size * random() * 10)
                t.right(90)

            t.end_fill()

        screen.update()

screen.update()
screen.exitonclick()





print("hello world")

