import random
import string

def generate_strong_password(password_length, complexity_level):
    if complexity_level == "1":
        allowed_characters = string.ascii_letters
    elif complexity_level == "2":
        allowed_characters = string.ascii_letters + string.digits
    elif complexity_level == "3":
        allowed_characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level choice"

    generated_password = ''.join(random.choice(allowed_characters) for _ in range(password_length))
    return generated_password

try:
    desired_length = int(input("Enter the desired length of the password: "))
    if desired_length <= 0:
        print("Password length should be greater than 0.")
    else:
        print("Select complexity level:")
        print("1. Alphanumeric (letters only)")
        print("2. Alphanumeric (letters and numbers)")
        print("3. Complex (letters, numbers, and symbols)")

        complexity_choice = input("Enter complexity level choice (1/2/3): ")

        password = generate_strong_password(desired_length, complexity_choice)

        if password != "Invalid complexity level choice":
            print(f"Generated Password: {password}")
except ValueError:
    print("Invalid input. Please enter a valid length (a positive integer).")
