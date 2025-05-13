def add_two_numbers():
    try:
        # Take input from the user
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        # Convert the inputs to floats (you can use int() if you only need integers)
        num1 = float(num1)
        num2 = float(num2)

        # Calculate the sum
        result = num1 + num2

        # Print the result
        print(f"The sum of {num1} and {num2} is {result}")

    except ValueError:
        print("Invalid input. Please enter numerical values.")

# Call the function to execute the addition
add_two_numbers()
