#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import os
os.chdir('C:/Users/malay/Desktop/Dataset')


# In[56]:


df=pd.read_csv('survey_results_public.csv')
df.shape


# In[5]:


df_schema=pd.read_csv('survey_results_schema.csv')
df_schema.head()


# In[6]:


pd.set_option('display.max_columns', None)


# In[7]:


df1=df[df['DevType']=='Data scientist or machine learning specialist']
df2=df[df['DevType']=='Data or business analyst']
frames=[df1,df2]
df_ds=pd.concat(frames)


# In[8]:


df_ds.head()


# # Popular Language among Data Specialists

# In[9]:


df_python=df_ds[df_ds['LanguageHaveWorkedWith'].str.contains("Python", case=False, na=False)]
df_python
len(df_python)
print("Hence {} % of the total data specialists in the survey have used Python(among other languages as well) on their Job".format(len(df_python)*100/(df_ds.shape[0]-sum(df_ds['LanguageHaveWorkedWith'].isnull()))))


# In[10]:


sum(df_ds['LanguageHaveWorkedWith'].isnull())


# In[11]:


df_R=df_ds[df_ds['LanguageHaveWorkedWith'].str.contains("R;", case=True, na=False)]
df_R_only= df_ds[df_ds['LanguageHaveWorkedWith']=='R']
frames_2=[df_R, df_R_only]
df_R_concat= pd.concat(frames_2)
print("Hence {} % of the total data specialists in the survey have used R(among other languages as well) on their Job".format(len(df_R_concat)*100/(len(df_ds)-sum(df_ds['LanguageHaveWorkedWith'].isnull()))))


# Percentage of people who have used both Python and R as part of their work

# In[12]:


df_python_R=df_ds[df_ds['LanguageHaveWorkedWith'].str.contains("Python", case=False, na=False) & df_ds['LanguageHaveWorkedWith'].str.contains(";R;", case=False, na=False)]
df_python_R
print("Hence {} % of the total data specialists in the survey who have used both Python and R on their Job".format(len(df_python_R)*100/len(df_ds)))


# Calculating the percentage of people who have worked on Python( among other languages as well) but have not worked on R

# In[13]:


(len(df_python)-(len(df_python_R)))*100/len(df_ds)


# Calculating the percentage of people who have worked on R( among other languages as well) but have not worked on Python

# In[14]:


(len(df_R)-(len(df_python_R)))*100/len(df_ds)


# In[15]:


df_Julia=df_ds[df_ds['LanguageHaveWorkedWith'].str.contains("Julia", case=False, na=False)]
len(df_Julia)
print("Hence {} % of the total data specialists in the survey have used Julia(among other languages as well) on their Job".format(len(df_Julia)*100/(df_ds.shape[0]-sum(df_ds['LanguageHaveWorkedWith'].isnull()))))


# In[16]:


df_Rust=df_ds[df_ds['LanguageHaveWorkedWith'].str.contains("Rust", case=False, na=False)]
len(df_Rust)
print("Hence {} % of the total data specialists in the survey have used Rust(among other languages as well) on their Job".format(len(df_Rust)*100/(df_ds.shape[0]-sum(df_ds['LanguageHaveWorkedWith'].isnull()))))


# In[17]:


df_Elixir=df_ds[df_ds['LanguageHaveWorkedWith'].str.contains("Elixir", case=False, na=False)]
len(df_Julia)
print("Hence {} % of the total data specialists in the survey have used Elixir(among other languages as well) on their Job".format(len(df_Elixir)*100/(df_ds.shape[0]-sum(df_ds['LanguageHaveWorkedWith'].isnull()))))


# In[18]:


df_Go=df_ds[df_ds['LanguageHaveWorkedWith'].str.contains("Go", case=False, na=False)]
len(df_Go)
print("Hence {} % of the total data specialists in the survey have used Go(among other languages as well) on their Job".format(len(df_Go)*100/(df_ds.shape[0]-sum(df_ds['LanguageHaveWorkedWith'].isnull()))))


# In[66]:


df_SQL=df_ds[df_ds['LanguageHaveWorkedWith'].str.contains("SQL", case=True, na=False)]
print("Hence {} % of the total data specialists in the survey have used SQL(among other languages as well) on their Job".format(len(df_SQL)*100/(len(df_ds)-sum(df_ds['LanguageHaveWorkedWith'].isnull()))))


# In[67]:


df_prog= pd.DataFrame({'Programming Language' : ['Python', 'R', 'Julia', 'Rust', 'Julia', 'Go', 'SQL'], 'Proportion of People using': [0.85,0.24,0.05,0.03,0.0027,0.03, 0.603]})
df_prog_sort=df_prog.sort_values('Proportion of People using')


# In[68]:


import seaborn as sns
sns.barplot(x='Programming Language', y='Proportion of People using', data= df_prog_sort)
plt.show()


# Hence, Python is predominantly used among Data specialists as per the data. Whereas, there is a very low percentage of data specialists who have used R on their Job but have not worked on Python yet.

# # Popular Database to work with for Data Specialists

# In[30]:


df_mysql=df_ds[df_ds['DatabaseHaveWorkedWith'].str.contains("MySql", case=False, na=False)]
print("Hence {} % of the total data specialists in the survey using MySql(among other databases as well) on their Job".format(len(df_mysql)*100/len(df_ds)))


