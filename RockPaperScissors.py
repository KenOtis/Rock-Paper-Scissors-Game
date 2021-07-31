import random
import time

def main():
    a=["rock","paper","scissors"]
    go="yes"
    print("\nLets play Rock, Paper, Scissors! \nBest of 3 wins.")
    computer=0
    user=0
    while (computer<2 or user<2 ):
        b=(random.choice(a))
        choice=input("Your choice: ")
        time.sleep(2)
        print ("Computer choice: ",b,"\n")
        if choice == "rock":
            if b== "scissors":
                user+=1
                print ("You win!\n")
            if b== "paper":
                computer+=1
                print ("Computer wins!\n")
        
        if choice == "scissors":
            if b== "paper":
                computer+=1
                print ("Computer Wins!\n")
            if b== "rock":
                user+=1
                print ("You wins!\n")
        
        if choice == "paper":
            if b== "scissors":
                user+=1
                print ("You win!\n")
            if b== "rock":
                computer+=1
                print ("Computer wins!\n")

        if choice == b:
            print ("Tie! no one gets a point.\n")

        if computer>2:
            print ("Computer Won!\nThanks for playing!")
            break

        if user>2:
            print("You win!\nThanks for playing!")
            break

main()