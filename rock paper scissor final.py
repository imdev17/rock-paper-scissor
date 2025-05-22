import random

option = ("r", "s", "p")
emoji = { "r":'🪨', "p": '📃', "s":'✂️' }
computer_pts = 0
user_pts = 0
tie = 0

print ("ROCK, PAPER & SCISSOR: This is a 10 round rock, paper, scissor game with a integrated " \
        "point system in which you'll get 0 points on losing a game and 1 point after winning each game. \n")
play = input("Do you wan to play? (y/n): ")

for i in range(0,10):   
    if play == "y":
        user_ans = input("Rock, Paper or Scissor? (r/p/s): ").lower()
        if user_ans not in option:
            print("Invalid Option")
            continue
        bot_ans = random.choice(option)

        if bot_ans == user_ans:
            print("Tie")
            tie +=1
        elif ( bot_ans == "r" and user_ans == "p" or
            bot_ans == "s" and user_ans == "r" or
            bot_ans == "p" and user_ans == "s"      
            ):
            print("You Won!")
            user_pts +=1
        else :
            print("Computer Won!")
            computer_pts +=1
    elif play == "n":
        print("Thanks for Playing!")
        break

    elif play !="y" or play != "n":
        print("Invalid Input")
        break
    print(f'You chose{emoji[user_ans]}  & Computer chose{emoji[bot_ans]}')
print("Your Score: ", user_pts, "Computer Score: ", computer_pts, "Tie: ",tie)
