# ==============================================================================
# CENTRAL LIMIT THEOREM (CLT) IN A NUTSHELL
# ==============================================================================
# 1. The Input: Start with ANY population shape (skewed, uniform, chaotic).
# 2. The Action: Take repeated random samples of size n (where n >= 30) 
#               and calculate the mean (average) of each sample.
# 3. The Result: The distribution of these sample means will ALWAYS form 
#               a Normal Distribution (Bell Curve).
# ==============================================================================
'''
In plain English, the Central Limit Theorem states: 
If you take enough random samples from any weird, lopsided, non-normal population, 
the distribution of their averages will always form a neat, symmetrical Bell Curve (Normal Distribution).
'''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# 1. Create a heavily skewed non-normal population (Exponential Distribution)
population = np.random.exponential(scale=2.0, size=10000)

# 2. Simulate taking 1,000 random samples (each of size n = 30)
sample_size = 30
num_samples = 1000
sample_means = []

for _ in range(num_samples):
    # Draw a random sample of size 30 from our skewed population
    sample = np.random.choice(population, size=sample_size)
    # Calculate and store the average of this sample
    sample_means.append(np.mean(sample))

# 3. Store the sample means in a Pandas DataFrame
df_means = pd.DataFrame({'Sample_Mean': sample_means})
# print(df_means)

# 4. Plotting the before and after comparison
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot A: The chaotic original population
axes[0].hist(population, bins=50, color='skyblue', edgecolor='black', density=True)
axes[0].set_title("1. Original Population (Exponential / Skewed)")
axes[0].set_xlabel("Value")
axes[0].set_ylabel("Density")

# Plot B: The sample means forming a Bell Curve
axes[1].hist(df_means['Sample_Mean'], bins=30, color='salmon', edgecolor='black', density=True)
axes[1].set_title(f"2. Distribution of Sample Means (n = {sample_size})\n(The Bell Curve Appears!)")
axes[1].set_xlabel("Sample Mean")
axes[1].set_ylabel("Density")

plt.tight_layout()
plt.show()

# Quick look at the DataFrame
print("First 5 rows of our Sample Means DataFrame:")
print(df_means.head())

'''
what is the differnce in CLT and [log1p, boxcox, yeo-jhonson]?
CLT never changes original data, takes random mean from multiple groups and make a bell.
others squish the outliers to fit inside the bell

log1p : Rule :0 and +ve  only : x>=0 (e.g., website clicks, sales counts, customer spend).
Box-cox : x >0
yeo-jhonson : all  : (e.g., profit/loss statements, temperature changes, temperature anomalies).


'''
# ==============================================================================
# RULE OF THUMB FOR CHOOSING A TRANSFORMER
# ==============================================================================
# 1. All numbers >= 0 and right-skewed?  --> Start with np.log1p()
# 2. All numbers strictly > 0?           --> Try Box-Cox
# 3. Mix of negative, zero, & positive?  --> Use Yeo-Johnson
# ==============================================================================

# ==============================================================================
# CLT vs. POWER TRANSFORMATIONS: THE DIFFERENCE
# ==============================================================================
# 1. Central Limit Theorem (CLT)
#    - What it is: A natural statistical law.
#    - Action: Take random sample averages of size n >= 30.
#    - Result: The *averages* form a bell curve, even if raw data is skewed.
#
# 2. Power Transformations (log1p, Yeo-Johnson)
#    - What it is: A manual data preprocessing / feature engineering step.
#    - Action: Apply math formulas to squash skewness in a specific column.
#    - Result: The *raw data points themselves* become more normally distributed.
# ==============================================================================