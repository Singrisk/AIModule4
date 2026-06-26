from datetime import date

class Student:
    """
    Represents a student in the Student Management System.

    Attributes:
        Roll_no (int): Unique roll number.
        Name (str): Student's name.
        Age (int): Student's age.
        Math (int): Mathematics marks.
        Physics (int): Physics marks.
        Chemistry (int): Chemistry marks.
        Biology (int): Biology marks.
        English (int): English marks.
        Interest (str): Student's career interest.
        Course (str): Selected/Recommended course.
    """

    def __init__(
        self,
        Roll_no: int,
        Name: str,
        Age: int,
        Math: int,
        Physics: int,
        Chemistry: int,
        Biology: int,
        English: int,
        Interest: str,
        Course: str
    ) -> None:

        self.Roll_no = Roll_no
        self.Name = Name
        self.Age = Age

        self.Math = Math
        self.Physics = Physics
        self.Chemistry = Chemistry
        self.Biology = Biology
        self.English = English

        self.Interest = Interest
        self.Course = Course

    def dob(self) -> int:
        """
        Returns the estimated year of birth.
        """
        return date.today().year - self.Age

    def average_marks(self) -> float:
        """
        Returns the average marks of the student.
        """
        total = (
            self.Math +
            self.Physics +
            self.Chemistry +
            self.Biology +
            self.English
        )

        return total / 5

    def to_detail(self) -> tuple:
        """
        Returns student personal and academic details.
        """
        return (
            self.Roll_no,
            self.Name,
            self.Age,
            self.Math,
            self.Physics,
            self.Chemistry,
            self.Biology,
            self.English,
            self.Interest
        )

    def to_course(self) -> tuple:
        """
        Returns course-related information.
        """
        return (
            self.Roll_no,
            self.Name,
            self.Course
        )

    def ml_features(self) -> list:
        """
        Returns only the features required by the ML model.
        """
        return [
            self.Math,
            self.Physics,
            self.Chemistry,
            self.Biology,
            self.English,
            self.Interest
        ]

    def __str__(self) -> str:
        return (
            f"\n{'='*55}\n"
            f"Roll Number : {self.Roll_no}\n"
            f"Name        : {self.Name}\n"
            f"Age         : {self.Age}\n"
            f"Birth Year  : {self.dob()}\n\n"
            f"Marks\n"
            f"  Mathematics : {self.Math}\n"
            f"  Physics     : {self.Physics}\n"
            f"  Chemistry   : {self.Chemistry}\n"
            f"  Biology     : {self.Biology}\n"
            f"  English     : {self.English}\n\n"
            f"Average Marks : {self.average_marks():.2f}\n"
            f"Interest      : {self.Interest}\n"
            f"Course        : {self.Course}\n"
            f"{'='*55}"
        )