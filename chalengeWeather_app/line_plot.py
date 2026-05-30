from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('weather_tokyo_data.csv')

weather_tokyo_data = df.groupby('day')['temperature'].mean()

plt.figure(figsize=(10, 6))

weather_tokyo_data.plot(kind='line', marker='o', color='skyblue')

plt.title('Average weather by Continent')
plt.xlabel('day')
plt.ylabel('temperature')

plt.grid(axis='both', linestyle='--', alpha=0.7)

plt.show()