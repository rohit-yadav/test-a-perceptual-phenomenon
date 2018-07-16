
# coding: utf-8

# # Analyzing the Stroop Effect

# In[1]:


# Import Modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('stroopdata.csv')


# In[5]:


df.head()


# In[6]:


df.describe()


# **A) Central Tendency**
# 
# 1. Mean of congruent = 14.05 and Mean of incongruent = 22.02
# 2. Median of congruent = 14.35 and Median of incongruent = 21.01
# 3. Mode of congruent = 22.33 and Mode of incongruent = 35.26

# **B) Variability**
# 
# 1. Standard Deviation of congruent = 3.56 and that of incongruent is 4.80

# In[7]:


sns.set(color_codes=True)


# In[8]:


# Visualizations here
sns.distplot(df['Congruent'])
plt.show()


# In[9]:


sns.distplot(df['Incongruent'])
plt.show()


# In[10]:


plt.boxplot(df['Incongruent'])
plt.show()


# In[11]:


plt.boxplot(df['Congruent'])
plt.show()

