# Requirments
# file:///C:/Users/Himisha/Downloads/Coffee+Machine+Program+Requirements.pdf

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def resource_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True
def is_resource_suff(resources , order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print("Here is your")
def operate_coins():
    print("insert coins.")
    totAL = int(input("Enter the quaterss"))*0.25
    totAL += int(input("Enter the dimes")) * 0.10
    totAL += int(input("Enter the nickels")) * 0.05
    totAL += int(input("Enter the pennie")) * 0.01
    # print(totAL)
    return totAL
#quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f'Water: {resources["water"]} ml')
        print(f'Milk: {resources["milk"]} ml')
        print(f'Coffee: {resources["coffee"]} ml')
        print(f'Money = ${profit}')
    else:
        drink = MENU[choice]
        print(drink)
        if resource_sufficient(drink["ingredients"]):
            payment = operate_coins()
            if payment<drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif payment>drink["cost"]:
                change = payment - drink["cost"]
                print(f"here is {change} your change")
                profit += drink["cost"]

