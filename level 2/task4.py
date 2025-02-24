# Task: Fibonacci Sequence

# Write a Python function that generates the
# Fibonacci sequence up to a given number of
# terms. The function should take an integer
# input from the user and display the
# Fibonacci sequence up to that number of
# terms.

def fibonacci_sequence(n):
    """
    Generates the Fibonacci sequence up to n terms.
    :param n: Number of terms to generate
    """
    if n <= 0:
        print("Please enter a positive integer.")  # Validate input
        return
    
    sequence = [0, 1]  # Initialize the sequence with the first two Fibonacci numbers
    
    # Generate the Fibonacci sequence
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])  # Add the last two numbers in the sequence
    
    print("Fibonacci Sequence:", sequence[:n])  # Print the sequence up to n terms

if __name__ == "__main__":
    try:
        # Take user input for the number of terms
        num_terms = int(input("Enter the number of terms: "))
        fibonacci_sequence(num_terms)  # Call the function to generate the sequence
    except ValueError:
        print("Invalid input! Please enter a positive integer.")  # Handle invalid input



# solution
# Enter the number of terms: 5
# Fibonacci Sequence: [0, 1, 1, 2, 3]