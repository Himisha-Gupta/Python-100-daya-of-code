import math

height = float(input("What is your height?"))
weight = float(input("What is your weigth?"))

bmi = (weight / (height ** 2))

print(f'your bmi is {bmi}')