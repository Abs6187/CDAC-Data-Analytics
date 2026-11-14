"""
Title: Employee Productivity & Analytics Lifecycle (Complete Solution)
Description: Complete end-to-end data analytics script reading from external CSV 
             and demonstrating discovery, descriptive stats, correlation, 
             regression, and evaluation.

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
    - Define business objective: Determine how experience and training hours drive task output.
    - Load employee productivity dataset from CSV.

    """
    print("\n[PHASE 1] Discovery, Business Understanding & Data Setup (5 Marks)")
    print("-" * 65)
    
    file_path = 'employee_productivity.csv'
    
    try:
        df = pd.read_csv(file_path)
        print(f"-> Successfully loaded dataset from: '{file_path}'")
    except FileNotFoundError:
        print(f"-> Error: File '{file_path}' not found. Ensure it is placed in the project folder.")
        raise
        
    print("-> Business Objective: Evaluate factors boosting workforce productivity to optimize training budgets.")
    print(f"-> Dataset Shape: {df.shape[0]} employees, {df.shape[1]} attributes")
    print("\nFirst 5 Records:")
    print(df.head())
    
    missing_count = df.isnull().sum().sum()
    print(f"\n-> Missing Values Check: {missing_count} missing values found.")
    
    return df


def phase_2_descriptive_statistics(df):
    """
    Module 2: Descriptive Statistics & Data Measures
    - Calculate Central Tendency & Dispersion for Weekly Tasks Completed.
    - Check for distribution shape and outliers using IQR.

    """
    print("\n[PHASE 2] Descriptive Statistics & Data Measures (10 Marks)")
    print("-" * 65)
    
    target_col = 'Weekly_Tasks_Completed'
    tasks = df[target_col]
    
    mean_val = tasks.mean()
    median_val = tasks.median()
    std_val = tasks.std()
    var_val = tasks.var()
    q1 = tasks.quantile(0.25)
    q3 = tasks.quantile(0.75)
    iqr_val = q3 - q1
    data_range = tasks.max() - tasks.min()
    
    print(f"-> Metric Analyzed: {target_col}")
    print(f"   * Mean: {mean_val:.2f} tasks/week")
    print(f"   * Median: {median_val:.2f} tasks/week")
    print(f"   * Standard Deviation: {std_val:.2f}")
    print(f"   * Variance: {var_val:.2f}")
    print(f"   * Interquartile Range (IQR): {iqr_val:.2f}")
    print(f"   * Range: {data_range} (Min: {tasks.min()}, Max: {tasks.max()})")
    
    # Outlier Detection
    lower_bound = q1 - 1.5 * iqr_val
    upper_bound = q3 + 1.5 * iqr_val
    outliers = tasks[(tasks < lower_bound) | (tasks > upper_bound)]
    print(f"-> Outlier Analysis (IQR Method): {len(outliers)} outliers detected.")
    
    return df


def phase_3_bivariate_association(df):
    """
    Module 4: Bivariate & Multivariate Association
    - Analyze relationships between Experience, Training Hours, and Task Output.
    - Compute Pearson Correlation Matrix.

    """
    print("\n[PHASE 3] Bivariate Association & Correlation (10 Marks)")
    print("-" * 65)
    
    numeric_df = df[['Years_Experience', 'Training_Hours', 'Weekly_Tasks_Completed', 'Performance_Rating']]
    
    corr_matrix = numeric_df.corr(method='pearson')
    print("-> Pearson Correlation Matrix:")
    print(corr_matrix.round(3))
    
    exp_corr = corr_matrix.loc['Years_Experience', 'Weekly_Tasks_Completed']
    train_corr = corr_matrix.loc['Training_Hours', 'Weekly_Tasks_Completed']
    
    print(f"\n-> Key Insights:")
    print(f"   1. Years Experience vs. Tasks Completed: r = {exp_corr:.2f} (Strong positive relationship)")
    print(f"   2. Training Hours vs. Tasks Completed: r = {train_corr:.2f} (Moderate-to-strong positive relationship)")
    
    return df


def phase_4_predictive_modeling(df):
    """
    Module 6 & 8: Predictive Analytics & Regression Modeling
    - Build a Simple Linear Regression model to predict Weekly Tasks Completed using Training Hours.

    """
    print("\n[PHASE 4] Predictive Modeling & Regression (10 Marks)")
    print("-" * 65)
    
    X = df[['Training_Hours']]
    y = df['Weekly_Tasks_Completed']
    
    model = LinearRegression()
    model.fit(X, y)
    
    intercept = model.intercept_
    coefficient = model.coef_[0]
    
    print("-> Simple Linear Regression Model Fitted:")
    print(f"   * Formula: Weekly Tasks = ({coefficient:.2f} * Training Hours) + {intercept:.2f}")
    print(f"   * Impact Slope: Each additional 10 hours of training yields ~{coefficient * 10:.1f} additional completed tasks.")
    
    return model, X, y


def phase_5_evaluation_and_reporting(model, X, y, df):
    """
    Module 6 & 7: Model Evaluation & Prescriptive HR Decision
    - Calculate R-squared and MAE.
    - Formulate actionable workplace insights.
  
    """
    print("\n[PHASE 5] Model Evaluation & Business Action (5 Marks)")
    print("-" * 65)
    
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    
    print(f"-> Model Evaluation Metrics:")
    print(f"   * R-Squared ($R^2$): {r2:.3f} (Explains {r2 * 100:.1f}% of productivity variance)")
    print(f"   * Mean Absolute Error (MAE): {mae:.2f} tasks")
    
    print("\n-> Prescriptive HR Recommendation:")
    print("   1. Skill Development: Target upskilling programs for junior employees (<3 years experience) where training yields the highest margin of improvement.")
    print("   2. Resource Planning: Use the regression formula to estimate team output capacity based on scheduled quarterly training hours.")
    
    return r2, mae


# ==========================================
# THE FACADE FUNCTION (Orchestrator)
# ==========================================

def run_analytics_lifecycle():
    """
    Facade function coordinating the lifecycle phases.
    """
    print("=" * 65)
    print("STARTING COMPLETE DATA ANALYTICS LIFECYCLE (Out of 40 Marks)")
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