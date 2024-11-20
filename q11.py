import pandas as pd
import numpy as np

# Create a DataFrame with random values
np.random.seed(42)  # For reproducibility
data = np.random.randint(1, 100, size=(10, 4))
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

# Randomly assign some NaN values
nan_indices = [(2, 1), (4, 3), (6, 0), (8, 2)]
for row, col in nan_indices:
    df.iat[row, col] = np.nan

# Highlight NaN values
def highlight_nan(s):
    return ['background-color: yellow' if pd.isna(v) else '' for v in s]

styled_df = df.style.apply(highlight_nan, axis=1)

# Display the styled DataFrame
styled_df