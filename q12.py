import pandas as pd
import numpy as np

# Create a DataFrame with random values
np.random.seed(42)  # For reproducibility
data = np.random.randint(1, 100, size=(10, 4))
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

# Define a function to style the DataFrame with black background and yellow font
def style_black_and_yellow(s):
    return 'background-color: black; color: yellow;'

# Apply the style
styled_df = df.style.applymap(lambda _: 'background-color: black; color: yellow;')

# Display the styled DataFrame
styled_df