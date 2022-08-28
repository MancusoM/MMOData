#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Intro, importing packages


# In[2]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

Importing Data
# In[3]:


total = pd.read_csv('Innings.csv')
total.head()


# In[4]:


inning = pd.read_csv('Book3.csv')
inning.describe()


# In[5]:


#Changing the columns from R to Runs, makes it easier later 
total.rename(columns = {'R':'Runs'}, inplace = True)


# In[6]:


#Making My Mets-only  Datasets 
MetsByInning = total[total['Team'] =='NYM']
Metsdata = inning[inning['Team'] == 'NYM']


# In[7]:


Metsdata


# In[8]:


#Minor Data Cleaning
inning.info()
inning.columns


# In[9]:


inning = inning.drop(['IBB','3B','PA','CS','SO','HBP','ROE','SH','GDP','SF','RBI','3B'], axis =1)
print(inning.columns)


# Data Viz 

# In[10]:


#Graph of which innings the Mets score in 
plt.figure(figsize = (10,8))
By_inning = sns.barplot(x='Inning', y='Runs', data = Metsdata)
plt.title("Mets Runs By Inning",fontsize = 20)
sns.set_style("darkgrid")
plt.savefig('RunsByInning.png')


# In[11]:


#Creating Dataset for the first inning 
First= inning[inning['Inning'] == 1]
First.head()


# In[37]:


#Graph of the amount of times teams score in the first inning, Mets are in orange
plt.figure(figsize = (21,12))
sns.set_style('darkgrid')
test = {Team: "#ffdab9" if Team == "NYM" else "#87CEFA" for Team in First.Team.unique()} #using this to make a custom color palette 

sns.barplot(x='Team', y='Runs', palette = test, data = First,)
plt.title('Runs in The First Inning',loc='right', fontsize = 30,x= .99,y=.92).set_style('italic')
plt.savefig('FirstInningRuns.png')


# In[13]:


#Creating a new dataset that only has the "Innings 1-3" split
FirstGroup= total[total['Split'] == 'Innings 1-3']
FirstGroup.head()


# In[38]:


#Graph of the amount of times teams score in the first/second/third innings combined, Mets are in orange
plt.figure(figsize = (18,10))
sns.set_style('darkgrid')

test = {Team: "#ffdab9" if Team == "NYM" else "#87CEFA" for Team in FirstGroup.Team.unique()}
Group = sns.barplot(x='Team', y='Runs', data = FirstGroup, palette =test)
plt.title('Runs From 1st to 3rd Inning',loc = 'right',x= .995,y=.93, fontsize = 30)
plt.savefig('GroupingRuns.png')

