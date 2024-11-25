import pandas as pd
import chardet
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import re

# Ensure you have the NLTK resources downloaded
nltk.download('stopwords')
nltk.download('punkt')

# File Path
file_path = 'C:\\Users\\shakt\\Desktop\\query\\NSF Active Awards Query- Convolutional Neural Networks Images.csv'  # Replace with your file path

# Step 1: Detect the Encoding of the Dataset
try:
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())  # Detect the file encoding
    detected_encoding = result['encoding']
    print(f"Detected Encoding: {detected_encoding}")
except Exception as e:
    print(f"Error detecting encoding: {e}")
    detected_encoding = 'utf-8'  # Default encoding

# Step 2: Try Loading the Dataset with Detected Encoding
try:
    data = pd.read_csv(file_path, encoding=detected_encoding)
    print("Dataset loaded successfully.")
except Exception as e:
    print(f"An error occurred while loading the dataset: {e}")
    data = None  # Set 'data' to None if loading fails

# If loading the dataset fails, try using different encoding options
if data is None:
    try:
        # Try loading with ISO-8859-1 encoding
        data = pd.read_csv(file_path, encoding='ISO-8859-1')
        print("Dataset loaded successfully with ISO-8859-1 encoding.")
    except Exception as e:
        print(f"An error occurred while loading the dataset with ISO-8859-1 encoding: {e}")
        data = None  # Set 'data' to None if loading fails

if data is None:
    try:
        # Try loading with ignoring errors
        data = pd.read_csv(file_path, encoding='utf-8', errors='ignore')
        print("Dataset loaded successfully with UTF-8 encoding (ignoring errors).")
    except Exception as e:
        print(f"An error occurred while loading the dataset: {e}")
        data = None  # Set 'data' to None if loading fails

# Step 3: Data Preprocessing if Dataset Loaded Successfully
if data is not None:
    # Step 3a: Explore the Dataset
    print("\nDataset Head:")
    print(data.head())
    print("\nDataset Info:")
    print(data.info())
    print("\nMissing Values:")
    print(data.isnull().sum())

    # Step 3b: Data Cleaning
    data = data.drop_duplicates()  # Remove duplicates
    data = data.dropna(subset=['Title', 'Abstract'])  # Drop rows with critical missing values
    if 'Amount' in data.columns:
        data['Amount'] = data['Amount'].fillna(data['Amount'].mean())  # Fill missing values in 'Amount'
    data['Title'] = data['Title'].str.lower()  # Normalize text (convert to lowercase)
    data['Abstract'] = data['Abstract'].str.lower()
    data['Title'] = data['Title'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))  # Remove special characters
    data['Abstract'] = data['Abstract'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))

    # Step 3c: Feature Engineering
    data['Text'] = data['Title'] + ' ' + data['Abstract']  # Combine Title and Abstract into a single text field

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    data['Cleaned_Text'] = data['Text'].apply(
        lambda x: ' '.join([word for word in word_tokenize(x) if word not in stop_words])
    )

    # Extract top keywords using TF-IDF
    vectorizer = TfidfVectorizer(max_features=50)
    tfidf_matrix = vectorizer.fit_transform(data['Cleaned_Text'])
    keywords = vectorizer.get_feature_names_out()
    print("\nTop Keywords from TF-IDF:")
    print(keywords)

    # Step 3d: Label Creation for Intent Detection (Example)
    labeled_data = pd.DataFrame({
        'Query': [
            'AI projects by NIH',
            'Highest funded AI research',
            'AI projects in 2021'
        ],
        'Intent': [
            'filter_organization',
            'sort_amount',
            'filter_year'
        ]
    })
    print("\nExample Labeled Data:")
    print(labeled_data)

    # Step 3e: Split Data for Training and Testing
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

    # Save the Cleaned Dataset
    cleaned_file_path = 'cleaned_nsf_awards.csv'
    data.to_csv(cleaned_file_path, index=False)
    print(f"\nCleaned dataset saved to: {cleaned_file_path}")

    # Save Labeled Data (for training an intent detection model)
    labeled_file_path = 'labeled_intent_data.csv'
    labeled_data.to_csv(labeled_file_path, index=False)
    print(f"Labeled data saved to: {labeled_file_path}")

    # Final Outputs
    print("\nDataset Preprocessing Completed!")
else:
    print("\nFailed to load the dataset.")
