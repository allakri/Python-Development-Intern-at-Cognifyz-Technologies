"""Task: Calculator Program

Create a Python program that acts as a basic
calculator. It should prompt the user to
enter two numbers and an operator (+
, -,
*
, /,
%), and then display the result of the
operation."""



def calculator():
    # Ask user for input
    num1 = float(input("Enter the first number: "))
    operator = input("Enter operator (+, -, *, /, %): ")
    num2 = float(input("Enter the second number: "))

    # Perform the operation based on the operator entered
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error! Division by zero."
    elif operator == "%":
        result = num1 % num2
    else:
        return "Invalid operator!"

    # Display the result
    return f"The result of {num1} {operator} {num2} is: {result}"

# Call the calculator function and print the result
print(calculator())
