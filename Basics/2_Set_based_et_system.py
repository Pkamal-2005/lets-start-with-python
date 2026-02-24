registered = set()
entered = set()

def register_user():
    name = input("Name: ").strip()
    if name in registered:
        print("The user is already registered")
    else:
        registered.add(name)
        print("Registered")

def enter_user():
    name = input("Name: ").strip()
    if name not in registered:
        print("Not registered")
    elif name in entered:
        print("Fraud detected")
    else:
        entered.add(name)
        print("Entered")

def total_users():
    print("Total Entered Users:", len(entered))

def main():
    while True:
        choice = input("1:Register User  2:Enter User  3:Total Users  4:Exit -> ")

        if choice == "1":
            register_user()
        elif choice == "2":
            enter_user()
        elif choice == "3":
            total_users()
        elif choice == "4":
            break
        else:
            print("Invalid Choice")
main()