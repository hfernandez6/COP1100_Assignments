#Hugo Fernandez
#COP1000 - Program 1
#5/18/2022
###########################
#Write a Program

#1. Set up your driver loop
#2. Set up your print name function
#3. Call your print name function
#4. Write a program to accept a user’s name and a  number
#IF the number is > 10 – Say “You Win xxxx”
#if the number is <=10 – Say “You Lose xxxx”
#xxxx is the user’s name

print ("Do you want to play a game?")
game = int(input("Enter 1 for yes, 0 for no?\n" ))

if(game == 1):
    name = input("What is your name?\n")
    number = int(input("What number do you pick?\n"))
    if (number>10):
        print ("You win:", name)
    elif (number<=10):
        print ("You lose", name)
    else:
        print("Something went wrong")
else:
    print ("Thanks for playing")