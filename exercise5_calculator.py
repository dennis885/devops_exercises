def calculator():
    num_calculations = 0

    while True:
        num_calculations += 1

        print("\n--- Calculator ---")
        print(f"Calculations: {num_calculations}")

        # Take user input for first number
        num1 = input("Enter the first number (or 'exit' to quit): ")

        if num1.lower() == "exit":
            break

        # Validate first number input
        if not num1.isdigit():
            print("Error: Invalid input. Only numbers allowed.")
            continue

        # Take user input for operation
        operation = input("Enter the operation (+, -, *, /): ")

        # Validate operation input
        if operation not in ['+', '-', '*', '/']:
            print("Error: Invalid operation.")
            continue

        # Take user input for second number
        num2 = input("Enter the second number: ")

        # Validate second number input
        if not num2.isdigit():
            print("Error: Invalid input. Only numbers allowed.")
            continue

        # Perform the calculation based on the operation
        num1 = float(num1)
        num2 = float(num2)

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2

        # Print the result
        print("Result:", result)

    print("\n--- Calculator Closed ---")
    print("Total calculations:", num_calculations)


# Run the calculator program
calculator()
