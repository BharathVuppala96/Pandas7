import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    lowseries=accounts['income']<20000
    avgseries=(accounts['income']>=20000) & (accounts['income']<=50000)
    highseries=accounts['income']>50000
    low=lowseries.sum()
    high=highseries.sum()
    avg=avgseries.sum()
    return pd.DataFrame([['Low Salary',low],['Average Salary',avg],['High Salary',high]], columns=['category','accounts_count'])