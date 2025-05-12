import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
csv_file = '/home/crystal/Memoire_Vault/Glass/WK-6-ASSIGNMENT/loads.csv'
df = pd.read_csv(csv_file)

# Visualization 1: Line chart (Simulated data for trends over time)
df['Year'] = [2020, 2021, 2022] 

plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Age'], marker='o', linestyle='-', color='b')
plt.title('Trends in Age Over Time', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Age', fontsize=12)
plt.grid(True)
plt.savefig('line_chart.png') 
plt.close() 

# Visualization 2: Bar chart (Average Age by City)
plt.figure(figsize=(10, 6))
sns.barplot(x='City', y='Age', data=df, palette='viridis')
plt.title('Average Age by City', fontsize=14)
plt.xlabel('City', fontsize=12)
plt.ylabel('Average Age', fontsize=12)
plt.savefig('bar_chart.png')  
plt.close()

# Visualization 3: Histogram (Age Distribution)
plt.figure(figsize=(10, 6))
plt.hist(df['Age'], bins=5, color='skyblue', edgecolor='black')
plt.title('Age Distribution', fontsize=14)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True)
plt.savefig('histogram.png')  
plt.close()

# Visualization 4: Scatter plot (Age vs. City)
df['City_Code'] = df['City'].astype('category').cat.codes

plt.figure(figsize=(10, 6))
plt.scatter(df['City_Code'], df['Age'], color='green')
plt.title('Scatter Plot: Age vs. City', fontsize=14)
plt.xlabel('City (Numeric Code)', fontsize=12)
plt.ylabel('Age', fontsize=12)
plt.xticks(df['City_Code'], df['City'])
plt.grid(True)
plt.savefig('scatter_plot.png') 
plt.close()
