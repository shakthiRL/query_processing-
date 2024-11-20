import pandas as pd
import numpy as np

# Create a DataFrame with 10 rows and 4 columns with random values
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])

# Function to highlight negative numbers in red and positive numbers in black
def highlight_negative_positive(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'

# Apply the styling function to the DataFrame
styled_df = df.style.applymap(highlight_negative_positive)

# Display the styled DataFrame
styled_df