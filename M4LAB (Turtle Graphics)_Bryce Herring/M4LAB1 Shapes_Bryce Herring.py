import turtle
turtle.shape("turtle")
turtle.pensize(2)

for i in [0,1,2,3]:
    turtle.forward(50)
    turtle.left(90)

for y in [0,1,2] :
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(50)
    
turtle.exitonclick()
