import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('avgIQpercountry.csv')

filtered_df = df[df['Average IQ'] >= 100]

filtered_df = filtered_df.sort_values(by="Average IQ", ascending=False)

print(filtered_df)

plt.figure(figsize=(14, 8))

bars = plt.bar(filtered_df['country'], filtered_df['Averaqe IQ'], color='skyblue')