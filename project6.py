# Making a calculator..in python..using concept of Recursion in python..WOW!!!
import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b
# creating a dictionary containing symbols                
operations_dict = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    num1 = float(input("Enter the first number :"))
    for symbol in operations_dict:
        print(symbol)

    continue_flag = True
    while  continue_flag:
        op_symbol = input("Pick an operation :")#act as key values
        num2 = float(input("Enter the second number :"))   

        calculator_fun = operations_dict[op_symbol]#function
        output = calculator_fun(num1,num2)
        print(f"{num1} {op_symbol} {num2} = {output}")

        should_continue = input(f"Enter 'y' to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit : ").lower()

        if should_continue=='y':
            num1 = output

        elif should_continue=='n':
            continue_flag = False
            os.system('cls')#as we want new claculation
            calculator()

        elif should_continue=='x':
            continue_flag = False   
            print("Bye") 

calculator()            
