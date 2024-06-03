import pandas as pd

data = {
    'Name': ['keshab','Ashok','Amrit','Suman'],
    'Age': [24, 27, 22, 32],
    'City': ['Kathmandu','Bhairahawa','Lalitpur','Bhaktapur']
}

df = pd.DataFrame(data)
print("DataFrame created from a dictionary:")
print(df)

print("\nBasic information about the DataFrame:")
print(df.info())


print("\nBasic statistics of the DataFrame:")
print(df.describe())

print("\nSelecting the 'Name' column:")
print(df['Name'])

print("\nSelecting the 'Name' and 'Age' columns:")
print(df[['Name', 'Age']])


print("\nFiltering rows where Age is greater than 25:")
print(df[df['Age'] > 25])


df['Salary'] = [50000, 60000, 55000, 65000]
print("\nDataFrame after adding a new column 'Salary':")
print(df)


df.to_csv('output.csv', index=False)
print("\nDataFrame saved to 'output.csv'")
