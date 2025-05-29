# coffee machine program

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

Resourses = {
    "water": 500,
    "milk": 50,
    "coffee": 70,
    "money": 5.0
}


def latte(supplies):
    if int(supplies["water"]) < 200:
        print("not enough water")
    if int(supplies["milk"]) < 50:
        print("not enough milk")
    if int(supplies["coffee"]) < 25:
        print("not enough coffee")
    else:
        cost = 2.5
        water = 200
        milk = 50
        coffee = 25
        print("enter coins required _ ")
        quaters = int(input("enter quarters"))
        dimes = int(input("enter dimes"))
        nickel = int(input("enter nickels"))
        penny = int(input("enter penny's"))
        monetry_value = quaters * 0.25 + dimes * 0.1 + nickel * 0.05 + penny * 0.01
        if monetry_value < cost:
            print("not enough money")
        else:
           change = monetry_value - cost
           print(f"here is your change ${change.__round__()}")
           supplies["money"] += cost
           supplies["water"] -= water
           supplies["milk"] -= milk
           supplies["coffee"] -= coffee
           print("here is your latte :D ")


def cappuccino(supplies):
    if int(supplies["water"]) < 100:
        print("not enough water")
    if int(supplies["milk"]) < 24:
        print("not enough milk")
    if int(supplies["coffee"]) < 50:
        print("not enough coffee")
    else:
        cost = 2.0
        water = 100
        milk = 24
        coffee = 50
        print("enter coins required _ ")
        quaters = int(input("enter quarters"))
        dimes = int(input("enter dimes"))
        nickel = int(input("enter nickels"))
        penny = int(input("enter penny's"))
        monetry_value = quaters * 0.25 + dimes * 0.1 + nickel * 0.05 + penny * 0.01
        if monetry_value < cost:
            print("not enough money")
        else:
            change = monetry_value - cost
            print(f"here is your change ${change.__round__()}")
            supplies["money"] += cost
            supplies["water"] -= water
            supplies["milk"] -= milk
            supplies["coffee"] -= coffee
            print("here is your cappuccino :D ")


def espresso(supplies):
    if int(supplies["water"]) < 150:
        print("not enough water")
    if int(supplies["milk"]) < 30:
        print("not enough milk")
    if int(supplies["coffee"]) < 30:
        print("not enough coffee")
    else:
        cost = 1.5
        water = 150
        milk = 30
        coffee = 30
        print("enter coins required _ ")
        quaters = int(input("enter quarters"))
        dimes = int(input("enter dimes"))
        nickel = int(input("enter nickels"))
        penny = int(input("enter penny's"))
        monetry_value = quaters * 0.25 + dimes * 0.1 + nickel * 0.05 + penny * 0.01
        if monetry_value < cost:
            print("not enough money")
        else:
            change = monetry_value - cost
            print(f"here is your change ${change.__round__(
                
            )}")
            supplies["money"] += cost
            supplies["water"] -= water
            supplies["milk"] -= milk
            supplies["coffee"] -= coffee
            print("here is your cappuccino :D ")
coffee_machine = True
while coffee_machine:
    coffee_of_choice = input("“What would you like? (espresso/latte/cappuccino):")
    if coffee_of_choice == "OFF":
        coffee_machine = False
    if coffee_of_choice == "latte":
        latte(supplies=Resourses)
    elif coffee_of_choice == "cappuccino":
        cappuccino(supplies=Resourses)
    elif coffee_of_choice == "espresso":
        espresso(supplies=Resourses)
    elif coffee_of_choice == "report":
        print(Resourses)

