import pandas as pd
data = {'Name': ['Alice', 'BOB', 'Charlie', 'david'],
        'Age': [25, 30, 35, 40]}

df = pd.DataFrame(data)

def swap_case_of_column(df, column_name):
    if column_name in df.columns:
        df[column_name] = df[column_name].str.swapcase()
    else:
        print(f"Column '{column_name}' not found in DataFrame.")
    return df
column_to_swap = 'Name'
df = swap_case_of_column(df, column_to_swap)
print(df)