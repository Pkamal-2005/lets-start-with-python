class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = {} 
        self.gpa = 0
    def mark(self, sub, mark):
        self.marks[sub] = mark

    def calculate_gpa(self):
        if not self.marks:
            print("No marks entered for", self.name)
            return
        total_marks = sum(self.marks.values())
        num_subjects = len(self.marks)
        percentage = total_marks / num_subjects
        if percentage >= 90:
            self.gpa = 4.0
        elif percentage >= 80:
            self.gpa = 3.5
        elif percentage >= 70:
            self.gpa = 3.0
        elif percentage >= 60:
            self.gpa = 2.5
        elif percentage >= 50:
            self.gpa = 2.0
        else:
            self.gpa = 0.0

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print("Marks:")
        for sub, mark in self.marks.items():
            print(f"  {sub}: {mark}")
        print(f"GPA: {self.gpa}\n")

student1 = Student("Kai", 124)
student1.mark("OE", 85)
student1.mark("ESE", 78)
student1.mark("AADK", 92)
student1.calculate_gpa()
student1.display()
