from datetime import datetime

class Vehicle:
    def __init__(self, make, model, rental_price_per_day):
        self.make = make
        self.model = model
        self._rental_price_per_day = rental_price_per_day 
        self.is_available = True

    def check_availability(self):
        return self.is_available

    def calculate_rental_cost(self, start_date, end_date):
        days = (end_date - start_date).days
        return days * self._rental_price_per_day

    def display_details(self):
        print(f"Make: {self.make}, Model: {self.model}, Price per day: ${self._rental_price_per_day}, Available: {self.is_available}")

    def rent(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.make} {self.model} has been rented.")
        else:
            print(f"{self.make} {self.model} is not available.")

    def return_vehicle(self):
        self.is_available = True
        print(f"{self.make} {self.model} has been returned.")


class Car(Vehicle):
    def __init__(self, make, model, rental_price_per_day):
        super().__init__(make, model, rental_price_per_day)


class SUV(Vehicle):
    def __init__(self, make, model, rental_price_per_day):
        super().__init__(make, model, rental_price_per_day)


class Truck(Vehicle):
    def __init__(self, make, model, rental_price_per_day):
        super().__init__(make, model, rental_price_per_day)


class RentalReservation:
    def __init__(self, customer, vehicle, start_date, end_date):
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date
        self.total_cost = vehicle.calculate_rental_cost(start_date, end_date)

    def display_reservation_details(self):
        print(f"Customer: {self.customer.name}, Vehicle: {self.vehicle.make} {self.vehicle.model}, Start Date: {self.start_date}, End Date: {self.end_date}, Total Cost: ${self.total_cost}")


class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self._contact_info = contact_info 
        self.rental_history = []

    def rent_vehicle(self, vehicle, start_date, end_date):
        if vehicle.check_availability():
            reservation = RentalReservation(self, vehicle, start_date, end_date)
            vehicle.rent()
            self.rental_history.append(reservation)
            print(f"{self.name} has rented {vehicle.make} {vehicle.model}.")
        else:
            print(f"Vehicle {vehicle.make} {vehicle.model} is not available.")

    def return_vehicle(self, vehicle):
        vehicle.return_vehicle()

    def display_rental_history(self):
        print(f"Rental history for {self.name}:")
        for reservation in self.rental_history:
            reservation.display_reservation_details()


def display_info(item):
    if isinstance(item, Vehicle):
        item.display_details()
    elif isinstance(item, RentalReservation):
        item.display_reservation_details()


car = Car("Toyota", "Corolla", 40)
suv = SUV("Honda", "CR-V", 60)
truck = Truck("Ford", "F-150", 80)

customer = Customer("John Doe", "johndoe@example.com")

start_date = datetime(2023, 9, 20)
end_date = datetime(2023, 9, 25)
customer.rent_vehicle(car, start_date, end_date)

customer.return_vehicle(car)

customer.display_rental_history()

display_info(car)
reservation = RentalReservation(customer, suv, start_date, end_date)
display_info(reservation)
