import pandas as pd

# Load dataset
file_path = 'C:\\Users\\shakt\\Desktop\\query\\NSF Active Awards Query- Convolutional Neural Networks Images.csv'
data = pd.read_csv(file_path)

# View dataset structure
print(data.head())
print(data.info())
print(data.isnull().sum())
print(data.describe())
print(data.sample(5))
data = data.drop_duplicates()
data = data.dropna(subset=['Title', 'Abstract'])
data = data.dropna(subset=['Title', 'Abstract'])
data['Title'] = data['Title'].str.lower()
data['Abstract'] = data['Abstract'].str.lower()
