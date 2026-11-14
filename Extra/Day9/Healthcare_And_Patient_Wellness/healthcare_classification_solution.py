"""
Title: Healthcare Classification Lifecycle (Complete Solution)
Description: Module 7 Supervised Segmentation & Classification demonstration script.
Total Evaluation Marks: 40 Marks
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ==========================================
# SUB-STEP FUNCTIONS (The Lifecycle Phases)
# ==========================================

def phase_1_discovery_and_setup():
    """
    Module 1 & 7: Discovery & Class Distribution Setup
    - Load classification dataset.
    - Inspect target variable balance.
    [Allocation: 5 Marks]
    """
    print("\n[PHASE 1] Discovery & Data Setup (5 Marks)")
    print("-" * 65)
    
    file_path = 'patient_classification_data.csv'
    df = pd.read_csv(file_path)
    
    print(f"-> Successfully loaded dataset: '{file_path}'")
    print(f"-> Dataset Shape: {df.shape[0]} patients, {df.shape[1]} attributes")
    
    class_counts = df['High_Risk_Hypertension'].value_counts()
    print("\n-> Target Class Distribution (High Risk Hypertension):")
    print(f"   * Normal/Low Risk (0): {class_counts.get(0, 0)} patients")
    print(f"   * High Risk (1): {class_counts.get(1, 0)} patients")
    
    return df


def phase_2_supervised_segmentation(df):
    """
    Module 7: Supervised Segmentation & Feature Profiling
    - Compare average feature attributes across risk segments.
    [Allocation: 10 Marks]
    """
    print("\n[PHASE 2] Supervised Segmentation & Profiling (10 Marks)")
    print("-" * 65)
    
    segmented = df.groupby('High_Risk_Hypertension')[['BMI', 'Daily_Steps', 'Age']].mean()
    print("-> Average Feature Profile by Risk Segment:")
    print(segmented.round(2))
    print("\n-> Insight: High-risk patients exhibit significantly higher BMI and lower daily step counts.")
    
    return df


def phase_3_classification_modeling(df):
    """
    Module 7: Rule-Based & Probabilistic Classification Models
    - Train a Logistic Regression classifier using BMI and Daily_Steps.
    [Allocation: 10 Marks]
    """
    print("\n[PHASE 3] Classification Model Induction (10 Marks)")
    print("-" * 65)
    
    X = df[['BMI', 'Daily_Steps']]
    y = df['High_Risk_Hypertension']
    
    model = LogisticRegression()
    model.fit(X, y)
    
    print("-> Logistic Regression Classifier Fitted successfully.")
    print(f"-> Model Intercept: {model.intercept_[0]:.3f}")
    print(f"-> Model Coefficients (Weights): BMI = {model.coef_[0][0]:.3f}, Daily_Steps = {model.coef_[0][1]:.3f}")
    
    return model, X, y


def phase_4_model_evaluation(model, X, y):
    """
    Module 7: Model Evaluation & Generalization
    - Evaluate accuracy and confusion matrix.
    - Translate results into clinical prescriptive actions.
    [Allocation: 15 Marks]
    """
    print("\n[PHASE 4] Model Evaluation & Clinical Action (15 Marks)")
    print("-" * 65)
    
    y_pred = model.predict(X)
    accuracy = accuracy_score(y, y_pred)
    conf_matrix = confusion_matrix(y, y_pred)
    
    print(f"-> Classifier Evaluation Metrics:")
    print(f"   * Overall Accuracy: {accuracy * 100:.1f}%")
    print(f"\n-> Confusion Matrix:\n{conf_matrix}")
    
    print("\n-> Prescriptive Clinical Recommendation:")
    print("   1. Automated Screening: Deploy this probabilistic classifier in patient portals to flag high-risk profiles based on wearable step counts and BMI.")
    print("   2. Targeted Interventions: Enroll classified high-risk cohorts into specialized cardiovascular wellness programs.")
    
    return accuracy


# ==========================================
# THE FACADE FUNCTION (Orchestrator)
# ==========================================

def run_analytics_lifecycle():
    """
    Facade function coordinating classification lifecycle phases.
    """
    print("=" * 65)
    print("STARTING HEALTHCARE CLASSIFICATION LIFECYCLE (Out of 40 Marks)")
    print("=" * 65)
    
    df = phase_1_discovery_and_setup()
    df = phase_2_supervised_segmentation(df)
    model, X, y = phase_3_classification_modeling(df)
    phase_4_model_evaluation(model, X, y)
    
    print("\n" + "=" * 65)
    print("CLASSIFICATION LIFECYCLE COMPLETED SUCCESSFULLY")
    print("=" * 65)


# ==========================================
# MAIN GUARD
# ==========================================
if __name__ == "__main__":
    run_analytics_lifecycle()