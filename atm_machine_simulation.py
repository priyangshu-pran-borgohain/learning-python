balance = 5000
pin = "1234"
transactions = []

def check_pin():
    entered_pin = input("Enter your PIN: ")
    return entered_pin == pin

def check_balance():
    print("Current Balance:", balance)

def deposit():
    global balance
    amount = int(input("Enter amount to deposit: "))
    balance += amount
    transactions.append(f"Deposited: {amount}")
    print("Deposit successful!")

def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        transactions.append(f"Withdrawn: {amount}")
        print("Please collect your cash.")
    else:
        print("Insufficient balance.")

def mini_statement():
    print("\nMini Statement:")
    if not transactions:
        print("No transactions yet.")
    else:
        for t in transactions:
            print(t)
    print()

while True:
    print("\n---- ATM MACHINE ----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Mini Statement")
    print("5. Exit")

    if not check_pin():
        print("Incorrect PIN.")
        continue

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        mini_statement()
    elif choice == "5":
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid option.")
