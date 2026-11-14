# ==============================================================================
# THE 6 STEPS OF HYPOTHESIS TESTING
# ==============================================================================
# 1. State the Hypotheses (H_0 and H_a)
# 2. Choose the Significance Level (alpha, e.g., 0.05)
# 3. Select the Appropriate Test (e.g., Independent t-test, ANOVA, Chi-Square)
# 4. Calculate the Test Statistic and p-value from the sample data
# 5. Make a Decision (Reject H_0 if p-value <= alpha, otherwise Fail to Reject H_0)
# 6. Interpret the Conclusion in plain English / business context
# ==============================================================================
import numpy as np
from scipy import stats

# ==============================================================================
# STEP 1: State the Hypotheses
# ==============================================================================
# H_0 (Null Hypothesis): The average spend for Website Design A equals Design B.
# H_a (Alternative Hypothesis): The average spend for Website Design A differs from Design B.

# ==============================================================================
# STEP 2: Choose the Significance Level
# ==============================================================================
alpha = 0.05  # 5% skepticism threshold

# ==============================================================================
# STEP 3: Select the Appropriate Test
# ==============================================================================
# We are comparing the means of two independent groups -> Independent Two-Sample t-test

# Generate sample data for customer spending under two designs
np.random.seed(42)
design_a = np.random.normal(loc=55, scale=10, size=30)  # Average spend ~$55
design_b = np.random.normal(loc=63, scale=12, size=30)  # Average spend ~$63

# ==============================================================================
# STEP 4: Calculate the Test Statistic and p-value
# ==============================================================================
t_stat, p_value = stats.ttest_ind(design_a, design_b)

print(f"--- HYPOTHESIS TEST RESULTS ---")
print(f"Test Statistic (t): {t_stat:.4f}")
print(f"p-value:            {p_value:.4f}\n")

# ==============================================================================
# STEP 5: Make a Decision
# ==============================================================================
if p_value <= alpha:
    decision = "Reject H_0 (Statistically significant difference found!)"
else:
    decision = "Fail to Reject H_0 (Not enough evidence to reject status quo)"

print(f"Decision: {decision}\n")

# ==============================================================================
# STEP 6: Interpret the Conclusion in Plain English / Business Context
# ==============================================================================
if p_value <= alpha:
    print("Conclusion: Customer spending differs significantly between the two designs.")
    print("Business Action: Roll out Website Design B; the increase in spend is unlikely due to random luck.")
else:
    print("Conclusion: Any observed difference in spending could easily be random variation.")
    print("Business Action: Keep testing or retain the current design.")