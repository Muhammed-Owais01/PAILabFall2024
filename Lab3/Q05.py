import json

name = input("Enter your name: ")
age = int(input("Enter your age: "))
max = 0
maxAgeName = ""
try:
    with open("Q05.json", "r") as file:
        data = json.load(file)
        data[name] = age
    with open("Q05.json", 'w') as file:
        file.seek(0)
        json.dump(data, file, indent=4)
        for i in data:
            if int(data[i]) > max:
                maxAgeName = i 
                max = data[i]
except FileNotFoundError:
    print("File does not exist")
print(f"Max Age of {maxAgeName} is {max}")
