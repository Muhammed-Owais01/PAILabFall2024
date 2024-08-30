students = {
    "Abser": [90, 70, 73, 63, 83],
    "Fasih": [69, 71, 92, 96, 86],
    "Ali":   [96, 91, 65, 65, 88],
    "Owais": [91, 84, 85, 22, 82]
}

def addStudent(studentName):
    students[studentName] = []

def addGrade(studentName, grade):
    if studentName in students:
        students[studentName].append(grade)
        return
    print("Student does not exist")

def removeStudent(studentName):
    if studentName in students:
        students.pop(studentName)
        print("Student Removed")
        return
    print("Student does not exist")

def findAverage(studentName):
    if studentName in students:
        grades = students[studentName]
        return sum(grades) / len(grades)
    return "Student does not exist"

while True:
    print("1- Add a student", "2- Add a grade", "3- Remove a student", "4- Find Average of a student", "5- Exit", sep='\n')
    choice = int(input("Choose an operation: "))
    if choice == 5: break
    studentName = input("Enter Student Name: ")
    if choice == 1:
        addStudent(studentName)
        print("Student added successfully")
    elif choice == 2:
        grade = int(input("Enter a grade: "))
        addGrade(studentName, grade)
    elif choice == 3:
        removeStudent(studentName)
    elif choice == 4:
        print(findAverage(studentName))