score = 0

print("Welcome to the General Knowledge Quiz!")
print()

# Question 1
answer = input("1. What is the capital of France? ")

if answer.strip().lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Paris.")

# Question 2
answer = input("2. Which planet is known as the Red Planet? ")

if answer.strip().lower() == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Mars.")

# Question 3
answer = input("3. How many days are there in a week? ")

if answer.strip() == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 7.")

# Final score
print()
print(f"Your final score is: {score}/3")