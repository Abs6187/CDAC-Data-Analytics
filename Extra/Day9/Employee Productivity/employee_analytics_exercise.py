"""
Title: Employee Productivity & Analytics Lifecycle 
Description: Fill in the TODO sections across the 5 lifecycle phases.

"""

# Step 0: Import necessary libraries
# TODO: Import pandas, numpy, scikit-learn LinearRegression, and metrics


def phase_1_discovery_and_setup():
    """
    [Phase 1] Discovery & Data Setup (5 Marks)
    - Goal: Load 'employee_productivity.csv' and inspect structure.
    - Check for null values and print summary info.
    """
    print("\n[PHASE 1] Discovery & Data Setup (5 Marks)")
    print("-" * 65)
    # TODO: Load CSV file using pandas
    # TODO: Print first 5 rows and verify shape
    # TODO: Check for missing values
    pass


def phase_2_descriptive_statistics(df):
    """
    [Phase 2] Descriptive Statistics & Data Measures (10 Marks)
    - Goal: Compute measures of central tendency and dispersion 
      for 'Weekly_Tasks_Completed'.
    - Check for potential outliers using IQR method.
    """
    print("\n[PHASE 2] Descriptive Statistics (10 Marks)")
    print("-" * 65)
    # TODO: Calculate Mean, Median, Std Dev, and IQR for Weekly_Tasks_Completed
    # TODO: Identify any values falling outside 1.5 * IQR bounds
    pass


def phase_3_bivariate_association(df):
    """
    [Phase 3] Bivariate Association & Correlation (10 Marks)
    - Goal: Examine relationships between Training Hours, Experience, 
      and Tasks Completed.
    - Compute Pearson correlation matrix.
    """
    print("\n[PHASE 3] Bivariate Association (10 Marks)")
    print("-" * 65)
    # TODO: Select numeric columns and compute Pearson correlation matrix
    # TODO: Highlight the correlation between Training_Hours and Weekly_Tasks_Completed
    pass


def phase_4_predictive_modeling(df):
    """
    [Phase 4] Predictive Analytics & Regression Modeling (10 Marks)
    - Goal: Predict 'Weekly_Tasks_Completed' based on 'Training_Hours'.
    - Train a Simple Linear Regression model.
    """
    print("\n[PHASE 4] Predictive Modeling (10 Marks)")
    print("-" * 65)
    # TODO: Set X = df[['Training_Hours']] and y = df['Weekly_Tasks_Completed']
    # TODO: Fit Linear Regression model and output slope & intercept
    pass


def phase_5_evaluation_and_reporting(model, X, y, df):
    """
    [Phase 5] Evaluation & Prescriptive Recommendation (5 Marks)
    - Goal: Evaluate model using R-squared and MAE.
    - Provide operational HR recommendations based on data.
    """
    print("\n[PHASE 5] Evaluation & HR Recommendations (5 Marks)")
    print("-" * 65)
    # TODO: Calculate R2 score and Mean Absolute Error (MAE)
    # TODO: Print prescriptive action item for employee training investments
    pass


def run_analytics_lifecycle():
    """
    Facade Orchestrator function.
    """
    print("=" * 65)
    print("STARTING EMPLOYEE ANALYTICS LIFECYCLE (Out of 40 Marks)")
    print("=" * 65)
    
    # Executing phases chronologically
    df = phase_1_discovery_and_setup()
    # df = phase_2_descriptive_statistics(df)
    # df = phase_3_bivariate_association(df)
    # model, X, y = phase_4_predictive_modeling(df)
    # phase_5_evaluation_and_reporting(model, X, y, df)


if __name__ == "__main__":
    run_analytics_lifecycle()