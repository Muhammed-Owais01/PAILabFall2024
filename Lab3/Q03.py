list1 = input("Enter Values List1: ").split(",")
list2 = input("Enter Values List2: ").split(",")
myDict = dict(zip(list1, list2))

with open("Q03Data.txt", "w") as file:
    file.write(str(myDict))

