import pandas as pd
import numpy as np

# Create a sample DataFrame with some missing values
data = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12],
    'D': [np.nan, 14, 15, 16]
}
df = pd.DataFrame(data)

# Detect missing values
missing_values = df.isnull()

# Display the DataFrame with True for missing and False otherwise
print("Missing Values in the DataFrame:")
print(missing_values)