with open("test.txt", 'r') as file:
    fileContent = " ".join(file.read().split('\n'))
    print("Character Count: ", len(fileContent.replace(" ", "")))
    print("Word Count: ", len(fileContent.split(" ")))