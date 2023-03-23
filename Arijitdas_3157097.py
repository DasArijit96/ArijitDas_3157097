# To generate random number
import random
# To generate beep sound
import winsound
# To Calculate time
import time

print("Guess the Number Game!!!")
# generating a random number to guess
random_number = random.randint(1, 100)
# Initializing No_of_guess to keep track of no of guesses
No_of_guess = 1
# Initializing the start timer
start_time = time.time()
# Loop so that player can keep guessing until guessing the correct number
# Instruction for the game
print("Press q to quit the game at any moment")
print("Guess A number between 1 and 100: ")
while True:
    # Taking input from the user as a variable guess
    guess = input("My guess is : ")
    # Creating a quitting option for player at any moment
    if guess == 'q':
        break
    # Converting char to integer
    else:
        guess = int(guess)
    # Checking if the guessed number is correct or not
    if guess == random_number:
        # To create sound when there is right guess
        winsound.Beep(1000, 1000)
        print("You guessed the correct number and you needed {} guesses for guessing the right number".format(
            No_of_guess))
        # To get the end time when player guessed the correct number
        end_time = time.time()
        # To get the total time needed for the player to guess the number
        total = end_time - start_time
        # Round up the time to two decimal point
        total_time = round(total, 2)
        print("It took you {} seconds".format(total_time))
        if input("Press 'p' to Play or any other key to quit: ").lower() == 'p':
            print("\a")
            print("Guess A number between 1 and 100: ")
            # Generating new random number and refreshing everything for new game
            random_number = random.randint(1, 100)
            No_of_guess = 1
            start = time.time()
            continue
        else:
            # ending the game
            break
    # Checking if the guessed number is bigger or smaller
    elif guess > random_number:
        print("You have guessed a higher number.Guess lower!!!")
        # To create sound when there is a wrong guess
        winsound.Beep(500, 300)
    # Checking if the guessed number is bigger or smaller
    elif guess < random_number:
        print("You have guessed a lower number.Guess higher!!!")
        # To create sound when there is a wrong guess
        winsound.Beep(500, 300)
    No_of_guess += 1
