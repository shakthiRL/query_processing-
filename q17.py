import pandas as pd

# Create a sample DataFrame
data = {
    'school_code': ['S001', 'S002', 'S001', 'S003', 'S002', 'S001', 'S003'],
    'student_name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'age': [14, 15, 14, 16, 15, 14, 16]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Group the DataFrame by 'school_code' and calculate mean, min, and max age
result = df.groupby('school_code')['age'].agg(['mean', 'min', 'max'])

print("\nMean, Min, and Max age for each school:")
print(result)