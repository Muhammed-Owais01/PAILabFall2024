from abc import ABC, abstractmethod

# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any
# vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on
# full fare as a maintenance charge. So total fare for bus instance will become the final amount =
# total fare + 10% of the total fare.

class Vehicle(ABC):
    def __init__(self, capacity):
        self.capacity = capacity

    @abstractmethod
    def get_fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, capacity):
        super().__init__(capacity)

    def get_fare(self):
        return super().get_fare() * 1.1

bus1 = Bus(20)

print(bus1.get_fare())
