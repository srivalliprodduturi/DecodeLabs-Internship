import string
import secrets

# Get password length from user
try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Password length must be greater than 0.")

    else:
        # Character pool
        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        # Generate secure random password
        password = ''.join(
            secrets.choice(characters)
            for _ in range(length)
        )

        print("Generated Password:", password)

except ValueError:
    print("Invalid input! Please enter a number.")