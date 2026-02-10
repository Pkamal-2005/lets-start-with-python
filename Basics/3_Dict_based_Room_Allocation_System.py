import datetime
rooms = {
    101: None,
    102: None,
    103: None,
    104: None
}
occupied = set()
PASSWORD = "KaiOP" 

while True:
    print("\n1. Allocate  2. Vacate  3. View Rooms  4. Exit")
    choice = input("Choose: ")
    
    if choice == "1":
        entered_pass = input("Enter password to allocate room: ")
        if entered_pass != PASSWORD:
            print("Incorrect password. Access denied.")
            continue
            
        room_input = input("Enter room number: ")
        try:
            room = int(room_input)  
        except ValueError:
            print("Invalid room number. Please enter a number.")
            continue
            
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
            print("Room not available or invalid room number")

    elif choice == "2":
        room_input = input("Enter room number to vacate: ")
        try:
            room = int(room_input)
        except ValueError:
            print("Invalid room number. Please enter a number.")
            continue
            
        if room in occupied:
            rooms[room] = None
            occupied.remove(room)
            print(f"Room {room} vacated")
        else:
            print("Room already empty or invalid room number")

    elif choice == "3":
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

    elif choice == "4":
        print("Exiting system")
        break

    else:
        print("Invalid choice")