dictionary = {
    "Physics": 40,
    "Chemistry": 78,
    "Maths": 82,
}

total = 0
highest = 0
for i in dictionary:
    total += dictionary[i]
    if (dictionary[i] > highest): 
        highest = dictionary[i]
        subject = i

print(f"Avg Marks: {total / 3}\nHighest Marks: {subject}")

    