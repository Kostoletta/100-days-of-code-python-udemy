from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
menu = Menu()
mm = MoneyMachine()


def do_report():
    cm.report()
    mm.report()


work = True
while work:
    choice = input(f">What would you like? ({menu.get_items()}): ").lower()
    if choice == "off":
        work = False
    elif choice == "report":
        do_report()
    else:
        drink = menu.find_drink(choice)
        if drink is not None and cm.is_resource_sufficient(drink) and mm.make_payment(drink.get_cost()):
            cm.make_coffee(drink)
