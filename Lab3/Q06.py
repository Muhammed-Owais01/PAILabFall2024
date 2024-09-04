question = input("Enter a question: ")
try:
    with open("questions.txt", 'w') as file:
        if (question.endswith("?")): file.write(question)
except FileNotFoundError:
    print("File does not exist")