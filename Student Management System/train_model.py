import os
import joblib
import warnings
import pandas as pd

from sklearn.model_selection import (
    train_test_split,
    RandomizedSearchCV
)

from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier

from lightgbm import LGBMClassifier

warnings.filterwarnings("ignore")


# ===========================================================
# Load Dataset
# ===========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSV_PATH = os.path.join(BASE_DIR, "students.csv")

data = pd.read_csv(CSV_PATH)


# ===========================================================
# Encode Categorical Columns
# ===========================================================

interest_encoder = LabelEncoder()

course_encoder = LabelEncoder()

data["Interest"] = interest_encoder.fit_transform(
    data["Interest"]
)

data["Course"] = course_encoder.fit_transform(
    data["Course"]
)


# ===========================================================
# Features & Target
# ===========================================================

X = data[
    [
        "Math",
        "Physics",
        "Chemistry",
        "Biology",
        "English",
        "Interest"
    ]
]

y = data["Course"]


# ===========================================================
# Train Test Split
# ===========================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)


# ===========================================================
# Model Dictionary
# ===========================================================

models = {

    "Random Forest": (

        RandomForestClassifier(random_state=42),

        {

            "n_estimators": [100, 200, 300],

            "max_depth": [5, 10, 15, None],

            "min_samples_split": [2, 5, 10],

            "min_samples_leaf": [1, 2, 4]

        }

    ),


    "XGBoost": (

        XGBClassifier(

            objective="multi:softprob",

            num_class=len(course_encoder.classes_),

            eval_metric="mlogloss",

            random_state=42

        ),

        {

            "n_estimators": [100, 200, 300],

            "max_depth": [3, 5, 7],

            "learning_rate": [0.01, 0.05, 0.1],

            "subsample": [0.8, 1.0],

            "colsample_bytree": [0.8, 1.0]

        }

    ),


    "LightGBM": (

        LGBMClassifier(

            random_state=42

        ),

        {

            "n_estimators": [100, 200, 300],

            "learning_rate": [0.01, 0.05, 0.1],

            "num_leaves": [31, 50, 70],

            "max_depth": [-1, 5, 10]

        }

    )

}


# ===========================================================
# Training Models
# ===========================================================

results = []

best_model = None

best_score = 0


for model_name, (model, params) in models.items():

    print("=" * 70)

    print(f"Training {model_name}")

    print("=" * 70)

    search = RandomizedSearchCV(

        estimator=model,

        param_distributions=params,

        n_iter=10,

        cv=5,

        scoring="accuracy",

        random_state=42,

        n_jobs=-1

    )

    search.fit(

        X_train,

        y_train

    )

    tuned_model = search.best_estimator_

    prediction = tuned_model.predict(X_test)

    accuracy = accuracy_score(

        y_test,

        prediction

    )

    precision = precision_score(

        y_test,

        prediction,

        average="weighted"

    )

    recall = recall_score(

        y_test,

        prediction,

        average="weighted"

    )

    f1 = f1_score(

        y_test,

        prediction,

        average="weighted"

    )

    results.append(

        [

            model_name,

            accuracy,

            precision,

            recall,

            f1,

            search.best_params_

        ]

    )

    if accuracy > best_score:

        best_score = accuracy

        best_model = tuned_model