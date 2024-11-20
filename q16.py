import pandas as pd

# Create a sample DataFrame
data = {
    'school_code': ['S001', 'S002', 'S001', 'S003', 'S002', 'S001', 'S003'],
    'student_name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'grade': [85, 90, 78, 92, 88, 75, 89]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Group the DataFrame by 'school_code'
grouped = df.groupby('school_code')

# Display the type of GroupBy object
print("\nType of GroupBy object:")
print(type(grouped))

# Display groups
print("\nGroups formed based on 'school_code':")
for name, group in grouped:
    print(f"\nSchool Code: {name}")
    print(group)