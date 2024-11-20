import pandas as pd
import numpy as np

# Create a sample DataFrame with missing values
data = {
    'A': [1, np.nan, 3, 4],
    'B': [np.nan, np.nan, 6, 8],
    'C': [9, 10, np.nan, np.nan],
    'D': [np.nan, 14, 15, 16]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Keep rows with at least 2 NaN values
rows_with_2_nan = df[df.isnull().sum(axis=1) >= 2]

print("\nRows with at least 2 NaN values:")
print(rows_with_2_nan)