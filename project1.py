# Rock Paper Scissors..Game in python..
# 0 for rock 1 for paper and 2 for scissor
import random
import rockpapersc

user_choice = int(input("Enter your choice :Type 0 for rock,1 for paper,2 for scissor :"))#input lenge
comp_choice = random.randint(0,2)#computer generate
print("user_choice =",user_choice)
print("comp_choice =",comp_choice)
if  user_choice>2 or user_choice<0:
    print("Invalid input and you lose")
elif user_choice==0 and comp_choice==2:
    print(rockpapersc.items[2])
    print("You Win")
elif user_choice==2 and comp_choice==0:
    print(rockpapersc.items[2])
    print("Computer Win")
elif comp_choice>user_choice:
    print(rockpapersc.items[comp_choice])
    print("Computer Win")
elif user_choice>comp_choice:
    print(rockpapersc.items[user_choice])
    print("You Win")   
else:
    print("It's Draw")         