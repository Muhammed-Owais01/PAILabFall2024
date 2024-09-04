try:
    with open("Q1Data.txt", 'r') as file:
        print(len(file.read()))
except FileNotFoundError:
    print("File does not exist")
