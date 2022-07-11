#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

csv_file_path = os.getenv('HOME')+'/aiffel/data_preprocess/data/vgsales.csv'
vgsales = pd.read_csv(csv_file_path) 
vgsales.tail()


# In[32]:


vgsales.drop(1, inplace = True)


# In[36]:


vgsales.head()


# In[35]:


vgsales.iloc[1]


# In[42]:


vgsales.loc[1]


# In[34]:


print('전체 데이터 건수: ', len(vgsales))


# In[16]:


print('컬럼별 결측치 개수')
len(vgsales) - vgsales.count()


# In[20]:


len(vgsales)


# In[29]:


type(vgsales)


# In[21]:


vgsales.count()


# In[22]:


vgsales.info()


# In[24]:


vgsales['Rank']


# In[27]:


vgsales['newRank'] = vgsales.Rank


# In[28]:


vgsales.newRank


# In[23]:


vgsales.describe(include='all')


# In[38]:


vgsales.isnull()


# In[40]:


vgsales.isnull().any(axis=1)


# In[41]:


[vgsales.isnull().any(axis=1)]

