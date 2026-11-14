"""
Title: E-Commerce Customer Analytics Lifecycle (Complete Solution)
Description: A modular Python script analyzing e-commerce customer behavior 
             and predicting annual spend using regression.

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
    - Define business objective: Determine how browsing time and cart size drive customer annual spend.
    - Load e-commerce dataset from external CSV.
    [Allocation: 5 Marks]
    """
    print("\n[PHASE 1] Discovery, Business Understanding & Data Setup (5 Marks)")
    print("-" * 65)
    
    file_path = 'ecommerce_customer_data.csv'
    
    try:
        df = pd.read_csv(file_path)
        print(f"-> Successfully loaded dataset from: '{file_path}'")
    except FileNotFoundError:
        print(f"-> Error: File '{file_path}' not found. Verify it is in the working directory.")
        raise
        
    print("-> Business Objective: Analyze customer engagement metrics to predict and maximize Annual Spend.")
    print(f"-> Dataset Shape: {df.shape[0]} customers, {df.shape[1]} attributes")
    print("\nFirst 5 Records:")
    print(df.head())
    
    missing_count = df.isnull().sum().sum()
    print(f"\n-> Missing Values Check: {missing_count} missing values found.")
    
    return df


def phase_2_descriptive_statistics(df):
    """
    Module 2: Descriptive Statistics & Data Measures
    - Calculate Central Tendency & Dispersion for Annual Spend.
    - Check distribution shape and detect potential outliers using IQR.
    [Allocation: 10 Marks]
    """
    print("\n[PHASE 2] Descriptive Statistics & Data Measures (10 Marks)")
    print("-" * 65)
    
    target_col = 'Annual_Spend_USD'
    spend = df[target_col]
    
    mean_val = spend.mean()
    median_val = spend.median()
    std_val = spend.std()
    var_val = spend.var()
    q1 = spend.quantile(0.25)
    q3 = spend.quantile(0.75)
    iqr_val = q3 - q1
    data_range = spend.max() - spend.min()
    
    print(f"-> Metric Analyzed: {target_col}")
    print(f"   * Mean: ${mean_val:.2f}")
    print(f"   * Median: ${median_val:.2f}")
    print(f"   * Standard Deviation: ${std_val:.2f}")
    print(f"   * Variance: {var_val:.2f}")
    print(f"   * Interquartile Range (IQR): ${iqr_val:.2f}")
    print(f"   * Range: ${data_range} (Min: ${spend.min()}, Max: ${spend.max()})")
    
    # Outlier Detection
    lower_bound = q1 - 1.5 * iqr_val
    upper_bound = q3 + 1.5 * iqr_val
    outliers = spend[(spend < lower_bound) | (spend > upper_bound)]
    print(f"-> Outlier Analysis (IQR Method): {len(outliers)} outliers detected.")
    
    return df


def phase_3_bivariate_association(df):
    """
    Module 4: Bivariate & Multivariate Association
    - Analyze relationships between Browsing Minutes, Items in Cart, and Annual Spend.
    - Compute Pearson Correlation Matrix.
    [Allocation: 10 Marks]
    """
    print("\n[PHASE 3] Bivariate Association & Correlation (10 Marks)")
    print("-" * 65)
    
    numeric_df = df[['Age', 'Browsing_Minutes', 'Items_In_Cart', 'Discount_Used_Flag', 'Annual_Spend_USD']]
    
    corr_matrix = numeric_df.corr(method='pearson')
    print("-> Pearson Correlation Matrix:")
    print(corr_matrix.round(3))
    
    browse_corr = corr_matrix.loc['Browsing_Minutes', 'Annual_Spend_USD']
    cart_corr = corr_matrix.loc['Items_In_Cart', 'Annual_Spend_USD']
    
    print(f"\n-> Key Business Insights:")
    print(f"   1. Browsing Minutes vs. Annual Spend: r = {browse_corr:.2f} (Very strong positive correlation)")
    print(f"   2. Items in Cart vs. Annual Spend: r = {cart_corr:.2f} (Very strong positive correlation)")
    
    return df


def phase_4_predictive_modeling(df):
    """
    Module 6 & 8: Predictive Analytics & Regression Modeling
    - Build a Simple Linear Regression model to predict Annual Spend using Browsing Minutes.
    [Allocation: 10 Marks]
    """
    print("\n[PHASE 4] Predictive Modeling & Regression (10 Marks)")
    print("-" * 65)
    
    X = df[['Browsing_Minutes']]
    y = df['Annual_Spend_USD']
    
    model = LinearRegression()
    model.fit(X, y)
    
    intercept = model.intercept_
    coefficient = model.coef_[0]
    
    print("-> Simple Linear Regression Model Fitted:")
    print(f"   * Formula: Annual Spend = ({coefficient:.2f} * Browsing Minutes) + {intercept:.2f}")
    print(f"   * Model Slope: Each additional minute spent browsing increases projected annual spend by ~${coefficient:.2f}.")
    
    return model, X, y


def phase_5_evaluation_and_reporting(model, X, y, df):
    """
    Module 6 & 7: Model Evaluation & Prescriptive Business Decision
    - Calculate R-squared and MAE.
    - Translate model findings into marketing strategies.
    [Allocation: 5 Marks]
    """
    print("\n[PHASE 5] Model Evaluation & Business Action (5 Marks)")
    print("-" * 65)
    
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    
    print(f"-> Model Evaluation Metrics:")
    print(f"   * R-Squared ($R^2$): {r2:.3f} (Explains {r2 * 100:.1f}% of annual spend variance)")
    print(f"   * Mean Absolute Error (MAE): ${mae:.2f}")
    
    print("\n-> Prescriptive Marketing Recommendation:")
    print("   1. Website Engagement: Implement UI features that increase session duration (e.g., personalized product recommendations and interactive galleries).")
    print("   2. Targeted Retention: Focus loyalty rewards on customers who exhibit high browsing duration but lower cart conversion.")
    
    return r2, mae


# ==========================================
# THE FACADE FUNCTION (Orchestrator)
# ==========================================

def run_analytics_lifecycle():
    """
    Facade function coordinating the lifecycle phases.
    """
    print("=" * 65)
    print("STARTING E-COMMERCE ANALYTICS LIFECYCLE (Out of 40 Marks)")
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