class ParkingLot:
    c = 5
    parked_cars = []
    def park_car(self, car):
        if len(ParkingLot.parked_cars) < ParkingLot.c:
            ParkingLot.parked_cars.append(car)
            print("Car parked:", car)
        else:
            print("Parking full")

    def remove_car(self, car):
        if car in ParkingLot.parked_cars:
            ParkingLot.parked_cars.remove(car)
            print("Car removed:", car)
        else:
            print("Car not found")

    def show(self):
        print("Cars in parking:", ParkingLot.parked_cars)

p = ParkingLot()
p.park_car("Car1")
p.park_car("Car2")
p.park_car("Car3")
p.show()
p.remove_car("Car1")
p.show()