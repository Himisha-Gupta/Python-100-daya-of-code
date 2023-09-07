from turtle import *
import heroes
#will import everything

jimmy = Turtle()
jimmy.shape("turtle")
jimmy.color("pink")


#------------------------------------ For creating a square ------------------------------------------
#Method 1
jimmy.forward(100)
jimmy.left(90)
jimmy.forward(100)
jimmy.left(90)
jimmy.forward(100)
jimmy.left(90)
jimmy.forward(100)

#------------------------------------ For creating a square ------------------------------------------
#Method 2
# def turn():
#     jimmy.forward(100)
#     jimmy.left(90)
#
# turn()
# turn()
# turn()
# turn()

#------------------------------------ For creating a square ------------------------------------------
#Method 3
#
# for _ in range(4):
#     jimmy.forward(100)
#     jimmy.left(90)




print(heroes.gen())





my_screen = Screen()
print(my_screen.exitonclick())