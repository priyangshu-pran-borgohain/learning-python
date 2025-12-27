FILE_NAME = "expenses.txt"

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food, Travel, etc): ")
    amount = input("Enter amount: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{category},{amount}\n")

    print("Expense added successfully!\n")

def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            print("\nDate | Category | Amount")
            print("--------------------------")
            for line in file:
                date, category, amount = line.strip().split(",")
                print(f"{date} | {category} | {amount}")
            print()
    except FileNotFoundError:
        print("No expenses found.\n")

def total_expense():
    total = 0
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                _, _, amount = line.strip().split(",")
                total += float(amount)
        print("Total Expense:", total, "\n")
    except FileNotFoundError:
        print("No expenses found.\n")

while True:
    print("---- EXPENSE TRACKER ----")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("Exiting Expense Tracker.")
        break
    else:
        print("Invalid choice. Try again.\n")
