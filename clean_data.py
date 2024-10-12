# Data Cleaning Example using Pandas
# Chunmay Aditya

import pandas as pd

# Load the dataset
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', None, 'David', 'Eva', 'Frank', 'Grace'],
    'Age': [25, 30, None, 22, 29, None, 40],
    'Score': [85, 90, 88, None, 95, 78, None]
})

print("Original DataFrame:")
print(df)

# 1. Remove duplicates
df = df.drop_duplicates()

# 2. Fill missing names with "Unknown"
df['Name'] = df['Name'].fillna("Unknown")

# 3. Fill missing ages with the mean age
df['Age'] = df['Age'].fillna(df['Age'].mean())

# 4. Fill missing scores with the median score
df['Score'] = df['Score'].fillna(df['Score'].median())

print("\nCleaned DataFrame:")
print(df)

# Save to CSV
df.to_csv("cleaned_data.csv", index=False)
print("\nData cleaned and saved to 'cleaned_data.csv'.")
