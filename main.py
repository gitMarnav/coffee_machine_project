from menu import MENU, resources, coin_value
from art import logo, thank_you, menu, boom
import os

earning = 0


def report():
    for keys in resources:
        print(f"{keys.title()}: {resources[keys]}")
    print(f"Today's earning: {earning}")


def check_resources(customer_input):
    ingredients = MENU[customer_input]["ingredients"]
    for keys in ingredients:
        if ingredients[keys] > resources[keys]:
            print(f"Sorry there is not enough {keys}.")
            print(f"{thank_you}  \ LimitedCoffee Services Ltd.")
            quit()


def process_coins(quarters, dimes, nickle, pennies):
    cost = MENU[customer_input]["cost"]
    payment = (coin_value["quarter"]*quarters + coin_value["dime"] *
               dimes + coin_value["nickle"]*nickle+coin_value["penny"]*pennies)
    if payment > cost:
        print(f"Here is ${(payment - cost):.2f} in change.")
    elif payment < cost:
        print("Sorry that's not enough money. Money refunded.")
        print(f"{thank_you}  \ LimitedCoffee Services Ltd.")
        quit()
    else:
        print("Thank you for paying.")
    global earning
    earning += cost


def process_resource(customer_input):
    ingredients = MENU[customer_input]["ingredients"]
    for keys in ingredients:
        resources[keys] -= ingredients[keys]


off = False
print(logo)
print(menu)
while not off:
    customer_input = input(
        "\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    if customer_input not in ["espresso", "latte", "cappuccino", "report", "off"]:
        os.system('cls')
        print("Invalid Input !!\nSystem Crash 💥")
        print(boom)
        quit()
    elif customer_input == "report":
        report()
        continue
    elif customer_input == "off":
        off = True
        os.system('cls')
        print(f"{thank_you}  \ LimitedCoffee Services Ltd.")
    else:
        check_resources(customer_input)
        process_resource(customer_input)
        print("\nPlease insert coins.")
        quarters = int(input(f"How many quarters?: "))
        dimes = int(input(f"How many dimes?: "))
        nickle = int(input(f"How many nickle?: "))
        pennies = int(input(f"How many pennies?: "))
        process_coins(quarters, dimes, nickle, pennies)

        print(f"Here is your {customer_input} ☕ Enjoy !!")
