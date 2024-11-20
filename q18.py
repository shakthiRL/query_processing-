import pandas as pd

# Create a sample DataFrame
data = {
    'school_code': ['S001', 'S002', 'S001', 'S003', 'S002', 'S001', 'S003'],
    'class': ['10A', '10B', '10A', '10C', '10B', '10A', '10C'],
    'student_name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'age': [14, 15, 14, 16, 15, 14, 16]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Group by both 'school_code' and 'class'
grouped = df.groupby(['school_code', 'class'])

# Display groups
print("\nGroups formed based on 'school_code' and 'class':")
for (school, class_name), group in grouped:
    print(f"\nSchool Code: {school}, Class: {class_name}")
    print(group)