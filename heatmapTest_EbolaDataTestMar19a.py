#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[2]:


#import CSV file
data1 = pd.read_csv('ebolaData.csv', encoding='latin-1')
data1


# In[73]:


#select contact type 


# In[4]:


data2 = data1[data1.Gender=='Female']


# In[5]:


data2.head()


# In[6]:


data3 = data2[data2.DischType=="Died"]


# In[7]:


data3.head()


# In[ ]:




