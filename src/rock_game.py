#import module we need
import random

def rock_paper_scissor_game():
    #initialize amount of wins   
    wins = 0

    #gamplay loop
    for i in range(3):
        stranger = 3      # random.randint(1,3)
        user = int(input("[1] Rock  [2] Paper   [3] Scissors    [9] Quit\n"))
        #user chooses ROCK
        if user == 1:
            if stranger == 1:
                print("Stranger chose rock...tie!")
            elif stranger == 2:
                print("Stranger chose paper...Stranger wins :(")
            else:
                print("Stranger chose scissors...you wins :)")
                wins += 1

        #user chooses PAPER
        elif user == 2:
            if stranger == 1:
                print("Stranger chose rock...you win :)")
                wins += 1
            elif stranger == 2:
                print("Stranger chose paper...tie!")
            else:
                print("Stranger chose scissors...Stranger wins :(")
        
        #user chooses SCISSORS
        elif user == 3:
            if stranger == 1:
                print("Stranger chose rock...Stranger wins :(")
            elif stranger == 2:
                print("Stranger chose paper...you win :)")
            else:
                print("Stranger chose scissors...tie!")
        elif user == 9:
            break
        else:
            print("What are you doing?")
            user = int(input("[1] Rock  [2] Paper   [3] Scissors    [9] Quit\n"))
        #print updated stats
        print("Wins: %s ot of 3 tries" % (wins))

    if wins == 3:
        return True
    else:
        return False