# In[31]:


df_PostgreSQL=df_ds[df_ds['DatabaseHaveWorkedWith'].str.contains("PostgreSQL", case=False, na=False)]
print("Hence {} % of the total data specialists in the survey using PostgreSQL(among other databases as well) on their Job".format(len(df_PostgreSQL)*100/len(df_ds)))


# In[32]:


df_DynamoDB=df_ds[df_ds['DatabaseHaveWorkedWith'].str.contains("DynamoDB", case=False, na=False)]
print("Hence {} % of the total data specialists in the survey using DynamoDB(among other databases as well) on their Job".format(len(df_DynamoDB)*100/len(df_ds)))


# In[33]:


df_Elasticsearch=df_ds[df_ds['DatabaseHaveWorkedWith'].str.contains("Elasticsearch", case=False, na=False)]
print("Hence {} % of the total data specialists in the survey using Elasticsearch(among other databases as well) on their Job".format(len(df_Elasticsearch)*100/len(df_ds)))


# In[34]:


df_SQLite=df_ds[df_ds['DatabaseHaveWorkedWith'].str.contains("SQLite", case=False, na=False)]
print("Hence {} % of the total data specialists in the survey using SQLite(among other databases as well) on their Job".format(len(df_SQLite)*100/len(df_ds)))


# In[35]:


df_Redis=df_ds[df_ds['DatabaseHaveWorkedWith'].str.contains("Redis", case=False, na=False)]
print("Hence {} % of the total data specialists in the survey using Redis(among other databases as well) on their Job".format(len(df_Redis)*100/len(df_ds)))


# In[36]:


df_Microsoft_SQL=df_ds[df_ds['DatabaseHaveWorkedWith'].str.contains("Microsoft SQL Server", case=False, na=False)]
print("Hence {} % of the total data specialists in the survey using Microsoft SQL Server(among other databases as well) on their Job".format(len(df_Microsoft_SQL)*100/len(df_ds)))


# In[37]:


df_Oracle=df_ds[df_ds['DatabaseHaveWorkedWith'].str.contains("Oracle", case=False, na=False)]
print("Hence {} % of the total data specialists in the survey using Oracle(among other databases as well) on their Job".format(len(df_Oracle)*100/len(df_ds)))


# In[38]:


df_MongoDB=df_ds[df_ds['DatabaseHaveWorkedWith'].str.contains("MongoDB", case=False, na=False)]
print("Hence {} % of the total data specialists in the survey using MongoDB(among other databases as well) on their Job".format(len(df_MongoDB)*100/len(df_ds)))


# In[39]:


df_Cassandra=df_ds[df_ds['DatabaseHaveWorkedWith'].str.contains("Cassandra", case=False, na=False)]
print("Hence {} % of the total data specialists in the survey using Cassandra(among other databases as well) on their Job".format(len(df_Cassandra)*100/len(df_ds)))


# In[40]:


df_db= pd.DataFrame({'Database' : ['MySQL', 'PostgreSQL', 'DynamoDB', 'Elastic Search', 'SQLite', 'Redis', 'Microsoft Sql Server','Oracle', 'MongoDB', 'Cassandra'], 'Proportion of People using': [0.29,0.36,0.03,0.07,0.22,0.08,0.25,0.09,0.13,0.014]})
df_db_sort=df_db.sort_values('Proportion of People using')
df_db_sort


# In[41]:


sns.barplot(x='Proportion of People using', y='Database', data= df_db_sort, orient='h')
plt.show()


# # Which Operating System is popular among the data professionals?

# In[61]:


df_macos=df_ds[df_ds['OpSysProfessional use'].str.contains("macOS", case=False, na=False)]
print("Hence {} % of the total data specialists in the survey who have used macOS(among other OS as well) on their Job".format(len(df_macos)*100/(df_ds.shape[0]-sum(df_ds['OpSysProfessional use'].isnull()))))


# In[62]:


df_Windows=df_ds[df_ds['OpSysProfessional use'].str.contains("Windows", case=False, na=False)]
print("Hence {} % of the total data specialists in the survey who have used Windows(among other OS as well) on their Job".format(len(df_Windows)*100/(df_ds.shape[0]-sum(df_ds['OpSysProfessional use'].isnull()))))


# In[63]:


df_linux=df_ds[df_ds['OpSysProfessional use'].str.contains("Linux-based", case=False, na=False)]
print("Hence {} % of the total data specialists in the survey who have used Linux(among other OS as well) on their Job".format(len(df_linux)*100/(df_ds.shape[0]-sum(df_ds['OpSysProfessional use'].isnull()))))


# In[64]:


df_wsl=df_ds[df_ds['OpSysProfessional use'].str.contains("WSL", case=False, na=False)]
print("Hence {} % of the total data specialists in the survey who have used WSL(among other OS as well) on their Job".format(len(df_wsl)*100/(df_ds.shape[0]-sum(df_ds['OpSysProfessional use'].isnull()))))


# In[65]:


df_bsd=df_ds[df_ds['OpSysProfessional use'].str.contains("BSD", case=False, na=False)]
print("Hence {} % of the total data specialists in the survey who have used BSD(among other OS as well) on their Job".format(len(df_bsd)*100/(df_ds.shape[0]-sum(df_ds['OpSysProfessional use'].isnull()))))

