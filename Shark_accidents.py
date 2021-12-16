#!/usr/bin/env python
# coding: utf-8

# In[68]:


#import packages

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[69]:


#import database

df= pd.read_csv(r"C:\Users\shruthirajesh\OneDrive - Georgian College\attacks.csv",encoding = "ISO-8859-1")
df.head() 


# In[70]:


df.columns


# In[71]:


df = df.drop(['Unnamed: 22', 'Unnamed: 23', 'Area', 'Case Number', 'Investigator or Source', 'Name', 'Location','Age', 'Injury', 'pdf', 'href formula', 'href','Time', 'Case Number.1', 'Case Number.2', 'original order','Date','Species '], axis = 1,errors='ignore')


# In[72]:


df


# In[73]:


#Treating missing and null values:

df.isna().sum()


# In[15]:


#There are over 19400 missing values present in each variable


# In[74]:


len(df) 


# In[75]:


df.dropna(subset=['Year','Type','Country','Activity','Sex ','Fatal (Y/N)'], inplace = True)


# In[76]:


df.isna().sum()


# In[77]:


df


# # Exploratory data analysis

# # 1) What are the countries with most shark attacks?

# In[80]:


print(df['Country'].value_counts())


# In[23]:


#Adding others column to group small values


# In[81]:


def group(column, threshold):
    table = df[column].value_counts()
    grouped_columns = [i for i in table.index if table[i] < threshold]
    for n in grouped_columns:
        df.loc[df[column] == n, column] = 'Other'
    print(df[column].value_counts())


# In[82]:


group('Country', 50)


# In[25]:


#Fuction to plot Horizontal Bar chart


# In[108]:


fig = plt.figure()
ax = fig.add_axes([2,2,2,2])
Country= ['USA','Other','AUSTRALIA','SOUTH AFRICA', 'PAPUA NEW GUINEA','BAHAMAS','NEW ZEALAND','BRAZIL','MEXICO','REUNION']
count = [1871,1078,1030,454,102,97,97,84,68,51]
ax.barh(Country,count)
ax.set_xlabel('Country')
ax.set_ylabel('Count')
plt.show()


# # 2) What are the most activities prior to attack?

# In[84]:


print(df['Activity'].value_counts())


# In[ ]:


#Grouping some categories


# In[85]:


df.loc[df['Activity'].str.contains('surf', case=False, na=False), 'Activity'] = 'Surfing'
df.loc[df['Activity'].str.contains('boarding', case=False, na=False), 'Activity'] = 'Surfing'
df.loc[df['Activity'].str.contains('swim', case=False, na=False), 'Activity'] = 'Swimming'
df.loc[df['Activity'].str.contains('fishing', case=False, na=False), 'Activity'] = 'Fishing'
df.loc[df['Activity'].str.contains('aquarium', case=False, na=False), 'Activity'] = 'Fishing'
df.loc[df['Activity'].str.contains('hunt', case=False, na=False), 'Activity'] = 'Fishing'
df.loc[df['Activity'].str.contains('trap', case=False, na=False), 'Activity'] = 'Fishing'
df.loc[df['Activity'].str.contains('walk', case=False, na=False), 'Activity'] = 'Swimming'
df.loc[df['Activity'].str.contains('wading', case=False, na=False), 'Activity'] = 'Swimming'
df.loc[df['Activity'].str.contains('float', case=False, na=False), 'Activity'] = 'Swimming'
df.loc[df['Activity'].str.contains('Treading water', case=False, na=False), 'Activity'] = 'Swimming'
df.loc[df['Activity'].str.contains('pull', case=False, na=False), 'Activity'] = 'Fishing'
df.loc[df['Activity'].str.contains('pick', case=False, na=False), 'Activity'] = 'Fishing'
df.loc[df['Activity'].str.contains('bath', case=False, na=False), 'Activity'] = 'Swimming'
df.loc[df['Activity'].str.contains('diving', case=False, na=False), 'Activity'] = 'Diving'
df.loc[df['Activity'].str.contains('snorkel', case=False, na=False), 'Activity'] = 'Diving'
df.loc[df['Activity'].str.contains('photo', case=False, na=False), 'Activity'] = 'Photo shoot'
df.loc[df['Activity'].str.contains('film', case=False, na=False), 'Activity'] = 'Filming'
df.loc[df['Activity'].str.contains('float', case=False, na=False), 'Activity'] = 'Floating'
df.loc[df['Activity'].str.contains('boarding', case=False, na=False), 'Activity'] = 'Boarding'
df.loc[df['Activity'].str.contains('wash', case=False, na=False), 'Activity'] = 'Washing'


# In[86]:


print(df['Activity'].value_counts())


# In[87]:


group('Activity', 10)


# In[107]:


fig = plt.figure()
ax = fig.add_axes([2,2,2,2])
activity= ['Swimming','Surfing','Fishing','Other', 'Diving','Standing','Kayaking','Fell overboard','Washing','Canoeing']
count = [1387,1328,926,594,511,98,30,28,20,10]
ax.bar(activity,count,color='teal')
ax.set_xlabel('Activity')
ax.set_ylabel('Count')
plt.show()


# # 3) What is the fatal and non-fatal rate?

# In[94]:


print(df['Fatal (Y/N)'].value_counts())


# In[95]:


df.drop(df[df['Fatal (Y/N)'] == 'UNKNOWN'].index, inplace=True)
df.drop(df[df['Fatal (Y/N)'] == 'M'].index, inplace=True)
df.drop(df[df['Fatal (Y/N)'] == '2017'].index, inplace=True)
df.drop(df[df['Fatal (Y/N)'] == ' N'].index, inplace=True)
df.drop(df[df['Fatal (Y/N)'] == 'y'].index, inplace=True)


# In[96]:


print(df['Fatal (Y/N)'].value_counts())


# In[110]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
Fatal =['N','Y']
students = [3728,1172]
ax.pie(students, labels = Fatal,autopct='%1.2f%%')
plt.show()


# # 4) What is the tendency of shark attacks from the year 1960 to 2010?

# In[111]:


df = df.loc[df['Year'] >= 1960,:]
df = df.loc[df['Year'] <= 2010,:]


# In[121]:


table = df.groupby('Year').count()


# In[127]:


plt.figure(figsize = (20,10))
sns.lineplot(data=table, x="Year", y = table['Type'])
plt.show()

