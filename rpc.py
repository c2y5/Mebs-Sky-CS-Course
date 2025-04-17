from random import randint
import os, sys
scores = {
    "user": 0,
    "computer": 0
}

choices = ['rock', 'paper', 'scissors']
round = 0

def check(a, b):
    if a not in choices:
        return "Invalid choice!"
    
    global scores

    if a == b:
        return "You tied"
    
    if a == "rock" and b == "scissors":
        scores["user"] += 1
        return "You win!"
    
    if a == "rock" and b == "paper":
        scores["computer"] += 1
        return "You lose!"
    
    if a == "paper" and b == "rock":
        scores["user"] += 1
        return "You win!"
    
    if a == "paper" and b == "scissors":
        scores["computer"] += 1
        return "You lose!"
    
    if a == "scissors" and b == "paper":
        scores["user"] += 1
        return "You win!"
    
    if a == "scissors" and b == "rock":
        scores["computer"] += 1
        return "You lose!"
    
def main():
    global round, scores
    if round == 3:
        if scores["user"] > scores["computer"]:
            print("You win the game!")
        elif scores["user"] < scores["computer"]:
            print("You lost the game!")
        else:
            print("It's a tie!")
        
        round = 0
        scores = {
            "user": 0,
            "computer": 0
        }
        if input("\nDo you want to play again? (y/n): ").lower() == "y":
            os.system("cls")
            main()
        else:
            sys.exit(0)
    
    print(f"Round {round + 1}")
    while True:
        a = input("Rock, paper or scissors: ").lower()
        if a in choices:
            break
        print("Invalid choice!\n")

    b = choices[randint(0, 2)]
    print(f"Computer chose: {b}\n")
    print(check(a, b), "\n")
    round += 1

    main()

main()