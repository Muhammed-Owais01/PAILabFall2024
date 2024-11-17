count = int(input("Enter total numbers: "))
list1 = []
for i in range(0, count):
    num = int(input("Enter a number: "))
    list1.append(num)

even = 0
for num in list1:
    if num % 2 == 0:
        even += 1
print(even)