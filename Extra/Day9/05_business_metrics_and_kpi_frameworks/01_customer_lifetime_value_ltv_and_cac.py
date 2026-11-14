import pandas as pd
import numpy as np

def CAC():
    # 1. Customer Acquisition Cost (CAC) Calculation
    df_cac = pd.DataFrame({
        'channel': ['Paid Search', 'Social Ads', 'Content SEO', 'Affiliates'],
        'spend': [12000, 15000, 4000, 8000],
        'customers_acquired': [200, 250, 100, 160]
    })

    print('=' * 60)
    print('-' * 60)
    df_cac['cac'] = df_cac['spend'] / df_cac['customers_acquired']
    print(df_cac)
    print('=' * 60)
    print('=' * 60)

def LTV(): # Customer lifeteime value
    '''
    LTV = (ARPU * GM)/r
    r = customer churn
    '''
    arpu = 60 # average revenue per user
    gross_margin = 0.8
    churn_rates = np.array([0.02, 0.05, 0.10, 0.20])
    df = pd.DataFrame({ 
        "churn_rate":churn_rates * 100,
        "ltv" : (arpu * gross_margin) / churn_rates
    })
    print('=' * 60)
    print('-' * 60)
   
    print(df)
    print('=' * 60)

def LtvToCac_Ratio():
    '''
    ratio = LTV/CAC
    payback_months = CAC/(ARPU * GM)
    '''
    df_unit = pd.DataFrame({
    'cohort': ['Q1 2026', 'Q2 2026', 'Q3 2026'],
    'ltv': [600, 750, 800],
    'cac': [150, 200, 180]
    })
    df_unit["ltv_cac_ratio"] = df_unit['ltv'] / df_unit['cac']
    df_unit["payback_months"] = df_unit['cac'] / (df_unit['ltv'] / 12) # monthly recovery

    print('=' * 60)
    print(df_unit)
    print('=' * 60)


if __name__ == "__main__":
    # CAC()
    # LTV()
    LtvToCac_Ratio()