class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_biodata(self):
        print(f"Name: {self.name}, Age: {self.age}")


obj1 = Student("Owais", 21)
obj1.print_biodata()