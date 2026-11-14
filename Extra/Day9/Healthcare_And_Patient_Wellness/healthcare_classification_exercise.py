"""
Title: Healthcare Classification Lifecycle (Student Exercise)
Description: Module 7 Supervised Segmentation & Classification Exercise.
Total Marks: 40 Marks
"""

# Step 0: Import necessary libraries
# TODO: Import pandas, LogisticRegression from sklearn.linear_model, accuracy_score, and confusion_matrix


def phase_1_discovery_and_setup():
    """
    [Phase 1] Discovery & Data Setup (5 Marks)
    - Goal: Load 'patient_classification_data.csv' and inspect class distribution.
    """
    print("\n[PHASE 1] Discovery & Data Setup (5 Marks)")
    print("-" * 65)
    # TODO: Load CSV file using pandas
    # TODO: Check class balance of 'High_Risk_Hypertension' (value_counts)
    pass


def phase_2_supervised_segmentation(df):
    """
    [Phase 2] Supervised Segmentation & Feature Selection (10 Marks)
    - Goal: Analyze feature differences between risk groups.
    """
    print("\n[PHASE 2] Supervised Segmentation (10 Marks)")
    print("-" * 65)
    # TODO: Group data by 'High_Risk_Hypertension' and calculate mean of numeric features (BMI, Daily_Steps)
    pass


def phase_3_classification_modeling(df):
    """
    [Phase 3] Classification Model Induction (10 Marks)
    - Goal: Train a Logistic Regression model to classify high-risk patients.
    """
    print("\n[PHASE 3] Classification Modeling (10 Marks)")
    print("-" * 65)
    # TODO: Define features X = df[['BMI', 'Daily_Steps']] and target y = df['High_Risk_Hypertension']
    # TODO: Fit LogisticRegression model
    pass


def phase_4_model_evaluation(model, X, y):
    """
    [Phase 4] Evaluating Classifiers & Generalization (15 Marks)
    - Goal: Compute Accuracy and Confusion Matrix.
    - Provide clinical prescriptive actions.
    """
    print("\n[PHASE 4] Model Evaluation & Clinical Action (15 Marks)")
    print("-" * 65)
    # TODO: Generate predictions and calculate accuracy_score and confusion_matrix
    # TODO: Print prescriptive clinical intervention recommendations
    pass


def run_analytics_lifecycle():
    """
    Facade Orchestrator function.
    """
    print("=" * 65)
    print("STARTING HEALTHCARE CLASSIFICATION LIFECYCLE (Out of 40 Marks)")
    print("=" * 65)
    
    df = phase_1_discovery_and_setup()
    # df = phase_2_supervised_segmentation(df)
    # model, X, y = phase_3_classification_modeling(df)
    # phase_4_model_evaluation(model, X, y)


if __name__ == "__main__":
    run_analytics_lifecycle()