# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

import random #always use this when we're going to use random numbers.

#Step 1: Introduction is a must for better understanding of the program.
print("Lottery winning numbers are out! Enter your three lucky numbers (0-9) and you might win P1,000,000!")

#Step 2: I used function for nonredundant codes.
def lottery():
    luckyNo1 = False 
    luckyNo2 = False
    luckyNo3 = False
    #The three lucky numbers of the user wil be false unless they are equal to the three lottery winning numbers.

    num1 = int(input("Your first lucky number: "))
    num2 = int(input("Your second lucky number: "))
    num3 = int(input("Your third lucky number: "))
    while len(str(num1)) != 1 or len(str(num2)) != 1 or len(str(num3)) != 1: #Loop for the three inputs of the user so the numbers are only ranging from 0-9 (or length of 1). Other integers will not be accepted.
        print("Wrong input.")
        num1 = int(input("Your first lucky number: "))
        num2 = int(input("Your second lucky number: "))
        num3 = int(input("Your third lucky number: "))
    #Step 3: Variables for the three random lottery numbers.
    lot1 = random.randint(0,9) 
    lot2 = random.randint(0,9)
    lot3 = random.randint(0,9)
    #Print the random lottery numbers.
    print("The lottery numbers are", lot1, lot2, lot3)

    if num1 == lot1 or num1 == lot2 or num1 == lot3:
        luckyNo1 = True 
    if num2 == lot1 or num2 == lot2 or num2 == lot3:
        luckyNo2 = True 
    if num3 == lot1 or num3 == lot2 or num3 == lot3:
        luckyNo3 = True 
    if luckyNo1 == True and luckyNo2 == True and luckyNo3 == True:
        print("Winner") #Display “Winner” if all 3 input numbers matched the generated numbers
    else:
        print("You loss") #Display ”You loss” if not

# Step 4: Another while loop so the user can try again if he/she lost. 
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.
tryAgain = "y"
while tryAgain == "y":
    lottery()
    tryAgain = input("Try again y/n: ")