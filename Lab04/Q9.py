class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"Id: {self.id}, Name: {self.name}")


class Marks(Student):
    student_marks = {}

    def __init__(self, algo_marks, datascience_marks, calculus_marks, id, name):
        super().__init__(id, name)
        self.student_marks["Algo"] = algo_marks
        self.student_marks["Data Science"] = datascience_marks
        self.student_marks["Calculus"] = calculus_marks

    def display_marks(self):
        print(self.student_marks)

class Result(Marks):
    def __init__(self, algo_marks, datascience_marks, calculus_marks, id, name):
        super().__init__(algo_marks, datascience_marks, calculus_marks, id, name)
        self.total = sum(self.student_marks[i] for i in self.student_marks)
        self.average = self.total / len(self.student_marks)

    def display_result(self):
        print(f"Total: {self.total}, Average: {self.average}")


obj1 = Result(65, 85, 78, 10239120, "Owais")
obj1.display()
obj1.display_marks()
obj1.display_result()
