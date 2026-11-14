import numpy as np
from sklearn.metrics import confusion_matrix,precision_recall_curve

y_true = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1]) # 5 actual normal, 5 actual spam
y_pred = np.array([0, 0, 1, 0, 1, 0, 1, 1, 1, 1])  # What the model predicted

# 2. Compute the Confusion Matrix
cm = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:\n", cm) # # Order in scikit-learn: [[TN, FP], [FN, TP]]
tn, fp, fn, tp = cm.ravel()
print("\n--- Breakdown of Cases ---")
print(f"True Negatives (TN): {tn} -> Correctly caught normal emails")
print(f"False Positives (FP): {fp} -> Normal emails incorrectly flagged as spam (False Alarms)")
print(f"False Negatives (FN): {fn} -> Spam emails that slipped through into the inbox")
print(f"True Positives (TP): {tp} -> Correctly caught spam emails")

# 4. Working with Probabilities for Precision-Recall Curve
# Let's assume these are the model's predicted probabilities of being Spam (Class 1)
y_probs = np.array([0.1, 0.2, 0.6, 0.3, 0.7, 0.4, 0.8, 0.9, 0.85, 0.95])

precision, recall, thresholds = precision_recall_curve(y_true, y_probs)
print("\n--- Precision-Recall Curve Outputs ---")
print("Thresholds:", thresholds)
print("Precision:", precision)
print("Recall:", recall)