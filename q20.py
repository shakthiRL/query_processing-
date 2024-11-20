import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'San Francisco']
}
df = pd.DataFrame(data)

# Define the substring you want to search for
substring = 'New'

# Find the index of rows where the 'City' column contains the substring
indices = df[df['City'].str.contains(substring, case=False, na=False)].index

print(f"Indices of rows where 'City' contains the substring '{substring}':")
print(indices)