import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\archive (1)\\ai_financial_market_daily_realistic_synthetic.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df['Company'].unique())
d =df.groupby('Company')['R&D_Spending_USD_Mn'].sum()/1000
print(d)
plt.bar(d.index,d.values,color=['blue','black','red'])
plt.show()

m =df.groupby('Company')['AI_Revenue_USD_Mn'].sum()
print(m)
plt.bar(m.index,m.values,color=['blue','black','red'])
plt.title('AI Revenue by Company')
plt.xlabel('Company')
plt.ylabel('AI Revenue (in Million USD)')
plt.show()
plt.figure(figsize=(10,6)) 
plt.plot(df['Date'],df['Stock_Impact_%'],color='blue')
plt.title('AI Revenue Over Time')
plt.xlabel('Date')
plt.ylabel('AI Revenue (in Million USD)')
plt.show()

data_open = df[df['Company']=='OpenAI']
print(data_open)
 
data_open1 = df[df['Company']=='Meta']
print(data_open1)

data_open2 = df[df['Company']=='Meta']
print(data_open2)

n = data_open.sort_values(by='Stock_Impact_%',ascending=False)
print(n)


p = data_open2.sort_values(by='Stock_Impact_%',ascending=False)
print(p)

q = data_open1.sort_values(by='Stock_Impact_%',ascending=False)
print(q)

plt.plot(data_open['Date'],data_open['AI_Revenue_USD_Mn'],color='m')
plt.show()

plt.plot(data_open1['Date'],data_open1['AI_Revenue_USD_Mn'],color='m')
plt.show()
plt.plot(data_open2['Date'],data_open2['AI_Revenue_USD_Mn'],color='m')
plt.show()

sns.heatmap(df.corr(numeric_only=True))
plt.show() 


spend = df.groupby('Date')['R&D_Spending_USD_Mn'].sum()
print(spend)

plt.plot(spend.index,spend.values,color='r')
plt.show()

spend = df.groupby('Date')['AI_Revenue_USD_Mn'].sum()
print(spend)

plt.plot(spend.index,spend.values,color='r')
plt.show()

sns.pairplot(df)
plt.show()

r = df['Event'].value_counts()
print(r)