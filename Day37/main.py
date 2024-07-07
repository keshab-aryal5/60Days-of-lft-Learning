import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [70000, 80000, 55000, 90000, 60000]
}
df = pd.DataFrame(data)

print("Initial DataFrame:")
print(df)

df['Bonus'] = df['Salary'] * 0.10
df['Age'] = df['Age'].astype(float)
df.rename(columns={'Salary': 'Annual Salary', 'Bonus': 'Annual Bonus'}, inplace=True)
df_filtered = df[df['Age'] > 25]

print("\nFiltered DataFrame:")
print(df_filtered)

mean_age = df['Age'].mean()
total_salary = df['Annual Salary'].sum()
df['Salary to Age Ratio'] = df['Annual Salary'] / df['Age']

print("\nStatistics:")
print(f"Mean Age: {mean_age}")
print(f"Total Salary: {total_salary}")

grouped_city = df.groupby('City').mean()

print("\nGrouped by City:")
print(grouped_city)

df_sorted = df.sort_values(by='Annual Salary', ascending=False)

print("\nSorted DataFrame:")
print(df_sorted)

pivot = df.pivot_table(values='Annual Salary', index='City', columns='Age', aggfunc=np.mean)

print("\nPivot Table:")
print(pivot)

df['Age Category'] = pd.cut(df['Age'], bins=[20, 25, 30, 35], labels=['20-25', '25-30', '30-35'])

df_dropped = df.drop(columns=['Salary to Age Ratio'])

df['Age'] = df['Age'].apply(lambda x: x + 1)

df['Salary Increment'] = df['Annual Salary'].apply(lambda x: x * 1.05)

df_merged = pd.merge(df, df_filtered, on='Name', suffixes=('_original', '_filtered'))

print("\nMerged DataFrame:")
print(df_merged)

age_salary_corr = df['Age'].corr(df['Annual Salary'])

print("\nCorrelation between Age and Salary:")
print(age_salary_corr)

plt.figure(figsize=(10, 6))
plt.bar(df['Name'], df['Annual Salary'])
plt.xlabel('Name')
plt.ylabel('Annual Salary')
plt.title('Annual Salary of Employees')
plt.show()

df['Annual Salary'].plot(kind='hist', bins=10, title='Salary Distribution')
plt.show()

df.to_csv('data.csv', index=False)
df_loaded = pd.read_csv('data.csv')

print("\nLoaded DataFrame from CSV:")
print(df_loaded)
