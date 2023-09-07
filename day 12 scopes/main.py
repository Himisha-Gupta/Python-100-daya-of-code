################### Scope ####################

# enemies = 1
#
# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

#######################Local Scope ################
#exists within the fucntion




############################# Modify Global Variable

enemies = 1

def increase_enemies():
  global enemies
  enemies += 2        #modified global variable to use into functions  avoid this
  print(f"enemies inside function: {enemies}")

  return enemies +1   #use this instead
increase_enemies()
print(f"enemies outside function: {enemies}")



################Global constants    in uppercase
PI = 3.14