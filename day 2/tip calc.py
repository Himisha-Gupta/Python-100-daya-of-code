import math

print("welcome to tip calculator")
amount = int(input("what is the amount of bill "))
tip = int(input("how much tip you want to give "))
total_amount = amount + ((tip/100)* amount)
print(total_amount)
num_of_people = int(input("in how many people you want to split the bill "))
each_person = str(total_amount/ num_of_people)
print("each person has to pay " + each_person)