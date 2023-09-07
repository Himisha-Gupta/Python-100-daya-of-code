from turtle import Turtle, Screen

from random import random, choice

tim = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
for i in range(10):
    # ?steps = int(random() * 100)
    angle = int(random()* 360)
    tim.right(angle)
    tim.fd(10)
    tim.color(choice(colours))

screen = Screen()
screen.exitonclick()