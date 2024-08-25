import pandas as pd

def transform():
    df = pd.read_csv('data/orders/orders.csv')

    print(df.head())

    return df

