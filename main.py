from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

off = False
coffee_menu = Menu()
coffee_machine = CoffeeMaker()
cash_machine = MoneyMachine()

while not off:
    selection = input("Please select a drink(espresso, latte, cappuccino): ").lower()

    if selection == "off":
        off = True
    elif selection == "report":
        coffee_machine.report()
        cash_machine.report()
    else:
        drink_check = coffee_menu.find_drink(selection)

        if drink_check:
            if coffee_machine.is_resource_sufficient(drink_check):

                payment = cash_machine.make_payment(drink_check.cost)
                if payment:
                    coffee_machine.make_coffee(drink_check)

                cash_machine.money_received = 0
