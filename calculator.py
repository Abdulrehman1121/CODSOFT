# Function to perform addition
def perform_addition(x, y):
    return x + y

# Function to perform subtraction
def perform_subtraction(x, y):
    return x - y

# Function to perform multiplication
def perform_multiplication(x, y):
    return x * y

# Function to perform division
def perform_division(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Get user input for two numbers and the operation choice
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation_choice = input("Enter choice (1/2/3/4): ")

    if operation_choice not in ('1', '2', '3', '4'):
        print("Invalid choice")
    else:
        if operation_choice == '1':
            result = perform_addition(number1, number2)
            operation = "+"
        elif operation_choice == '2':
            result = perform_subtraction(number1, number2)
            operation = "-"
        elif operation_choice == '3':
            result = perform_multiplication(number1, number2)
            operation = "*"
        else:
            result = perform_division(number1, number2)
            operation = "/"

        print(f"{number1} {operation} {number2} = {result}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
