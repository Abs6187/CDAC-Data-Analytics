# ==============================================================================
# THE CHI-SQUARE (chi^2) TEST OF INDEPENDENCE
# ==============================================================================
# - While t-tests and ANOVA deal with numeric averages (like test scores, 
#   spend amounts, or blood pressure), the Chi-Square test handles categorical 
#   data (counts, frequencies, and categories like product choices, gender, or regions).
#
# - What it compares: Tests whether two categorical variables are related to each 
#   other (dependent) or completely independent.
#
# - Example: "Is customer product preference (Electronics vs. Clothing vs. Home) 
#   independent of their age group (Young vs. Old), or do younger customers 
#   prefer different products than older customers?"
# ==============================================================================

import numpy as np
from scipy import stats

# ==============================================================================
# CHI-SQUARE TEST OF INDEPENDENCE
# ==============================================================================
# Step 1: State the Hypotheses
#   - H_0: Product preference and age group are independent (no relationship).
#   - H_a: Product preference and age group are dependent (a relationship exists).

# Step 2: Choose the Significance Level
alpha = 0.05

# Step 3: Select the Appropriate Test & Create Contingency Table (Observed Counts)
# Rows: Age Groups (Young, Old)
# Columns: Product Preferences (Electronics, Clothing, Home)
observed_table = np.array([
    [50, 20, 30],  # Young customers
    [10, 40, 50]   # Older customers
])


# Step 4: Calculate Chi-Square Statistic, p-value, Degrees of Freedom, and Expected Frequencies
chi2_stat, p_value, dof, expected = stats.chi2_contingency(observed_table)


print(f"--- CHI-SQUARE TEST RESULTS ---")
print(f"Chi2 Statistic: {chi2_stat:.4f}")
print(f"p-value:        {p_value:.4f}\n")

# Step 5: Make a Decision
if p_value <= alpha:
    decision = "Reject H_0 (Variables are significantly dependent/related!)"
else:
    decision = "Fail to Reject H_0 (Variables appear independent)"
print(f"Decision: {decision}")

# Step 6: Interpret the Conclusion
if p_value <= alpha:
    print("Conclusion: Customer product preference is significantly associated with their age group.")
    print("Business Action: Tailor marketing campaigns and product recommendations by age demographic.")
else:
    print("Conclusion: Any observed pattern could be random variation.")