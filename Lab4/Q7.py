class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity
        self.fare = self.capacity * 100


class Bus(Vehicle):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.fare *= 1.1

    def display_vehicle_data(self):
        print(f"Capacity: {self.capacity}, Fare: {self.fare}")


obj1 = Bus(40)
obj1.display_vehicle_data()
