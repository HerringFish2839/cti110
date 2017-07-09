import turtle
import random

wn = turtle.Screen()
Ruby = turtle.Turtle()
Ruby.shape("turtle")
wn.bgcolor("Grey")
Ruby.pensize(4)

Ruby.color("Red")

colors = ["Red", "White", "Black", "Yellow"]

#Drawing the Snowflake
for i in range(10):
    for i in range(2):
        Ruby.forward(100)
        Ruby.right(60)
        Ruby.forward(100)
        Ruby.right(120)
    Ruby.right(36)
    Ruby.color(random.choice(colors))

wn.exitonclick()
