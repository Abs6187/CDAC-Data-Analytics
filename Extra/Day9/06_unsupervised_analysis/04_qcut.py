import pandas as pd
import numpy as np

df_rfm = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5],
    'recency_days': [2, 45, 120, 5, 300],
    'frequency': [12, 3, 1, 15, 1],
    'monetary': [2500, 450, 100, 3200, 80]
})

df_rfm['rfm_tier'] = pd.qcut(df_rfm['monetary'], q=2, labels=['Standard', 'VIP'])

print(
    "RFM Segmentation Summary:\n",
    df_rfm,
)
