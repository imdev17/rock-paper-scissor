import random

#1= Rock, 2= Paper, 3= Scissor

print("ROCK, PAPER & SCISSOR: \nThis is a 10 round game.")
play= input("Do you want to play(y/n): ")
choices = ('r','p','s')

computer_pts = 0
user_pts = 0
i = 0

while True:
    if play == "y":

        for i in range(1,11):
            i+=1
            num = random.randint(1,3)
            user_ans = input("Make your choice r/p/s: ").lower()
            if user_ans not in choices:
                    print("Invalid Input")

                #ROCK, num = 1
            if num == 1 and user_ans=="r":
                        print("Same Choice. Play again!")
            elif num == 1 and user_ans == "p":
                        print("Computer chose 🪨 and you chose 📃 \nYou Won!")
                        user_pts +=1
            elif num == 1 and user_ans == "s":
                        print("Computer chose 🪨 and you chose ✂️ \nComputer Won! ")
                        computer_pts +=1

                #PAPER, num = 2
            elif num == 2 and user_ans=="r":
                        print("Computer chose 📃 and you chose 🪨 \nComputer Won!")
                        computer_pts +=1
            elif num == 2 and user_ans == "p":
                        print("Same Choice. Play again!")
            elif num == 2 and user_ans == "s":
                        print("Computer chose 📃 and you chose ✂️ \nYou Won! ")
                        user_pts +=1

                #SCISSOR, num = 3
            elif num == 3 and user_ans=="r":
                        print("Computer chose ✂️ and you chose 🪨 \nYou Won!")
                        user_pts +=1
            elif num == 3 and user_ans == "p":
                        print("Computer chose ✂️ and you chose 📃 \nComputer Won!")
                        computer_pts +=1
            elif num == 3 and user_ans == "s":
                        print("Same choice. Play again!")
        break
            
    elif play == "n":
        print("Game Over")
        break
    print( "Your Score: ", user_pts , "& Computer Score: ", computer_pts)

print( "Your Score: ", user_pts , "& Computer Score: ", computer_pts)