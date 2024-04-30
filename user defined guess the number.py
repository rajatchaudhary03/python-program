import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    print("I have selected a number between 1 and 100. Let's see if you can guess it!")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

# Run the game
guess_the_number()
