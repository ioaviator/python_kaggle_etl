import sqlalchemy as sa
import pandas as pd

def load(df:pd.DataFrame) -> None:

    '''
        Load transformed data into the data warehouse

        args:
            df(DataFrame): data to be loaded into the data warehouse
    '''

    #connect to database
    engine = sa.create_engine('mssql+pyodbc://AVIATOR/ecommerce?driver=ODBC+Driver+17+for+SQL+Server')

    # load data into database table
    df.to_sql(name='orders', con=engine, index=False, if_exists='replace')

    return None