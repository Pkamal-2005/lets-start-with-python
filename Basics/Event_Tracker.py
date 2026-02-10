from datetime import datetime

SECRET_KEY = "KaiOP"
MAX_TRIES = 3

def login():
    tries = MAX_TRIES
    while tries > 0:
        key = input("Password: ").strip()
        if key == SECRET_KEY:
            print("Access granted\n")
            return True
        tries -= 1
        print(f"Invalid password. Remaining tries: {tries}")
    return False


def show_menu():
    print("\n--- Event Control Panel ---")
    print("1. Add Registration")
    print("2. Allow Entry")
    print("3. View Summary")
    print("4. Quit")


def register_person(reg_users, unknown_users):
    person = input("Name to register: ").strip().lower()
    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    if person in reg_users:
        print(f"{person} is already registered.")
    else:
        reg_users.add(person)
        unknown_users.discard(person)
        print(f"{person} registered successfully at {time}")


def enter_event(reg_users, present_users, unknown_users):
    person = input("Name entering event: ").strip().lower()
    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    if person in present_users:
        print(f"{person} already entered once.")
    elif person not in reg_users:
        unknown_users.add(person)
        print(f"{person} is not registered.")
    else:
        present_users.add(person)
        print(f"{person} entry confirmed at {time}")


def display_status(reg_users, present_users, unknown_users):
    print("\n--- Event Report ---")
    print("Total Registered :", len(reg_users))
    print("Total Entered    :", len(present_users))
    print("Unregistered    :", len(unknown_users))

    if present_users:
        print("\nAttendees List:")
        for name in present_users:
            print("-", name)


# ---------- Main Program ----------
if not login():
    print("System locked. Try later.")
    exit()

reg_users = set()
present_users = set()
unknown_users = set()

while True:
    show_menu()
    option = input("Select option: ").strip()

    if option == "1":
        register_person(reg_users, unknown_users)
    elif option == "2":
        enter_event(reg_users, present_users, unknown_users)
    elif option == "3":
        display_status(reg_users, present_users, unknown_users)
    elif option == "4":
        print("Program closed.")
        break
    else:
        print("Invalid option. Please choose again.")