import pandas as pd

def transform() -> pd.DataFrame:
    '''
        clean and transform data

        return:
            df(DataFrame): transformed data ready to be used for analysis
    '''

    df = pd.read_csv('data/orders/orders.csv')

    print(df.head())

    return df

