from turtle import Turtle , Screen
import random
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(700,600)
screen.tracer(0)


positions= [(0, 0), (-20,0), (-40,0)]
all_segments =[]
for snake in range(3):
    snakes = Turtle()
    snakes.shape("square")
    snakes.color("white")
    snakes.penup()
    snakes.goto(positions[snake])
    all_segments.append(snakes)


screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # to follow where the head is going

    for segment in range(len(all_segments)-1, 0, -1):
        new_x = all_segments[(segment-1)].xcor()
        new_y = all_segments[(segment - 1)].ycor()
        all_segments[segment].goto(new_x, new_y)


all_segments[0].forward(20)
all_segments[0].left(90)



















# snake1 = Turtle()
# snake1.shape("square")
# snake1.color("white")
# snake1.goto(-20, 0)
#
# snake2 = Turtle()
# snake2.shape("square")
# snake2.color("white")
# snake2.goto(0, 0)
#
#
# snake3 = Turtle()
# snake3.shape("square")
# snake3.color("white")
# snake2.goto(20, 0)
#
#
#
screen.exitonclick()
