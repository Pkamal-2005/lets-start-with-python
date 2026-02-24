balance = 0
transactions = []
password = "@Kai"

def check_password():
    for i in range(3):
        p = input("Enter password: ")
        if p == password:
            print("Access granted.")
            return True
        else:
            print(f"Incorrect password. {2-i} attempts remaining.")
    print("Access denied.")
    return False

def deposit():
    global balance
    amt = float(input("Enter deposit amount: "))
    if amt > 0:
        balance += amt
        transactions.append(f"Deposited: Rs.{amt:.2f}")
        print("Amount deposited.")
    else:
        print("Invalid amount.")

def withdraw():
    global balance
    amt = float(input("Enter withdrawal amount: "))
    if 0 < amt <= balance:
        balance -= amt
        transactions.append(f"Withdrew: Rs.{amt:.2f}")
        print("Amount withdrawn.")
    else:
        print("Invalid amount.")

def check_balance():
    print(f"Current balance: Rs.{balance:.2f}")

def view_transactions():
    if transactions:
        for t in transactions:
            print(t)
    else:
        print("No transactions yet.")

# Main Program
if check_password():
    while True:
        print("\n1.Deposit  2.Withdraw  3.Balance  4.Transactions  5.Exit")
        choice = input("Choose: ")

        if choice == '1':
            deposit()
        elif choice == '2':
            withdraw()
        elif choice == '3':
            check_balance()
        elif choice == '4':
            view_transactions()
        elif choice == '5':
            print("Exiting system. 안녕히 가세요!")
            break
        else:
            print("Invalid choice.")