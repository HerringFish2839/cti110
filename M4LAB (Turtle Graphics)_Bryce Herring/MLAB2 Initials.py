import turtle

win = turtle.Screen()
Tead = turtle.Turtle()
Tead.shape("turtle")
win.bgcolor("Black")
Tead.color("Blue")
Tead.pensize(5)


#Spacing
Tead.penup()
Tead.backward(100)
Tead.pendown()

#Letter B
Tead.left(90)
Tead.forward(120)
Tead.left(90)
Tead.forward(10)
Tead.backward(10)
Tead.right(90)
Tead.right(90)
Tead.forward(70)
Tead.right(90)
Tead.forward(60)
Tead.right(90)
Tead.forward(70)
Tead.left(90)
Tead.forward(60)
Tead.left(90)
Tead.backward(10)
Tead.forward(80)
Tead.left(90)
Tead.forward(60)

#Letter H
Tead.right(90)
Tead.penup()
Tead.forward(70)
Tead.pendown()
Tead.left(90)
Tead.forward(60)
Tead.backward(120)
Tead.forward(60)
Tead.right(90)
Tead.forward(70)
Tead.left(90)
Tead.forward(60)
Tead.backward(120)

#Initial
Tead.left(90)
Tead.penup()
Tead.forward(105)
Tead.right(90)
Tead.pendown()






win.exitonclick()
