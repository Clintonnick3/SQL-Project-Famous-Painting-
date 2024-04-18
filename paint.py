# importing modules

import pandas as pd
from sqlalchemy import create_engine

# Creating engine and connecting to postgressql

engine = create_engine('postgresql://postgres:admin@localhost:5432/fampaint')


# reading csv files and storing in dataframe objects
files = ['canvas_size', 'image_link', 'museum_hours', 'museum', 'product_size', 'subject', 'work']

# storing csv files in dataframe 
for file in files:
    df = pd.read_csv(f'./{file}.csv')
    df.to_sql(file, engine, if_exists='replace', index=False)
    print(f'done {file}')
