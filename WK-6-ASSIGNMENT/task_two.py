import pandas as pd

# Load the dataset
csv_file = '/home/crystal/Memoire_Vault/Glass/WK-6-ASSIGNMENT/loads.csv'
df = pd.read_csv(csv_file)

# Compute basic statistics for numerical columns
print("Basic Statistics for Numerical Columns:")
print(df.describe())

# Group by 'City' and compute the mean of 'Age' for each group
print("\nMean Age for each City:")
grouped_df = df.groupby('City')['Age'].mean()
print(grouped_df)

