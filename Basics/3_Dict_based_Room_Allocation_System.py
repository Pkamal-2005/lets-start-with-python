import datetime

rooms = {
    101: None,
    102: None,
    103: None,
    104: None
}

occupied = set()
PASSWORD = "KaiOP"


def allocate_room():
    entered_pass = input("Enter password to allocate room: ")
    if entered_pass != PASSWORD:
        print("Incorrect password. Access denied.")
        return

    try:
        room = int(input("Enter room number: "))
    except ValueError:
        print("Invalid room number.")
        return

    if room in rooms and rooms[room] is None:
        name = input("Name: ")
        phone = input("Phone: ")
        purpose = input("Purpose: ")
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        rooms[room] = {
            "Name": name,
            "Phone": phone,
            "Purpose": purpose,
            "Allocated_Time": current_time
        }

        occupied.add(room)
        print(f"Room {room} allocated successfully at {current_time}")
    else:
        print("Room not available or invalid number")


def vacate_room():
    try:
        room = int(input("Enter room number to vacate: "))
    except ValueError:
        print("Invalid room number.")
        return

    if room in occupied:
        rooms[room] = None
        occupied.remove(room)
        print(f"Room {room} vacated")
    else:
        print("Room already empty or invalid number")


def view_rooms():
    print("\n=== Room Status ===")
    for r, info in rooms.items():
        if info:
            print(f"Room {r} -> Occupied")
            print(f"  Name: {info['Name']}")
            print(f"  Phone: {info['Phone']}")
            print(f"  Purpose: {info['Purpose']}")
            print(f"  Allocated Time: {info['Allocated_Time']}")
        else:
            print(f"Room {r} -> Empty")
    print("===================")


def main():
    while True:
        print("\n1. Allocate  2. Vacate  3. View Rooms  4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            allocate_room()
        elif choice == "2":
            vacate_room()
        elif choice == "3":
            view_rooms()
        elif choice == "4":
            print("Exiting system")
            break
        else:
            print("Invalid choice")


main()