# Higher lower game..
import random
import gamedatabase
import logo_hi_lo
import os

print(logo_hi_lo.game_logo)

score = 0
def display_accountinfo(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name},a {description},from {country}"
def check_answer(guess,follower_1,follower_2):
    if follower_1<follower_2:
        if guess==1:
            return False
        else:
            return True

    else:
        if guess==1:
            return True
        else:
            return False
account_2 = random.choice(gamedatabase.data)

continue_flag = True        
while continue_flag:
    account_1 = account_2
    account_2 = random.choice(gamedatabase.data) 
    # tab tak generate kro jab tak different na ho jaye..
    while account_1==account_2:
        account_2 = random.choice(gamedatabase.data)

    print(f"Compare 1:{display_accountinfo(account_1)}")
    print(logo_hi_lo.vs)
    print(f"Compare 2:{display_accountinfo(account_2)}")

    guess = int(input("Who has more follower? Type 1 or Type 2 : "))

    follower_count_1 = account_1["follower_count"]
    follower_count_2 = account_2["follower_count"]

    is_correct = check_answer(guess,follower_count_1,follower_count_2)

    os.system('cls')
    print(logo_hi_lo.game_logo)

    if is_correct==True:
        score+=1
        print(f"You are right.Your score is : {score}")

    else:
        continue_flag = False
        print(f"You are wrong.Your final score is : {score}")
    