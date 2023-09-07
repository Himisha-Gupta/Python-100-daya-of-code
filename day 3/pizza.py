print("Welcome to Himisha's Pizza!")
size = input("S M or L")


price = 0

if size == "S":
    price += 15
elif size == "M":
    price += 20
else:
    price +=25


pepperoni = input("Y or N")
if pepperoni == "Y":
    if size == "S":
        price+= 2
    else:
        price+= 3
else:
    price += 0

cheese = input("Y or N")
if cheese == "Y":
    price += 1

pricew= str(price)
print("Your Final bill is " + pricew)