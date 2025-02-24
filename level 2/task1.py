import random

# Task: Guessing Game
# Write a Python program that generates a random number between 1 and 100.
# The user should then try to guess the number.
# The program should provide hints such as "too high" or "too low"
# until the correct number is guessed.

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Guessing Game!")
    print("I've selected a number between 1 and 100. Try to guess it!")
    
    while True:
        try:
            # Get user's guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if the guess is within the valid range
            if user_guess < 1 or user_guess > 100:
                print("Please enter a number between 1 and 100.")
            # Provide feedback if the guess is too low
            elif user_guess < number_to_guess:
                print("Too low! Try again.")
            # Provide feedback if the guess is too high
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            # Correct guess
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            # Handle invalid (non-numeric) input
            print("Invalid input! Please enter a valid number.")

# Run the game if the script is executed directly
if __name__ == "__main__":
    guessing_game()
