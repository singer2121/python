import turtle
loadwindow = turtle.Screen()
turtle.speed(12)

for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)

turtle.exitonclick()