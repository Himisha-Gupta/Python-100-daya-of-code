# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
remaining_years = 90 - int(age)


in_weeks = str(int(remaining_years) * 52)

in_days = str(int(remaining_years) * 365)


in_months = str(int(remaining_years)* 12)


print("You have " + in_days + " days, " + in_weeks+ " weeks, "+ "and " + in_months+ " months left.")