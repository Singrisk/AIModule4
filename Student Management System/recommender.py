import pickle
import pandas as pd

# ===============================
# Load Trained Model and Encoders
# ===============================

with open("course_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("interest_encoder.pkl", "rb") as file:
    interest_encoder = pickle.load(file)

with open("course_encoder.pkl", "rb") as file:
    course_encoder = pickle.load(file)


# ===============================
# Recommendation Function
# ===============================

def recommend_course(
    math: int,
    physics: int,
    chemistry: int,
    biology: int,
    english: int,
    interest: str
):

    try:
        interest = interest_encoder.transform([interest])[0]

        student = pd.DataFrame([{
            "Math": math,
            "Physics": physics,
            "Chemistry": chemistry,
            "Biology": biology,
            "English": english,
            "Interest": interest
        }])

        prediction = model.predict(student)[0]

        probabilities = model.predict_proba(student)[0]
        confidence = max(probabilities) * 100

        course = course_encoder.inverse_transform([prediction])[0]

        return course, confidence

    except ValueError:
        return (
            "Unknown Interest!\n"
            "Valid Interests are:\n"
            "- Engineering\n"
            "- Doctor\n"
            "- Commerce\n"
            "- Programming"
        )