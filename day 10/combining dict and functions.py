def add(n1 , n2):
    return n1+n2

def sub(n1 , n2):
    return n1-n2

def mul(n1 , n2):
    return n1*n2

def div(n1 , n2):
    return n1/n2


operations ={
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

num1 = int(input("Enter your first number:" ))
num2 = int(input("Enter your second number:" ))

for operation in operations:
    print (operation)

oper = (input("Enter the operation you want to perform " ))

calc = operations[oper]

answer = calc(num1 , num2)
print(answer)
