# ==============================================================================
# IS A Z-TEST A HYPOTHESIS TEST?
# ==============================================================================
# - YES! A Z-test is just another tool in the hypothesis testing toolkit.
# - It follows the exact same 6-step workflow as t-tests and ANOVA.
# - The only difference is the mathematical formula used to calculate the 
#   test statistic (using the Normal distribution instead of the t-distribution).
# ==============================================================================

# ==============================================================================
# WHERE DOES THE Z-TEST FIT?
# ==============================================================================
# - Category: Large Sample Tests / Parametric tests for means.
# - When to use: 
#   1. Sample size is large (n >= 30).
#   2. You KNOW the true population standard deviation (sigma).
# 
# - Z-test vs. t-test: 
#   - Z-test uses the Normal distribution (known population std dev).
#   - t-test uses the t-distribution (unknown population std dev, estimated from sample).
# 
# - Real-world note: In practice, we almost never know the population standard 
#   deviation, which is why t-tests are used 99% of the time instead of Z-tests.
# ==============================================================================

import numpy as np
from statsmodels.stats.weightstats import ztest

# ==============================================================================
# Z-TEST USING statsmodels
# ==============================================================================
# Step 1: State the Hypotheses
#   - H_0: The true population mean score equals 75 (mu = 75).
#   - H_a: The true population mean score differs from 75 (mu != 75).

# Step 2: Choose the Significance Level
alpha = 0.05

# Step 3: Select the Appropriate Test & Collect Large Sample Data (n >= 30)
np.random.seed(42)
sample_scores = np.random.normal(loc=77, scale=10, size=50)  # Large sample (n = 50)

# Step 4: Calculate the Test Statistic and p-value using statsmodels ztest
# value=75 specifies the hypothesized population mean under H_0
z_stat, p_value = ztest(sample_scores, value=75)

print(f"--- Z-TEST RESULTS ---")
print(f"Z-Statistic: {z_stat:.4f}")
print(f"p-value:     {p_value:.4f}\n")

# Step 5: Make a Decision
if p_value <= alpha:
    decision = "Reject H_0 (Mean score is significantly different from 75!)"
else:
    decision = "Fail to Reject H_0 (No significant difference from 75)"

print(f"Decision: {decision}\n")

# Step 6: Interpret the Conclusion
if p_value <= alpha:
    print("Conclusion: The sample average deviates significantly from the target value.")
    print("Business Action: Investigate why performance has shifted away from the benchmark.")
else:
    print("Conclusion: The difference could easily be due to random sampling variation.")
    print("Business Action: Maintain the status quo.")