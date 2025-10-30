# complete the code below of informative data analysis on the given dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("C:\\archive\\Spotify Youtube Dataset.csv")
print(data.head())
print(data.info())
data.drop(columns=['Url_spotify','Uri','Url_youtube'],inplace=True)
print(data.head())
print(data.isna().sum())

data['Comments'] = data['Comments'].fillna(0)
print(data.isna().sum())

Artist_group = data.groupby('Artist')['Views'].sum()
print(Artist_group)
Artist_sorted = Artist_group.sort_values(ascending=False)
print(Artist_sorted.head(10))

Artist_group1 = data.groupby('Track')['Stream'].sum()
print(Artist_group1)
Artist_sorted1 = Artist_group1.sort_values(ascending=False)
print(Artist_sorted1.head(10))

gp = data.groupby('Track')['Stream'].sum()
gpsort = gp.sort_values(ascending=True)
print(gpsort.head(5))

print(data['Album_type'].unique())

a_type = data['Album_type'].value_counts()
print(a_type)

plt.pie(a_type,labels=a_type.index,autopct='0x2c',startangle=60,shadow='True',explode=(0.05,0.05,0.05),pctdistance=0.75)
plt.show()

df = data.groupby('Album_type')[['Likes','Views','Comments']].mean()
print(df)

c_views = data.groupby('Channel')['Views'].sum().sort_values(ascending=False).head()
print(c_views)

T_danceability = data.groupby('Album')['Danceability'].sum().sort_values(ascending=False)
print(T_danceability.head(10))

df_vics = data[['Views','Likes','Comments','Stream']]
print(df_vics.corr())

sns.heatmap(df_vics.corr())
plt.show()

trackratio=data[['Track','Likes','Views']]
trackratio['LV_Rtios'] = data['Likes']/data['Views'] * 100
print(trackratio)
tv =trackratio.sort_values(by='LV_Rtios',ascending=False).head()
print(tv.head(7))