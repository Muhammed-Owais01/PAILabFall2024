class Animal:
    def __init__(self, name, age, habitat, available):
        self.name = name
        self.age = age
        self.habitat = habitat
        self.available = available
    
    def setAvailable(self, available):
        self.available = available

    def displayAnimalInfo(self):
        print(f"Name: {self.name}, Age: {self.age}, Habitat: {self.habitat}, Available: {self.available}, ")

class Mammal(Animal):
    def __init__(self, name, age, habitat, available, fur_length, diet_type):
        super().__init__(name, age, habitat, available)
        self.fur_length = fur_length
        self.diet_type = diet_type
    
    def displayAnimalInfo(self):
        super().displayAnimalInfo()
        print(f"Fur Length: {self.fur_length}, Diet Type: {self.diet_type}", end='\n')

class Birds(Animal):
    def __init__(self, name, age, habitat, available, wingspan, flight_altitude):
        super().__init__(name, age, habitat, available)
        self.wingspan = wingspan
        self.flight_altitude = flight_altitude
    
    def displayAnimalInfo(self):
        super().displayAnimalInfo()
        print(f"WingSpan: {self.wingspan}, Flight Altitude: {self.flight_altitude}", end='\n')

class Reptiles(Animal):
    def __init__(self, name, age, habitat, available, scale_pattern, venomous_status):
        super().__init__(name, age, habitat, available)
        self.scale_pattern = scale_pattern
        self.venomous_status = venomous_status
    
    def displayAnimalInfo(self):
        super().displayAnimalInfo()
        print(f"Scale Pattern: {self.scale_pattern}, Venomous Status: {self.venomous_status}")

mammal = Mammal("Lion", 5, "Savannah", True, "Short", "Carnivore")
bird = Birds("Eagle", 3, "Mountain Range", True, 2.5, 3000)
reptile = Reptiles("Python", 2, "Rainforest", False, "Diamond", "Non-venomous")

print("Displaying information for each animal:")
mammal.displayAnimalInfo()
bird.displayAnimalInfo()
reptile.displayAnimalInfo()

print("\nChanging availability status...")
mammal.setAvailable(False)
bird.setAvailable(False)
reptile.setAvailable(True)

print("\nUpdated availability status:")
mammal.displayAnimalInfo()
bird.displayAnimalInfo()
reptile.displayAnimalInfo()
