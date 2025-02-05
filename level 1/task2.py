# Task: Temperature Conversion

# Create a Python program that converts
# temperatures between Celsius and
# Fahrenheit. Prompt the user to enter a
# temperature value and the unit of
# measurement, and then display the
# converted temperature.

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32  # Formula for conversion

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9  # Formula for conversion

# Main function to handle user input and perform conversion
def convert_temperature():
    try:
        print("Welcome to the Temperature Converter!")  # Welcome message

        # Prompt user for temperature value
        temp = float(input("Please enter the temperature value: "))

        # Prompt user for the unit of measurement
        unit = input("Please specify the unit of measurement (C for Celsius, F for Fahrenheit): ").strip().upper()

        # Check the unit and perform the appropriate conversion
        if unit == 'C':
            converted = celsius_to_fahrenheit(temp)
            print(f"{temp}°C is equal to {converted:.2f}°F")  # Display converted temperature
        elif unit == 'F':
            converted = fahrenheit_to_celsius(temp)
            print(f"{temp}°F is equal to {converted:.2f}°C")  # Display converted temperature
        else:
            # Handle invalid unit input
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        # Handle invalid temperature input
        print("Invalid temperature value. Please enter a numeric value.")

# Example usage
convert_temperature()  # Calling the function to start the program
