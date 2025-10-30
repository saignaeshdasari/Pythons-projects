# complete the code below of informative data analysis on the given dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\hp\\Downloads\\archive (1)\\netflix_titles.csv")
     
print(df.head())
print(df.info())
print(df['listed_in'].head())
print(df.duplicated().sum())
print(df.describe())

cols =["date_added","cast","description"]
df.drop(cols,axis=1,inplace=True)
print(df.columns)
print(df.head())

df['listed_in'] = df['listed_in'].astype('category')
print(df['listed_in'])
print(df['listed_in'].nunique())



df['listed_in'] = df['listed_in'].str.split(',')
df = df.explode('listed_in').reset_index(drop=True)
print(df.head())


# def categorize(df,col,labels):
#     edges = [df[col].describe()['min'],
# df[col].describe()['25%'],
# df[col].describe()['50%'],
# df[col].describe()['75%'],
# df[col].describe()['max']]
    
#     df[col] = pd.cut(df[col],edges,labels=labels,duplicates='drop')
#     return df
# labels = ['not_popular','below_AVG','popular']
# categorize(df,'rating',labels)
# print(df['rating'])
# print(df['rating'].value_counts())
# df.dropna(inplace=True)
# print(df.isna().sum())

# Data visualization

print(df['listed_in'].describe())
sns.catplot(y ='listed_in',data=df,kind='count',order=df['listed_in'].value_counts().index,color='#4287f5')

plt.title("Genre distribution")
plt.show()

sns.catplot(y ='rating',data=df,kind='count',order=df['rating'].value_counts().index,color='#4287f5')

plt.title("Genre distribution")
plt.show()

df['release_year'].hist()
plt.title("release date")
plt.show()