# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmii = (round((weight/(height**2))))
bmi = str(round((weight/(height**2))))
if bmii<18.5:
    print("Your BMI is "+ bmi +", you are underweight.")
elif bmii> 18.5 and bmii<25:
    print("Your BMI is "+ bmi +", you have a normal weight.")
elif bmii>25 and bmii< 30:
    print("Your BMI is "+ bmi +", you are slightly overweight.")
elif bmii>30 and bmii< 35:
    print("Your BMI is "+ bmi +", you are obese.")
else:
    print("Your BMI is "+ bmi +", you are clinically obese.")