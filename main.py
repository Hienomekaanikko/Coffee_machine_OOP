from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menuitem = MenuItem("name", "water", "milk", "coffee", "cost")
menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
machine_on = True
#ask what would the customer want

while machine_on:
    order_name = input(f"What would you like to have? {menu.get_items()}: ")
    if order_name == "report":
        coffeemaker.report()
    elif order_name == "off":
        machine_on = False
    else:
        drink = menu.find_drink(order_name)

    #check resources
        if coffeemaker.is_resource_sufficient(drink) == True:
            payment = moneymachine.make_payment(drink.cost)
            if payment == True:
                coffeemaker.make_coffee(drink)
                moneymachine.report()
        else:
            print("Ingredients are insufficient")
