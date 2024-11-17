class Employee:
    def get_data(self, name, salary, tax):
        self.name = name
        self.salary = salary
        self.tax = tax

    def salary_after_tax(self):
        self.salary *= 0.98
        return self.salary

    def update_tax_percentage(self):
        if self.tax == 2:
            self.tax = 3
            self.salary *= 1 - (self.tax / 100)

    def print_salary(self):
        print(self.salary)

obj1 = Employee()
obj1.get_data("Owais", 10321, 2)
obj1.print_salary()
print(obj1.salary_after_tax())
obj1.update_tax_percentage()
obj1.print_salary()