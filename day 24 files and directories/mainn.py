#------------------------------------- reading a file ------------------------------


file = open(r"C:\Users\Himisha\OneDrive\Desktop\my_file.txt")
content = file.read()
print(content)
file.close()

      #----------------without closing file---------------
# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)


#---------------------------------------- writing a file ------------------------------
# with open("new_file.txt" , mode ="w") as file:
#
#     file.write("Another line")
#
# # this will delete everythng in the file and add given text
# # if you write a file that doesnt exist that will create a new file




#---------------------------------------- appending a file ------------------------------
# with open("my_file.txt" , mode ="a") as file:
#
#     file.write("\nAnother line")
#
# # this will add given text to the file

