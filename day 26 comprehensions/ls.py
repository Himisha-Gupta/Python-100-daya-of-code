# LIST COMP.

# numbers = [1,2,3,4,5]
#
# new_list = [n+1  for n in numbers]
# print(new_list)
#
# range = [n*2 for n in range(1, 5)]
# print(range)

#CONDITIONAL LIST COMP.

# new = [n*2 for n in range(1,6) if n%2 == 0]
# print(new)

names = ["Hailey" , "Maes" , "Beth" , "Care" , "Torry" , "Eleanor"]
name = [name.upper() for name in names if len(name)>5]
print(name)