searchWord = input("Enter a word to search: ")
replaceWord = input("Enter a word to replace: ")

try:
    with open("Q02Data.txt", 'r') as file:
        fileContent = file.read()
        if searchWord in fileContent:
            fileContent = fileContent.replace(searchWord, replaceWord)
        else: print("Word does not exist in file")
except FileNotFoundError:
    print("File does not exist")

try:
    with open("Q02Data.txt", 'w') as file:
        file.write(fileContent) 
except FileNotFoundError:
    print("File does not exist")