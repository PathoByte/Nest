import pandas as pd

# Path to my CSV file
csv_file = '/home/crystal/Memoire_Vault/Glass/WK-6-ASSIGNMENT/loads.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Display the first few rows
print(df.head())

# Display data types of each column
print("Data Types:")
print(df.dtypes)

# Check for missing values in each column
print("\nMissing Values:")
print(df.isnull().sum())

# Check for missing values
print("Missing Values before cleaning:")
print(df.isnull().sum())

# After cleaning, check the dataset again
print("\nDataset after cleaning:")
print(df.head())
