# payment methods, floats <-
penny = 0.01
dime = 0.10
nickel = 0.05
quarter = 0.25

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
# TODO this is now 2
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#TODO create a cost counter using the payment methods above
### after seeing the walkthrough version I see it could've been done a lot quicker and cleaner
def total_cost():
    print("Please insert coins")
    nickel_multi = int(input("How many nickels do you want to insert? ").lower())
    nickel_total = nickel * nickel_multi
    penny_multi = int(input("How many pennys do you want to insert? ").lower())
    penny_total = penny * penny_multi
    dime_multi = int(input("How many dimes do you want to insert? ").lower())
    dime_total = dime * dime_multi
    quarter_multi = int(input("How many quarters do you want to insert? ").lower())
    quarter_total = quarter * quarter_multi

    total_costing = nickel_total + penny_total + dime_total + quarter_total
    return total_costing


# TODO make it function to check if transaction is successful.

def is_transaction_succesfull(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Here is a refund.")
        return False


# step def coffee_machine

# TODO: create the calcuation for the types of coffees
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


# TODO 2, to ensure that there this will be checked before every order

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO 5 put it all in a flowing function def coffee machine

is_on = True
while is_on:
    choice = input("What type of coffee would you like? espresso/latte/cappuccino: ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = total_cost()
            if is_transaction_succesfull(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
