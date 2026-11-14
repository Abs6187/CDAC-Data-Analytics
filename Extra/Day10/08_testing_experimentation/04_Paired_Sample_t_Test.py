import numpy as np
from scipy import stats
'''
Scenario: Testing whether employee blood pressure dropped after participating in a 
6-week corporate wellness program (comparing the same group at two different times).
'''

# ==============================================================================
# EXAMPLE 2: PAIRED SAMPLE t-TEST (Dependent t-Test)
# ==============================================================================
# Step 1: State the Hypotheses
#   - H_0: The average change in blood pressure after the program is 0 (no effect).
#   - H_a: The average change in blood pressure is not 0 (the program had an effect).

# Step 2: Choose the Significance Level
alpha = 0.05


# Step 3: Select the Appropriate Test & Collect Sample Data
# We are comparing measurements from the same employees before and after.
np.random.seed(42)
bp_before = np.random.normal(loc=140, scale=12, size=25)  # Pre-program BP
bp_after = bp_before - np.random.normal(loc=6, scale=4, size=25)  # Post-program BP (dropped by ~6 points)

# Step 4: Calculate the Test Statistic and p-value
t_stat, p_value = stats.ttest_rel(bp_before, bp_after)

print(f"\n--- PAIRED SAMPLE t-TEST RESULTS ---")
print(f"Test Statistic (t): {t_stat:.4f}")
print(f"p-value:            {p_value:.4f}\n")

# Step 5: Make a Decision
if p_value <= alpha:
    decision = "Reject H_0 (Significant change in blood pressure detected!)"
else:
    decision = "Fail to Reject H_0 (No statistically significant change)"
print(f"Decision: {decision}")

# Step 6: Interpret the Conclusion
if p_value <= alpha:
    print("Conclusion: The wellness program successfully lowered employee blood pressure.")
    print("Business Action: Expand the wellness program company-wide.")
else:
    print("Conclusion: The observed blood pressure change could be random variation.")