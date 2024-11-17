name = input("Enter your name: ")
cnic = input("Enter your cnic: ")
age = input("Enter your age: ")
salary =  input("Enter your salary: ")

with open("Q04Data.txt", 'w') as file:
    file.write(name + " " + cnic + " " + age + " " + salary + " ")

contactNumber = input("Enter your contact number: ")
with open("Q04Data.txt", 'a') as file:
    file.write(contactNumber)

