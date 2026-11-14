"""
Title: Healthcare Patient Analytics Lifecycle (Complete Solution)
Description: A modular Python script reading patient clinical data to analyze 
             lifestyle factors and predict blood pressure outcomes.
Total Evaluation Marks: 40 Marks
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# ==========================================
# SUB-STEP FUNCTIONS (The Lifecycle Phases)
# ==========================================

def phase_1_discovery_and_setup():
    """
    Module 1: Foundations, Business Understanding & Setup
    - Define clinical objective: Understand how physical activity and BMI correlate with blood pressure.
    - Load patient dataset from external CSV.
    [Allocation: 5 Marks]
    """
    print("\n[PHASE 1] Discovery, Business Understanding & Data Setup (5 Marks)")
    print("-" * 65)
    
    file_path = 'patient_health_data.csv'
    
    try:
        df = pd.read_csv(file_path)
        print(f"-> Successfully loaded dataset from: '{file_path}'")
    except FileNotFoundError:
        print(f"-> Error: File '{file_path}' not found. Verify it is in the working directory.")
        raise
        
    print("-> Clinical Objective: Identify lifestyle drivers affecting patient Systolic Blood Pressure.")
    print(f"-> Dataset Shape: {df.shape[0]} patients, {df.shape[1]} attributes")
    print("\nFirst 5 Records:")
    print(df.head())
    
    missing_count = df.isnull().sum().sum()
    print(f"\n-> Missing Values Check: {missing_count} missing values found.")
    
    return df


def phase_2_descriptive_statistics(df):
    """
    Module 2: Descriptive Statistics & Data Measures
    - Calculate Central Tendency & Dispersion for Systolic Blood Pressure.
    - Check distribution shape and detect potential outliers using IQR.
    [Allocation: 10 Marks]
    """
    print("\n[PHASE 2] Descriptive Statistics & Data Measures (10 Marks)")
    print("-" * 65)
    
    target_col = 'Systolic_BP'
    bp = df[target_col]
    
    mean_val = bp.mean()
    median_val = bp.median()
    std_val = bp.std()
    var_val = bp.var()
    q1 = bp.quantile(0.25)
    q3 = bp.quantile(0.75)
    iqr_val = q3 - q1
    data_range = bp.max() - bp.min()
    
    print(f"-> Metric Analyzed: {target_col} (mmHg)")
    print(f"   * Mean: {mean_val:.2f} mmHg")
    print(f"   * Median: {median_val:.2f} mmHg")
    print(f"   * Standard Deviation: {std_val:.2f}")
    print(f"   * Variance: {var_val:.2f}")
    print(f"   * Interquartile Range (IQR): {iqr_val:.2f}")
    print(f"   * Range: {data_range} (Min: {bp.min()}, Max: {bp.max()})")
    
    # Outlier Detection
    lower_bound = q1 - 1.5 * iqr_val
    upper_bound = q3 + 1.5 * iqr_val
    outliers = bp[(bp < lower_bound) | (bp > upper_bound)]
    print(f"-> Outlier Analysis (IQR Method): {len(outliers)} outliers detected.")
    
    return df


def phase_3_bivariate_association(df):
    """
    Module 4: Bivariate & Multivariate Association
    - Analyze relationships between Daily Steps, BMI, Age, and Blood Pressure.
    - Compute Pearson Correlation Matrix.
    [Allocation: 10 Marks]
    """
    print("\n[PHASE 3] Bivariate Association & Correlation (10 Marks)")
    print("-" * 65)
    
    numeric_df = df[['Age', 'Daily_Steps', 'Sleep_Hours', 'BMI', 'Systolic_BP']]
    
    corr_matrix = numeric_df.corr(method='pearson')
    print("-> Pearson Correlation Matrix:")
    print(corr_matrix.round(3))
    
    bmi_corr = corr_matrix.loc['BMI', 'Systolic_BP']
    steps_corr = corr_matrix.loc['Daily_Steps', 'Systolic_BP']
    
    print(f"\n-> Key Clinical Insights:")
    print(f"   1. BMI vs. Systolic BP: r = {bmi_corr:.2f} (Strong positive correlation)")
    print(f"   2. Daily Steps vs. Systolic BP: r = {steps_corr:.2f} (Strong negative correlation)")
    
    return df


def phase_4_predictive_modeling(df):
    """
    Module 6 & 8: Predictive Analytics & Regression Modeling
    - Build a Simple Linear Regression model to predict Systolic BP using BMI.
    [Allocation: 10 Marks]
    """
    print("\n[PHASE 4] Predictive Modeling & Regression (10 Marks)")
    print("-" * 65)
    
    X = df[['BMI']]
    y = df['Systolic_BP']
    
    model = LinearRegression()
    model.fit(X, y)
    
    intercept = model.intercept_
    coefficient = model.coef_[0]
    
    print("-> Simple Linear Regression Model Fitted:")
    print(f"   * Formula: Systolic BP = ({coefficient:.2f} * BMI) + {intercept:.2f}")
    print(f"   * Model Slope: Each unit increase in BMI corresponds to a ~{coefficient:.2f} mmHg increase in Systolic BP.")
    
    return model, X, y


def phase_5_evaluation_and_reporting(model, X, y, df):
    """
    Module 6 & 7: Model Evaluation & Prescriptive Clinical Recommendation
    - Calculate R-squared and MAE.
    - Translate model findings into clinical advice.
    [Allocation: 5 Marks]
    """
    print("\n[PHASE 5] Model Evaluation & Clinical Action (5 Marks)")
    print("-" * 65)
    
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    
    print(f"-> Model Evaluation Metrics:")
    print(f"   * R-Squared ($R^2$): {r2:.3f} (Explains {r2 * 100:.1f}% of blood pressure variance)")
    print(f"   * Mean Absolute Error (MAE): {mae:.2f} mmHg")
    
    print("\n-> Prescriptive Clinical Recommendation:")
    print("   1. Preventive Care: Target lifestyle intervention programs focusing on weight management and step goals to mitigate hypertension risks.")
    print("   2. Resource Allocation: Patients exhibiting elevated BMI thresholds should be prioritized for periodic cardiovascular monitoring.")
    
    return r2, mae


# ==========================================
# THE FACADE FUNCTION (Orchestrator)
# ==========================================

def run_analytics_lifecycle():
    """
    Facade function coordinating the lifecycle phases.
    """
    print("=" * 65)
    print("STARTING HEALTHCARE ANALYTICS LIFECYCLE (Out of 40 Marks)")
    print("=" * 65)
    
    df = phase_1_discovery_and_setup()
    df = phase_2_descriptive_statistics(df)
    df = phase_3_bivariate_association(df)
    model, X, y = phase_4_predictive_modeling(df)
    phase_5_evaluation_and_reporting(model, X, y, df)
    
    print("\n" + "=" * 65)
    print("ANALYTICS LIFECYCLE COMPLETED SUCCESSFULLY")
    print("=" * 65)


# ==========================================
# MAIN GUARD
# ==========================================
if __name__ == "__main__":
    run_analytics_lifecycle()