# Simple Calculator

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        # Take operation input
        choice = int(input("Enter the number corresponding to the operation (1/2/3/4): "))

        # Check for valid operation
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please select a valid operation.")
            return

        # Take two numbers as input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the selected operation
        if choice == 1:
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")
        elif choice == 2:
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")
        elif choice == 3:
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
        elif choice == 4:
            # Handle division by zero
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is: {result}")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

# Run the calculator
calculator()
