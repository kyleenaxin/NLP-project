import pandas as pd

# original dataset
df = pd.read_csv("scomedy-comedians.csv")

# new dataset with birth_year
df_with_year = df.assign(
    birth_year = (
        df['bio'].str.extract(r"(?i)born[^0-9]{0,40}((19|20)\d{2})")[0]
        .fillna(df['bio'].str.extract(r"((19|20)\d{2})")[0])
        .astype("Int64")
    )
)

df_with_year.drop('bio', axis=1, inplace=True)
df_with_year.dropna 
df_with_year.to_csv('drop_na.csv', index=False)


def year_check(df):
    if df['birth_year'].isna().any():
        print("Missing Birth Year!")
    else:
        print("All good!")
    
year_check(df_with_year)