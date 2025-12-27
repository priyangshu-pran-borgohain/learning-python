accounts = {}

def create_account():
    name = input("Enter your name: ")
    pin = input("Set your 4-digit PIN: ")
    accounts[name] = {"pin": pin, "balance": 0}
    print("Account created successfully!\n")

def deposit():
    name = input("Enter name: ")
    pin = input("Enter PIN: ")

    if name in accounts and accounts[name]["pin"] == pin:
        amount = int(input("Enter amount to deposit: "))
        accounts[name]["balance"] += amount
        print("Deposit successful!\n")
    else:
        print("Invalid name or PIN.\n")

def withdraw():
    name = input("Enter name: ")
    pin = input("Enter PIN: ")

    if name in accounts and accounts[name]["pin"] == pin:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= accounts[name]["balance"]:
            accounts[name]["balance"] -= amount
            print("Withdrawal successful!\n")
        else:
            print("Insufficient balance.\n")
    else:
        print("Invalid name or PIN.\n")

def check_balance():
    name = input("Enter name: ")
    pin = input("Enter PIN: ")

    if name in accounts and accounts[name]["pin"] == pin:
        print("Current Balance:", accounts[name]["balance"], "\n")
    else:
        print("Invalid name or PIN.\n")

while True:
    print("---- Bank Management System ----")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print("Thank you for using the bank system.")
        break
    else:
        print("Invalid choice. Try again.\n")
