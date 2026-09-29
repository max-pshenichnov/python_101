import turtle
from random import choice

# параметры экрана
screen = turtle.Screen()
screen.setup(600, 600)
screen.title("я - футбольный мячик")
screen.tracer(0)

ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(2)
#ball.penup()

colors = ["#FF0000", "#E79E0D", "#FFF700", "#1EFF00", "#00FFE5", "#2600FF", "#B700FF"]
ball.color(choice(colors))
           
LIMIT = 260
velocity = [4, 3]

def frame():
    x, y = ball.position()
    x += velocity[0]
    y += velocity[1]

    if x > LIMIT or x < -LIMIT:
        ball.color(choice(colors))
        velocity[0] = -velocity[0]
    if y > LIMIT or y < -LIMIT:
        ball.color(choice(colors))
        velocity[1] = -velocity[1]

    ball.goto(x, y)
    screen.update()
    screen.ontimer(frame, 5)

frame()
screen.mainloop()