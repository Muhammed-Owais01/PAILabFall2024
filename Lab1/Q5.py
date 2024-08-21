count = int(input("Enter total numbers: "))
list = []
for i in range(0, count):
    list.append(int(input("Enter a number: ")))

number = int(input("Remove number from list: "))
for i in list[:]:
    if i < number:
        list.remove(i)
print(list)