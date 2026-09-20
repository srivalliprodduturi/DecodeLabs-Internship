total = 0

while True:
    expense = input("Enter expense amount or 'quit' to finish: ")

    # Stop the loop
    if expense.lower() == "quit":
        break

    # Validate and convert input
    try:
        expense = float(expense)

        # Prevent negative expenses
        if expense < 0:
            print("Invalid expense. Please enter a positive amount.")
            continue

        # Accumulator
        total = total + expense

    except ValueError:
        print("Invalid input. Please enter a number or 'quit'.")

print(f"Total Spent: {total:.2f}")