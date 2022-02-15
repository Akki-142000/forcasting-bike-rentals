#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os


# In[9]:


type(os)


# In[10]:


pwd


# In[ ]:





# In[11]:


filePath="hour.csv"
bikesData=pd.read_csv(filePath)


# In[13]:


bikesData.head()


# In[15]:


bikesData.tail()


# In[16]:


bikesData.describe()


# In[17]:


bikesData.info()


# In[18]:


columnsToDrop = ['instant','casual','registered','atemp','dteday']

bikesData = bikesData.drop(columnsToDrop,1)


# In[19]:


bikesData.describe()


# In[20]:


bikesData.info()


# In[21]:


import numpy as np
np.random.seed(42)
from sklearn.model_selection import train_test_split  


# In[29]:


import pandas as pd
bikesData['dayCount'] = pd.Series(range(bikesData.shape[0]))/24
bikesData.head()


# In[ ]:


train_set, test_set = train_test_split(bikesData, test_size = 0.3, random_state=42)


# In[30]:


train_set.sort_values('dayCount')
test_set.sort_values('dayCount')


# In[31]:


def display_scores(scores):
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard deviation:", scores.std())


# In[32]:


display_scores(train_set)
display_scores(test_set)


# In[35]:


#ignore warnings
import warnings
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

columnsToScale = ['temp', 'hum', 'windspeed']
scaler = StandardScaler()
train_set[columnsToScale]= scaler.fit_transform(train_set[columnsToScale])


# In[36]:


float(train_set['temp'].mean())
display_scores(test_set[columnsToScale])


# In[25]:





# In[ ]:




