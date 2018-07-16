
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

