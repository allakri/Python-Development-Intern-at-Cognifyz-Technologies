import random

# Task: Number Guesser
# Create a number guessing game where the program generates a random number
# between a specified range, and the user tries to guess it.
# Provide feedback to the user if their guess is too high or too low.

def number_guesser():
    # Get the lower and upper bounds from the user
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))
    
    # Generate a random number within the given range
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0
    
    print("Welcome to the Number Guesser Game!")
    print(f"I've selected a number between {lower_bound} and {upper_bound}. Try to guess it!")
    
    while True:
        try:
            # Get user's guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if the guess is within the valid range
            if user_guess < lower_bound or user_guess > upper_bound:
                print(f"Please enter a number between {lower_bound} and {upper_bound}.")
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
    number_guesser()