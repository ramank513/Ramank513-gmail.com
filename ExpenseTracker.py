# Simple Personal Expense Tracker

expenses = {}

print("--- Welcome to your Python Expense Tracker ---")

while True:
    print("\nOptions: [1] Add Expense [2] Show Summary [3] Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        category = input("Enter category (e.g., Food, Rent, Fun): ").capitalize()
        try:
            amount = float(input(f"How much did you spend on {category}? "))
            
            # Add to existing category or create a new one
            if category in expenses:
                expenses[category] += amount
            else:
                expenses[category] = amount
            print(f"Added ${amount:.2f} to {category}.")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    elif choice == '2':
        print("\n--- Current Spending Summary ---")
        if not expenses:
            print("No expenses recorded yet.")
        else:
            total = sum(expenses.values())
            for cat, amt in expenses.items():
                print(f"{cat}: ${amt:.2f}")
            print(f"---------------------------")
            print(f"TOTAL SPENT: ${total:.2f}")

    elif choice == '3':
        print("Goodbye! Happy saving.")
        break
    else:
        print("Invalid choice. Please pick 1, 2, or 3.")
