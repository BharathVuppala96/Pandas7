import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    df=delivery[delivery['order_date']==delivery['customer_pref_delivery_date'] ]

    return pd.DataFrame([round(len(df)/len(delivery)*100,2)],columns=['immediate_percentage'])