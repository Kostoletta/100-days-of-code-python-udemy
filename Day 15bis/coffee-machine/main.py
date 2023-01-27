from menu import MENU, resources

money = 0


def report():
    """Print levels of water, milk, coffee and amount of money"""
    # Water: 300ml
    # Milk: 200ml
    # Coffee: 100g
    # Money: $1.5
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print("Money: ${:.2f}".format(money))


def ask_money(cost) -> int:
    total = 0
    # how many quarters?: 0
    # how many dimes?: 0
    # how many nickles?: 0
    # how many pennies?: 0
    total += int(input(">How many quarters?: ")) * 0.25
    total += int(input(">How many dimes?: ")) * 0.10
    total += int(input(">How many nickles?: ")) * 0.05
    total += int(input(">How many pennies?: ")) * 0.01
    if total >= cost:
        global money
        money += total
        return total - cost
    else:
        print("Sorry that's not enough money. Money refunded.")
        return -1


def subtract_resources(ingredients):
    resources["water"] -= ingredients["water"]
    resources["milk"] -= ingredients["milk"]
    resources["coffee"] -= ingredients["coffee"]


def make_beverage(beverage, choice):
    # check if there is enough resources for that beverage
    if beverage["ingredients"]["water"] > resources["water"]:
        print(">Sorry there is not enough water.")
        return
    elif beverage["ingredients"]["milk"] > resources["milk"]:
        print(">Sorry there is not enough milk.")
        return
    elif beverage["ingredients"]["coffee"] > resources["coffee"]:
        print(">Sorry there is not enough coffee.")
        return
    else:
        change = ask_money(beverage["cost"])
        if change >= 0:
            subtract_resources(beverage["ingredients"])
            if change > 0:
                print("Here is ${:.2f} in change.".format(change))
            print(f"Here is your {choice} ☕️. Enjoy!")


def serve():
    work = True
    while work:
        choice = input(">What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            work = False
        elif choice == "report":
            report()
        elif choice in MENU:
            make_beverage(MENU[choice], choice)
        else:
            print(">Type a valid input please")


serve()
