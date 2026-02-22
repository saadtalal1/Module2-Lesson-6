import turtle
turtle.Screen().bgcolor("black")
turtle.Screen().setup(300,400)
turtle.Turtle()
turtle.color("white")
turtle.goto(0,0)
turtle.right(90)
side_length=5
num_sides=100
for i in range(num_sides):
    turtle.forward(side_length)
    turtle.right(90)
    side_length=i+10
turtle.done()
