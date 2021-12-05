# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

import random 
#Step 1: Generate 1 random number from 0-100.
guessNo = random.randint(0,100)
#Step 2: Ask the user to guess the number.
userNo = int(input("Guess the random number from 0-100: "))
#while loop: for the repetition of asking the user until he guessed the random number correctly.
while userNo != guessNo:
    if userNo > guessNo:
        print(userNo, "is greater than the random number.") #Step 3: Display greater than if the inputed number is > random number.
    if userNo < guessNo:
        print(userNo, "is less than the random number.") #Step 4: Display less than if the inputed number is < random number.
    userNo = int(input("Try again. Guess the random number 0-100: "))
print("You guessed it right! The random number is", guessNo) #To break the loop, keep asking the user until he guessed the random number correctly.