import numpy as np
import pandas as pd
from sklearn.metrics import r2_score

# 1. Base dataset of 20 records
sq_ft = np.array([
    800, 950, 1100, 1200, 1350, 1500, 1650, 1800, 1950, 2100,
    2250, 2400, 2550, 2700, 2850, 3000, 3150, 3300, 3450, 3600
])
actual_prices = np.array([
    45, 52, 60, 65, 72, 80, 88, 95, 102, 110,
    118, 125, 132, 140, 148, 155, 162, 170, 178, 185
])
# Calculate the mean price (the "lazy baseline" guess)
mean_price = np.mean(actual_prices)

# 2. Create the 3 DataFrames for the 3 Scenarios

# --- DataFrame 1: Best Case (R² near 1.0) ---
# Predictions are almost identical to actual prices
pred_best = actual_prices + np.random.normal(0, 1.5, size=20) 
df_best = pd.DataFrame({
    'Sq_Ft': sq_ft,
    'Actual_Price': actual_prices,
    'Predicted_Price': pred_best
})
r2_best = r2_score(df_best['Actual_Price'], df_best['Predicted_Price'])

# --- DataFrame 2: Zero Case (R² = 0.0) ---
# Predictions are just the average price for every single house
df_zero = pd.DataFrame({
    'Sq_Ft': sq_ft,
    'Actual_Price': actual_prices,
    'Predicted_Price': [mean_price] * 20
})
r2_zero = r2_score(df_zero['Actual_Price'], df_zero['Predicted_Price'])

# --- DataFrame 3: Negative Case (R² < 0) ---
# Predictions are wildly backward (larger houses predicted to be cheaper)
pred_negative = actual_prices[::-1] + np.random.normal(0, 25, size=20)
df_negative = pd.DataFrame({
    'Sq_Ft': sq_ft,
    'Actual_Price': actual_prices,
    'Predicted_Price': pred_negative
})
r2_neg = r2_score(df_negative['Actual_Price'], df_negative['Predicted_Price'])

# 3. Display Results
print(f"--- 1. BEST CASE --- \nR2 Score: {r2_best:.4f}\n", df_best.head(3), "\n")
print(f"--- 2. ZERO CASE --- \nR2 Score: {r2_zero:.4f}\n", df_zero.head(3), "\n")
print(f"--- 3. NEGATIVE CASE --- \nR2 Score: {r2_neg:.4f}\n", df_negative.head(3), "\n")