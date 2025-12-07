import pandas as pd

left = pd.read_csv("cleaned-data.csv")
right = pd.read_csv("combined.csv")


# df = df.drop('tags', axis = 1)
# df.to_csv('new_df.csv', index = False)

# quotes_by_comedian = (
#     df.groupby("comedian", as_index=False)
#       .agg({"text": lambda s: " || ".join(s)})
# )

# quotes_by_comedian.to_csv("combined.csv", index = False)


merged_df = pd.merge(left, right, on = 'comedian', how = 'inner')
merged_df.to_csv('merged.csv', index = False)