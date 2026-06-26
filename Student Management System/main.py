from StudentManagementSystem import StudentManagementSystem
sms = StudentManagementSystem()

while True:

    print("\n" + "=" * 70)
    print("          STUDENT MANAGEMENT SYSTEM")
    print("=" * 70)

    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Display All Students")
    print("6. Display Courses")
    print("7. Recommend Course (ML)")
    print("8. Exit")

    try:

        choice = int(input("\nEnter your choice: "))

        # ---------------- ADD ----------------

        if choice == 1:

            roll = int(input("Roll Number : "))
            name = input("Name : ")
            age = int(input("Age : "))

            math = int(input("Math Marks : "))
            physics = int(input("Physics Marks : "))
            chemistry = int(input("Chemistry Marks : "))
            biology = int(input("Biology Marks : "))
            english = int(input("English Marks : "))

            interest = input("Interest : ")

            course = input("Course : ").upper()

            sms.add(
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

        # ---------------- DELETE ----------------

        elif choice == 2:

            roll = int(input("Roll Number : "))
            sms.delete(roll)

        # ---------------- UPDATE ----------------

        elif choice == 3:

            roll = int(input("Roll Number : "))

            print("\nLeave blank if you don't want to update a field.\n")

            name = input("Name : ")
            age = input("Age : ")

            math = input("Math Marks : ")
            physics = input("Physics Marks : ")
            chemistry = input("Chemistry Marks : ")
            biology = input("Biology Marks : ")
            english = input("English Marks : ")

            interest = input("Interest : ")
            course = input("Course : ")

            sms.update(

                roll,

                Name=name or None,
                Age=int(age) if age else None,

                Math=int(math) if math else None,
                Physics=int(physics) if physics else None,
                Chemistry=int(chemistry) if chemistry else None,
                Biology=int(biology) if biology else None,
                English=int(english) if english else None,

                Interest=interest or None,
                Course=course.upper() if course else None

            )

        # ---------------- SEARCH ----------------

        elif choice == 4:

            roll = int(input("Roll Number : "))
            sms.search(roll)

        # ---------------- DISPLAY ----------------

        elif choice == 5:

            sms.display_students()

        # ---------------- COURSES ----------------

        elif choice == 6:

            sms.display_courses()

        # ---------------- ML RECOMMENDATION ----------------

        elif choice == 7:

            print("\nEnter Student's Marks\n")

            math = int(input("Math : "))
            physics = int(input("Physics : "))
            chemistry = int(input("Chemistry : "))
            biology = int(input("Biology : "))
            english = int(input("English : "))

            interest = input("Interest : ")

            sms.recommend_course(
                math,
                physics,
                chemistry,
                biology,
                english,
                interest
            )

        # ---------------- EXIT ----------------

        elif choice == 8:

            print("\nThank you for using the Student Management System.")
            break

        else:

            print("Invalid Choice!")

    except ValueError:

        print("Please enter valid numeric input.")