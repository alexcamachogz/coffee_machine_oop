from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while True:
    drink_options = menu.get_items()[:-1]
    option_selected = input(f"What would you like? ({drink_options}): ")
    drink = menu.find_drink(option_selected)

    if option_selected == "off":
        print("Coffe machine is turn off! Goodbye.")
        break
    elif option_selected == "report":
        coffee_maker.report()
        money_machine.report()
    elif drink:
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else:
        print("Please try again.")
