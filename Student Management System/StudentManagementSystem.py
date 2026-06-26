import os
import csv
from Student import Student
from recommender import recommend_course

class StudentManagementSystem:
    """
    Student Management System

    Features
    --------
    1. Add Student
    2. Delete Student
    3. Update Student
    4. Search Student
    5. Display All Students
    6. Display Available Courses
    7. Recommend Course (ML)
    8. Save and Load Records
    """

    SCHOOL = "D.A.V Public School"
    ADDRESS = "B.R.S Nagar, Ludhiana"

    FILE = "students.csv"

    VALID_COURSES = (
        "MEDICAL",
        "NONMEDICAL",
        "GENERAL",
        "GENERALWITHCS"
    )

    def __init__(self):
        print("=" * 70)
        print(f"Welcome to {self.SCHOOL}")
        print(self.ADDRESS)
        print("=" * 70)

        self.StudentTable = {}
        self.Courses = set()

        self.load()
    
    def load(self):
        if not os.path.exists(self.FILE):
            return

        with open(self.FILE, "r", newline="") as file:

            reader = csv.reader(file)

            for row in reader:

                student = Student(

                    int(row[0]),
                    row[1],
                    int(row[2]),

                    int(row[3]),
                    int(row[4]),
                    int(row[5]),
                    int(row[6]),
                    int(row[7]),

                    row[8],
                    row[9]

                )

                self.StudentTable[student.Roll_no] = student
                self.Courses.add(student.Course)
    
    def save_to_file(self):
        with open(self.FILE, "w", newline="") as file:

            writer = csv.writer(file)

            for student in self.StudentTable.values():

                writer.writerow([

                    student.Roll_no,
                    student.Name,
                    student.Age,

                    student.Math,
                    student.Physics,
                    student.Chemistry,
                    student.Biology,
                    student.English,

                    student.Interest,
                    student.Course

                ])
    
    def add(
        self,
        roll,
        name,
        age,

        math,
        physics,
        chemistry,
        biology,
        english,

        interest,
        course
    ):

        if roll in self.StudentTable:
            print("Student already exists.")
            return

        student = Student(

            roll,
            name,
            age,

            math,
            physics,
            chemistry,
            biology,
            english,

            interest,
            course

        )

        self.StudentTable[roll] = student

        self.Courses.add(course)

        self.save_to_file()

        print("Student Added Successfully.")
    
    def update(
        self,
        roll,

        **kwargs
    ):

        if roll not in self.StudentTable:

            print("Student Not Found.")
            return

        student = self.StudentTable[roll]

        for key, value in kwargs.items():

            if value is not None:

                setattr(student, key, value)

        self.save_to_file()

        print("Student Updated Successfully.")
    
    def search(self, roll):
        student = self.StudentTable.get(roll)

        if student is None:

            print("Student Not Found.")

            return

        print(student)

        return self.StudentTable.get(student_id)
    
    def display_students(self):
        if not self.StudentTable:

            print("No Student Found")

            return

        for student in self.StudentTable.values():

            print(student)
    
    def display_courses(self):
        print("\nAvailable Courses")

        for course in sorted(self.Courses):

            print(course)
    
    def recommend_course(
        self,

        math,
        physics,
        chemistry,
        biology,
        english,
        interest
    ):

        course = recommend_course(

            math,
            physics,
            chemistry,
            biology,
            english,
            interest

        )

        print("\nRecommended Course")

        print(course)