import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)

def commit_to_database(data):
    df = pd.DataFrame([data])
    df.to_sql('earnings_data', engine, if_exists='append', index=False)
    return df