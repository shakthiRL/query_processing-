import pandas as pd
import numpy as np

# Create a sample DataFrame with missing values
data = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, np.nan, 3, 8],
    'C': [9, np.nan, 11, 12],
    'D': [np.nan, 14, 15, 16]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Replace missing values with a meaningful replacement (e.g., 0)
df_filled = df.fillna(0)

print("\nDataFrame after replacing missing values:")
print(df_filled)