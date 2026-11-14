import numpy as np
from scipy import stats
# ==============================================================================
# WHY USE ANOVA INSTEAD OF MULTIPLE t-TESTS?
# ==============================================================================
# If you have 4 different website designs and you want to compare them, 
# you might be tempted to run several independent t-tests between pairs 
# (Design A vs B, A vs C, B vs D, etc.).
#
# However, doing this drastically increases your risk of a False Positive 
# (Type I Error) due to compounding probability. 
#
# ANOVA solves this by comparing all groups simultaneously in a single 
# statistical test.
# ==============================================================================

# ==============================================================================
# ONE-WAY ANOVA TEST
# ==============================================================================
# Step 1: State the Hypotheses
#   - H_0: The average spending across all four regions is equal (mu_N = mu_S = mu_E = mu_W).
#   - H_a: At least one region has a significantly different average spending.

# Step 2: Choose the Significance Level
alpha = 0.05

# Step 3: Select the Appropriate Test & Collect Sample Data
# We are comparing averages across 4 separate groups -> One-Way ANOVA
np.random.seed(42)
region_north = np.random.normal(loc=50, scale=8, size=30)
region_south = np.random.normal(loc=53, scale=9, size=30)
region_east  = np.random.normal(loc=52, scale=7, size=30)
region_west  = np.random.normal(loc=65, scale=10, size=30) # Significantly higher spend

# Step 4: Calculate the Test Statistic (F-value) and p-value
f_stat, p_value = stats.f_oneway(region_north, region_south, region_east, region_west)

print(f"--- ONE-WAY ANOVA RESULTS ---")
print(f"F-Statistic: {f_stat:.4f}")
print(f"p-value:     {p_value:.4f}\n")


# Step 5: Make a Decision
if p_value <= alpha:
    decision = "Reject H_0 (At least one region's average spend differs significantly!)"
else:
    decision = "Fail to Reject H_0 (No significant difference across regions)"
print(f"Decision: {decision}")

# Step 6: Interpret the Conclusion
if p_value <= alpha:
    print("Conclusion: Regional location has a statistically significant impact on customer spending.")
    print("Business Action: Investigate why the West region performs differently (or market strategies there).")
else:
    print("Conclusion: Variation across regions could be due to random chance.")