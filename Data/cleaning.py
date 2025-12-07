import pandas as pd
import numpy as np

# original dataset
df_with_year = pd.read_csv("drop_na.csv")

def year_check(df):
    if df['birth_year'].isna().any():
        print("Missing Birth Year!")
    else:
        print("All good!")
    
year_check(df_with_year)




def year_index(df):
    missing_indices = []
    for idx, val in df['birth_year'].items():
        if pd.isna(val):
            missing_indices.append(idx)
    print(missing_indices)

year_index(df_with_year)