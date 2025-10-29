import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'],
    'Salary': [50000, 60000, 70000, 80000, 55000]
}

df = pd.DataFrame(data)

#  Display the DataFrame
print("Original DataFrame:")
print(df)

#  Access Columns
print("\nNames column:")
print(df['Name'])


print("\nPeople with Salary > 55000:")
print(df[df['Salary'] > 55000])

# Add a New Column
df['Bonus'] = df['Salary'] * 0.10
print("\nAfter Adding Bonus Column:")
print(df)

#  Basic Statistics
print("\nDescriptive Statistics:")
print(df.describe())

#  Sort Data
print("\nSorted by Salary (Descending):")
print(df.sort_values(by='Salary', ascending=False))
