import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weather_tokyo_data.csv')

print(df.info())

df['full_date'] = pd.to_datetime(df['year'].astype(str) + '/' + df["day"], format='%Y/%m/%d')

df['temperature'] = df['temperature'].str.replace(r'\([^)]*\)', "", regex=True)

df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')

df = df.dropna()

df = df.sort_values(by="full_date")

print(df.info())

mean_temperature = df['temperature'].mean()
print(f"The average temperature for the entire dataset is {mean_temperature} C")

mean_temp_by_month = df.groupby(df["full_date"].dt.month)["temperature"].mean()
print("\n The mean temperature for each month is:\n", mean_temp_by_month)

plt.figure(figsize=(10, 6))
plt.bar(mean_temp_by_month.index, mean_temp_by_month.values)
plt.title('Mean Temperature by Month')
plt.xlabel("Month")
plt.ylabel('Mean Temperature (°C)')
plt.xticks(range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()