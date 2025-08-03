import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ts.csv', parse_dates=['Date'])
df.set_index('Date', inplace=True)

df_grouped = df.T.groupby(lambda col: col.split('_en.wikipedia.org')[0]).sum().T

df_grouped.to_csv('wikipeople_unimodal.csv')

df_grouped.iloc[:, :1].plot(figsize=(12, 5), title='Top 1 Person Page Views Over Time')
plt.xlabel('Date')
plt.ylabel('Page Views')
plt.grid(True)
plt.tight_layout()
plt.show()
