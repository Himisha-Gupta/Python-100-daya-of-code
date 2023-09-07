#attributes :- variables       what it has
#methods:- function             what it does

#    package       class
from turtle import Turtle , Screen

#object class
timmy = Turtle()
my_screen = Screen()
# timmy is a object of classs Turtle

#object attribute
timmy.shape("turtle")
timmy.color("black")
# timmy.forward(100)
print(my_screen.canvheight)
print(my_screen.canvheight)

#object   methods
my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
table.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769])
table.align = "c"
print(table)
