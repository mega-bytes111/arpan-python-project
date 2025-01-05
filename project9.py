# Coffee Machine..virtual coffee machine that accepts coins
Menu = {
    "latte":{
      "ingredients":{
          "water": 200,
          "milk": 150,
          "coffee": 24
      },
      "cost":150
    },
    "espresso":{
      "ingredients":{
          "water": 50,
          "coffee": 18
      },
      "cost":100
    },
    "cappuccino":{
      "ingredients":{
          "water": 250,
          "milk": 100,
          "coffee": 24
      },
      "cost":200
    }
}
profit = 0
resources = {
    "water":500,#ml
    "milk":200,
    "coffee": 100
}
# check if enough resources is available..
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
# machine will only accepte 5,10 or 20rs coins..
def process_coins():
     print("Please insert coins : ")
     total = 0
     coin_five = int(input("How many 5rs coins?:"))
     coin_ten = int(input("How many 10rs coins?:"))
     coin_twenty = int(input("How many 20rs coins?:"))
     total = coin_five*5 + coin_ten*10 + coin_twenty*20
     return total
# check if payment is successful..
def is_paymet_successful(money_recieved,coffee_cost):
    if money_recieved>=coffee_cost:
         global profit
         profit+=coffee_cost
         change = money_recieved-coffee_cost   
         print(f"Here is your {change}Rs in change.")
         return True
    else:
         print("Sorry that's not enough money. Money refunded.")
         return False
def make_coffee(coffee_name,coffee_ingredients):
    for item in coffee_ingredients:
             resources[item]-=coffee_ingredients[item]
    print(f"Here is your {coffee_name} ☕..Enjoy!!")

is_on = True
while  is_on:
    choice = input("What would you like to have? (latte/espresso/cappuccino): ")
    if choice=='off':
        is_on = False

    elif choice=='report':
        print(f"Water={resources['water']}ml")
        print(f"Milk={resources['milk']}ml")
        print(f"coffee={resources['coffee']}g")
        print(f"Money=Rs{profit}")
    else:
        coffee_type = Menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
#   now machine ask to insert money
                payment = process_coins()
                if is_paymet_successful(payment,coffee_type['cost']):
                     make_coffee(choice,coffee_type['ingredients'])