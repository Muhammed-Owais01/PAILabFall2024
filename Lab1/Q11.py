dict = {}
for i in range(0, 3):
    subject = input("Enter a subject: ")
    marks = int(input("Enter marks: "))
    dict[subject] = marks

total = 0
for i in dict:
    total += dict[i]
    print(f"{i}: {dict[i]}%")
print(f"Average: {total / 3}")