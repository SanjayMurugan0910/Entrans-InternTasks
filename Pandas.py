import pandas as pd

# 1️⃣ Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'],
    'Salary': [50000, 60000, 70000, 80000, 55000]
}

df = pd.DataFrame(data)

# 2️⃣ Display the DataFrame
print("Original DataFrame:")
print(df)

# 3️⃣ Access Columns
print("\nNames column:")
print(df['Name'])
# 4️⃣ Filter Rows
print("\nPeople with Salary > 55000:")
print(df[df['Salary'] > 55000])

# 5️⃣ Add a New Column
df['Bonus'] = df['Salary'] * 0.10
print("\nAfter Adding Bonus Column:")
print(df)

# 6️⃣ Basic Statistics
print("\nDescriptive Statistics:")
print(df.describe())

# 7️⃣ Sort Data
print("\nSorted by Salary (Descending):")
print(df.sort_values(by='Salary', ascending=False))
