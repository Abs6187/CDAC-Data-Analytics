"""
Title: E-Commerce Customer Analytics Lifecycle 
Description: Fill in the TODO sections across the 5 lifecycle phases using 
             'ecommerce_customer_data.csv'.

"""

# Step 0: Import necessary libraries
# TODO: Import pandas, numpy, LinearRegression from sklearn.linear_model, and evaluation metrics


def phase_1_discovery_and_setup():
    """
    [Phase 1] Discovery & Data Setup (5 Marks)
    - Goal: Load 'ecommerce_customer_data.csv' and inspect structure.
    - Check for null values and print summary info.
    """
    print("\n[PHASE 1] Discovery & Data Setup (5 Marks)")
    print("-" * 65)
    # TODO: Load CSV file using pandas
    # TODO: Print first 5 rows and verify dataset shape
    # TODO: Check for any missing values
    pass


def phase_2_descriptive_statistics(df):
    """
    [Phase 2] Descriptive Statistics & Data Measures (10 Marks)
    - Goal: Compute measures of central tendency and dispersion 
      for 'Annual_Spend_USD'.
    - Check for potential outliers using the IQR method.
    """
    print("\n[PHASE 2] Descriptive Statistics (10 Marks)")
    print("-" * 65)
    # TODO: Calculate Mean, Median, Std Dev, Variance, and IQR for Annual_Spend_USD
    # TODO: Identify any values falling outside 1.5 * IQR bounds
    pass


def phase_3_bivariate_association(df):
    """
    [Phase 3] Bivariate Association & Correlation (10 Marks)
    - Goal: Examine relationships between Browsing Minutes, Items in Cart, and Annual Spend.
    - Compute Pearson correlation matrix.
    """
    print("\n[PHASE 3] Bivariate Association (10 Marks)")
    print("-" * 65)
    # TODO: Select numeric columns and compute Pearson correlation matrix
    # TODO: Highlight correlations involving Annual_Spend_USD
    pass


def phase_4_predictive_modeling(df):
    """
    [Phase 4] Predictive Analytics & Regression Modeling (10 Marks)
    - Goal: Predict 'Annual_Spend_USD' based on 'Browsing_Minutes'.
    - Train a Simple Linear Regression model.
    """
    print("\n[PHASE 4] Predictive Modeling (10 Marks)")
    print("-" * 65)
    # TODO: Set X = df[['Browsing_Minutes']] and y = df['Annual_Spend_USD']
    # TODO: Fit Linear Regression model and output slope & intercept
    pass


def phase_5_evaluation_and_reporting(model, X, y, df):
    """
    [Phase 5] Evaluation & Prescriptive Recommendations (5 Marks)
    - Goal: Evaluate model performance using R-squared and MAE.
    - Provide prescriptive business recommendations based on findings.
    """
    print("\n[PHASE 5] Evaluation & Business Action (5 Marks)")
    print("-" * 65)
    # TODO: Calculate R2 score and Mean Absolute Error (MAE)
    # TODO: Print prescriptive marketing action items
    pass


def run_analytics_lifecycle():
    """
    Facade Orchestrator function.
    """
    print("=" * 65)
    print("STARTING E-COMMERCE ANALYTICS LIFECYCLE (Out of 40 Marks)")
    print("=" * 65)
    
    # Executing phases chronologically
    df = phase_1_discovery_and_setup()
    # df = phase_2_descriptive_statistics(df)
    # df = phase_3_bivariate_association(df)
    # model, X, y = phase_4_predictive_modeling(df)
    # phase_5_evaluation_and_reporting(model, X, y, df)


if __name__ == "__main__":
    run_analytics_lifecycle()