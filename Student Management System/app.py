from flask import Flask, render_template, request
from StudentManagementSystem import StudentManagementSystem
from recommender import recommend_course

app = Flask(__name__)

# Create one instance of the Student Management System
sms = StudentManagementSystem()


# ===========================
# Home Page
# ===========================

@app.route("/")
def home():
    return render_template("index.html")


# ===========================
# Add Student
# ===========================

@app.route("/add", methods=["GET", "POST"])
def add_student():

    message = ""

    if request.method == "POST":

        roll_no = int(request.form["roll_no"])
        name = request.form["name"]
        age = int(request.form["age"])
        course = request.form["course"]

        sms.add(roll_no, name, age, course)

        message = "Student Added Successfully!"

    return render_template(
        "add_student.html",
        message=message
    )


# ===========================
# Search Student
# ===========================

@app.route("/search", methods=["GET", "POST"])
def search_student():

    student = None

    if request.method == "POST":

        roll_no = int(request.form["roll_no"])

        student = sms.search(roll_no)

    return render_template(
        "search_student.html",
        student=student
    )


# ===========================
# Display Students
# ===========================

@app.route("/display")
def display_students():

    students = sms.display_students()

    return render_template(
        "display_students.html",
        students=students
    )


# ===========================
# Course Recommendation
# ===========================

@app.route("/recommend", methods=["GET", "POST"])
def recommend():

    prediction = None
    confidence = None

    if request.method == "POST":

        math = int(request.form["math"])
        physics = int(request.form["physics"])
        chemistry = int(request.form["chemistry"])
        biology = int(request.form["biology"])
        english = int(request.form["english"])
        interest = request.form["interest"]

        prediction, confidence = recommend_course(
            math,
            physics,
            chemistry,
            biology,
            english,
            interest
        )

        confidence = round(confidence, 2)

    return render_template(
        "recommend.html",
        prediction=prediction,
        confidence=confidence
    )


# ===========================
# Run Flask App
# ===========================

if __name__ == "__main__":
    app.run(debug=True)