import pandas as pd
import chardet

def load_dataset(dataset_path):
    """
    Load a dataset with automatic encoding detection.
    """
    try:
        # Step 1: Detect file encoding
        with open(dataset_path, 'rb') as file:
            result = chardet.detect(file.read(10000))  # Analyze first 10,000 bytes
            detected_encoding = result['encoding']
            print(f"Detected Encoding: {detected_encoding}")

        # Step 2: Try loading dataset with detected encoding
        try:
            data = pd.read_csv(dataset_path, encoding=detected_encoding)
            print("Dataset Loaded Successfully with detected encoding!")
        except UnicodeDecodeError:
            print("Error decoding with detected encoding. Trying 'latin1' encoding.")
            data = pd.read_csv(dataset_path, encoding='latin1')  # Fallback to 'latin1'
        
        # Step 3: Display dataset summary
        print("\nDataset Preview:")
        print(data.head())
        print("\nDataset Info:")
        print(data.info())
        print("\nMissing Values in Each Column:")
        print(data.isnull().sum())

        return data

    except FileNotFoundError:
        print(f"Error: The dataset file '{dataset_path}' was not found.")
    except Exception as e:
        print(f"An error occurred while loading the dataset: {e}")

# Specify the dataset path
dataset_path = "C:\\Users\\shakt\\Desktop\\query\\NSF Active Awards Query- Convolutional Neural Networks Images.csv"  # Replace with your actual dataset file path

# Call the function to load the dataset
dataset = load_dataset(dataset_path)

