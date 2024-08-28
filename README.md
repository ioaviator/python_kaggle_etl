# Data Pipeline Integration with Kaggle API, SQL Server, and Power BI

<br/>

# Project Description:
This project demonstrates an end-to-end data engineering workflow using Python, SQL Server, and Power BI. The primary goal is to connect to the Kaggle API using Python to download a specified dataset, perform data transformations with Pandas, load the transformed data into SQL Server, and visualize the data in Power BI.
<br />

# Requirements
- Python 3.8+
- Kaggle API Token
- Microsoft SQL Server

<br />

## Key components of the project include:

Data Acquisition: Using Python to connect to the Kaggle API and download datasets.

Data Transformation: Utilizing Pandas to clean, manipulate, and prepare the data for further analysis.

Data Loading: Storing the processed data into SQL Server for structured querying and management.

Data Visualization: Employing Power BI to create interactive and insightful visualizations from the SQL Server data.

<br>

## Data Pipeline Diagram

![Data Pipeline](./img/presentation.gif)


<br />

# Usage
- Generate kaggle api token, to be used for authentication. **[Generate Token](https://www.kaggle.com/docs/api)**
- Fork the repository
- Clone the repository to your local environment. ```
git clone https://repo-url```
- Navigate into the cloned repository, create a virtual environment. ```python -m venv venv```
- Activate the virtual environment ```source venv/Scripts/activate ``` or ``` source venv/bin/activate```
- Install package dependencies. ``` pip install -r requirements.txt```
- Modify connection to SQL Server database in ```etl/load.py```

```engine = sa.create_engine('mssql+pyodbc://[server_name]/database_name?driver=[SQL+Server_ODBC+Driver]')```

```df.to_sql(name='table_name', con=engine, index=False, if_exists='replace')```

#### Example

```engine = sa.create_engine('mssql+pyodbc://ioaviator/ecommerce?driver=ODBC+Driver+17+for+SQL+Server')```

```df.to_sql(name='orders', con=engine, index=False, if_exists='replace')```

- Run project ``` python main.py```

<br />

# Contribution/Modification

## Change the url to your dataset of choice using *utils/download_file.py*

```os.system(f'kaggle datasets download [account_name]/[dataset_name] -f new_filename.csv -p {download_dir}')```

#### Example

```os.system(f'kaggle datasets download ioaviator/retail-orders -f orders.csv -p {download_dir}')```

## Clean/transform the data using *etl/transform.py*

```
def transform() -> pd.DataFrame:
    '''
        clean and transform data

        return:
            df(DataFrame): transformed data ready to be used for analysis
    '''

    df = pd.read_csv('data/orders/orders.csv')

    print(df.head())

    return df 
```

## Load the transformed dataset into the created SQL Server database using *etl/load.py*

```
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
```

### Modify the database connection and table name

```engine = sa.create_engine('mssql+pyodbc://[server_name]/database_name?driver=[SQL+Server_ODBC+Driver]')```

```df.to_sql(name='table_name', con=engine, index=False, if_exists='replace')```

#### Example

```engine = sa.create_engine('mssql+pyodbc://ioaviator/ecommerce?driver=ODBC+Driver+17+for+SQL+Server')```

```df.to_sql(name='orders', con=engine, index=False, if_exists='replace')```