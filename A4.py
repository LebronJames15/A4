


print("Welcome to the Simple Calculator!")
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
while True:
        # Take input from the user
        choice = input("Enter choice (1, 2, 3, 4): ")

        # Check if the choice is valid
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"The result is: {num1 + num2}")
                elif choice == '2':
                    print(f"The result is: {num1 - num2}")
                elif choice == '3':
                    print(f"The result is: {num1 * num2}")
                elif choice == '4':
                    if num2 == 0:
                        print("Error: Division by zero is not allowed.")
                    else:
                        print(f"The result is: {num1 / num2}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        else:
            print("Invalid choice.")

