print("--------WELCOME TO THE GUESSING GAME--------")
user = int(input("Enter a range (from 1 to __) for the guessing game: "))
import random
num = random.randint(1,user)
guess = False
while guess == False:
    user_guess = int(input("Guess a number from 1 to " + str(user) + ": "))
    if user_guess == num:
        print("You guessed the right number!")
        print("Congratulations you won the game!")
        guess= True
    elif user_guess<num:
        print("Your guess is too low, try higher!")
    elif user_guess > num: 
        print("Your guess is too high, try lower!")

print("--------THANK YOU FOR PLAYING THE GUESSING GAME--------")