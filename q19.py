
import pandas as pd

# Simulating the World alcohol consumption dataset
data = {
    'Country': ['USA', 'Canada', 'Mexico', 'UK', 'Germany'],
    'Alcohol_Consumption': [8.0, 7.5, 6.3, 9.2, 10.1],
    'Beer': [5.0, 4.5, 3.2, 6.1, 7.2],
    'Wine': [2.5, 2.0, 1.8, 2.6, 3.0],
    'Spirits': [0.5, 1.0, 1.3, 0.5, 0.9]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the dimensions (shape) of the dataset
print("Dimensions of the dataset (rows, columns):")
print(df.shape)

# Extract and display the column names of the dataset
print("\nColumn names in the dataset:")
print(df.columns)
