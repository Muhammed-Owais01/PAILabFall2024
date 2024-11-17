from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_bonus(self):
        pass

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self.salary * 0.2

    def hire(self):
        print(f"{self.name} is hiring...")

class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self.salary * 0.1

    def write_code(self):
        print(f"{self.name} is writing code...")

class SeniorManager(Manager):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self.salary * 0.3


mang1 = Manager("Owais", 20)
dev1 = Developer("Fasih", 320)
senMan = SeniorManager("Ali", 2030)

print(f"Manager Bonus: {mang1.calculate_bonus()}")
mang1.hire()
print(f"Developer Bonus: {dev1.calculate_bonus()}")
dev1.write_code()
print(f"Senior Manager Bonus: {senMan.calculate_bonus()}")