"""
Sep 8 2023

Simple rock paper or scissors game aganist the computer in python
Computer will randomly pick between rock, paper and scissors, and depending on that the user will either win or lose
"""

import random
  
print("Rock, Paper, or Scissors!")
won = 0
gameOver = False
while gameOver == False:
    
    userChoice = input("Enter rock, paper, or scissors(or exit): ")
    userChoice = userChoice.lower()

    if userChoice == "paper":
        userChoice = "p"
    elif userChoice == "rock":
        userChoice = "r"
    elif userChoice == "scissors" or userChoice == "scissor":
        userChoice = "s"
    elif userChoice == "exit" or userChoice == "e":
        userChoice = "e"
    #else:
        
    rps = ["Rock", "Paper", "Scissors"]
    computerChoice = random.choice(rps)

    if (((userChoice == "r" and computerChoice == "Scissors") or (userChoice == "s" and computerChoice == "Paper")) or (userChoice == "p" and computerChoice == "Rock")):
        print("Computer choose: ", computerChoice)
        won = 1 + won
        print("you won!!!")

    elif (userChoice == "s" and computerChoice == "Scissors") or (userChoice == "p" and computerChoice == "Paper") or (userChoice == "r" and computerChoice == "Rock"):
        print("Computer choose: ", computerChoice)
        print("tie")
       
        
    elif not(userChoice == "p" or userChoice == "r" or userChoice == "s" or userChoice == "e"):
        print("invaild")


    elif userChoice == "e":
        print("Bye")
        gameOver = True
        
    else :
        print("Computer choose: ", computerChoice)
        print("u lost")
      
print("You won", won ,"times")
    
