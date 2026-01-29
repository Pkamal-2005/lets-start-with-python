balance = 0
transactions = []
password = "@Kai"

while True:
    passw = input("Enter your password to access the transaction system: ")
    if passw == password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. 2 Attempts remaining.")
    passw = input("Enter your password to access the transaction system: ")
    if passw == password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. 1 Attempt remaining.")
    passw = input("Enter your password to access the transaction system: ")
    if passw == password:
        print("Access granted.")
        break
    else:
        print("Access denied. Exiting the system.")
        exit()
while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. View Transactions")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            transactions.append(f"Deposited: Rs.{amount:.2f}")
            print(f"Rs.{amount:.2f} deposited successfully.")
        else:
            print("Invalid amount. Please enter a positive number.")
    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))
        if 0 < amount <= balance:
            balance -= amount
            transactions.append(f"Withdrew: Rs.{amount:.2f}")
            print(f"Rs{amount:.2f} withdrawn successfully.")
        else:
            print("Invalid amount. Please enter a positive number not exceeding your balance.")
    elif choice == '3':
        print(f"Current balance: Rs.{balance:.2f}")
    elif choice == '4':
        if transactions:
            print("Transaction History:")
            for transaction in transactions:
                print(transaction)
        else:
            print("No transactions yet.")
    elif choice == '5':
        print("Exiting the system. 안녕히 가세요!")
        break
    else:
        print("Invalid choice. Please select a valid option.")