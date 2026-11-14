import numpy as np
from scipy import stats
'''
Scenario: Testing whether the average test score of our class is significantly different from a 
known national average of 75.
'''
# ==============================================================================
# EXAMPLE 1: ONE-SAMPLE t-TEST
# ==============================================================================
# Step 1: State the Hypotheses
#   - H_0: The class mean test score equals the national average (mu = 75).
#   - H_a: The class mean test score differs from the national average (mu != 75).

# Step 2: Choose the Significance Level
alpha = 0.05  # 5% skepticism threshold

# Step 3: Select the Appropriate Test & Collect Sample Data
# We are comparing 1 group mean against a known target value.
np.random.seed(42)
class_scores = np.random.normal(loc=78, scale=8, size=30)  # Sample average ~78
national_average = 75

# Step 4: Calculate the Test Statistic and p-value
t_stat, p_value = stats.ttest_1samp(class_scores, national_average)

# Step 5: Make a Decision
if p_value <= alpha:
    decision = "Reject H_0 (Scores are significantly different from 75!)"
else:
    decision = "Fail to Reject H_0 (No significant difference from 75)"
print(f"Decision: {decision}")

# Step 6: Interpret the Conclusion
if p_value <= alpha:
    print("Conclusion: Our class performs significantly differently than the national average.")
else:
    print("Conclusion: Any difference from 75 could easily be due to random luck.")
