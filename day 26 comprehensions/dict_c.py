import random

# new_dict1 = {key: value for (key , value) in dict.items()}

names = ["Hailey" , "Maes" , "Beth" , "Care" , "Torry" , "Eleanor"]

#new_dict = {key: value for item in names}

new_dict = {item: random.randint(1, 100) for item in names}
print(new_dict)

new_dict1 = {key: value for (key , value) in new_dict.items() if value >= 60}
print(new_dict1)
