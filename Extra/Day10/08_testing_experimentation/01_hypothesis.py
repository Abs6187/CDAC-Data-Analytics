'''
Hypotheses Testing Flow
Step 1 : State Hypotheses | Define H_0 (null hypotheses) : Business as usual / status quo / 
                                   H_1 (your claim) (Alternative Hypothesis) : What are you trying to prove
                                   status quo (latin) = "the state in which" & " Exixting state of affirs.

Step 2 : Choose Significant | set your threshold (alpha , usualy 0.05 or 5%) : tolarence level (false alarm)

Step 3 Calculate p-value | How your data is under H_0 | p= probablity
                            if p<= 0.05 : reject : very unlikely |
                            if p_value > 0.05 : reject | result is a fluke, 
                            -------------------------------------------------------------------
                            If the p-value is LOW (p < 0.05):
                            
                            Action: Reject the status quo (Null Hypothesis).
                            
                            What it means: Your results are statistically significant. 
                            It is very unlikely (<5% chance) that random luck produced these numbers. 
                            You have strong evidence that something real is happening.
                            -------------------------------------------------------------------
                            If the p-value is HIGH (p > 0.05):
                            
                            Action: Fail to reject(ACCEPT) the status quo.
                            
                            What it means: Your results are not statistically significant. 
                            It is entirely possible that what you are seeing is just a random fluke or noise, 
                            so you stick with business as usual.


'''

'''
# ==============================================================================
# THE 4 STEPS OF THE HYPOTHESIS TESTING FRAMEWORK
# ==============================================================================
# Step 1: State Your Hypotheses (H_0 and H_a)
#   - H_0 (Null Hypothesis): "Business as usual" / status quo / no effect.
#   - H_a (Alternative Hypothesis): What you are trying to prove / your claim.
#
# Step 2: Choose Your Significance Level (alpha, usually 0.05 or 5%)
#   - Your "skepticism threshold" for falsely rejecting the null hypothesis.
#   - If result chance < 5% by random luck, it is considered statistically significant.
#
# Step 3: Calculate the p-value (The Surprise Metric)
#   - Answers: "If H_0 were true, how likely is data this extreme by random chance?"
#   - Low p-value (e.g., 0.01)  -> Data is super weird; H_0 is likely wrong.
#   - High p-value (e.g., 0.40) -> Could easily happen by luck; can't rule out H_0.
#
# Step 4: Make Your Decision
#   - If p-value <= alpha -> Reject H_0. Celebrate a statistically significant effect!
#   - If p-value > alpha  -> Fail to reject H_0. Stick with the status quo for now.
# ==============================================================================
'''

# ==============================================================================
# QUICK GUIDE TO CHOOSING A HYPOTHESIS TEST
# ==============================================================================
# Test Type               | What you are comparing
# ------------------------+-----------------------------------------------------
# One-Sample t-test       | 1 Group mean vs. a target value
# Independent t-test      | 2 Separate group means
# Paired t-test           | Same group at 2 different times (Before vs. After)
# ANOVA                   | 3 or More group means
# Chi-Square Test         | Relationships between categorical variables
# ==============================================================================


# ==============================================================================
# TYPES OF HYPOTHESIS TESTS
# ==============================================================================
# 1. The t-Family (Comparing Averages)
#    - One-Sample t-test:
#      - When to use: Compare the average of one group against a known standard or target value.
#      - Example: "Is the average test score of our class higher than the national average of 75?"
#    - Independent Two-Sample t-test:
#      - When to use: Compare the averages of two completely separate groups.
#      - Example: "Do customers who use Website Design A spend more money than customers using Website Design B?"
#    - Paired Sample t-test (Dependent t-test):
#      - When to use: Compare averages from the same group at two different times (before and after an event).
#      - Example: "Did employee blood pressure drop after a 6-week wellness program?"
#
# 2. Multi-Group & Categorical Tests
#    - ANOVA (Analysis of Variance):
#      - When to use: Compare the averages across three or more groups at the same time (t-tests only handle two).
#      - Example: "Is there a difference in sales performance across four different regional branches?"
#    - Chi-Square (chi^2) Test of Independence:
#      - When to use: Test if two categorical variables are related or independent.
#      - Example: "Is customer product preference (Electronics, Clothing, Home) independent of their age group?"
#
# 3. Large Sample Tests
#    - Z-test:
#      - When to use: Very similar to a t-test, but used when your sample size is large (n >= 30) and you know the population standard deviation.
# ==============================================================================

# ==============================================================================
# SUMMARY OF THE T-TEST FAMILY
# ==============================================================================
# 1. One-Sample T-Test
#    - What it compares: One group against a known target or standard.
#    - Simple Example: A cereal box claims to weigh 500 grams. You weigh 30 boxes 
#      and use a one-sample t-test to see if your batch's average weight is 
#      actually different from the 500-gram target.
#
# 2. Independent Two-Sample T-Test
#    - What it compares: Two completely separate groups.
#    - Simple Example: You give a new study guide to Class A and no study guide 
#      to Class B. You use an independent t-test to compare the average exam 
#      scores of these two different groups of students.
#    - (Note: There is a variation called Welch's t-test used when the two 
#      groups have very different spreads or sample sizes).
#
# 3. Paired Sample T-Test (Dependent T-Test)
#    - What it compares: The same group twice (usually "before and after").
#    - Simple Example: You measure the weight of 20 people, put them on a 30-day 
#      diet, and weigh those exact same 20 people again. You use a paired t-test 
#      to see if their average weight changed.
# ==============================================================================