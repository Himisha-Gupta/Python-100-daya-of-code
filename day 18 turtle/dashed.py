from turtle import Turtle, Screen
tt_turtle_obj = Turtle()

for _ in range(25):
    tt_turtle_obj.forward(5)
    tt_turtle_obj.penup()
    tt_turtle_obj.forward(5)
    tt_turtle_obj.pendown()

screen = Screen()
screen.exitonclick()