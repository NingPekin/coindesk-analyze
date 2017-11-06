
# coding: utf-8

# In[79]:

import json
import requests
import pandas as pd
get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt


# In[84]:

response = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?start=2017-09-01&end=2017-11-05')


# In[85]:

json_data = json.loads(response.text)


# In[86]:

print (json_data)


# In[95]:

bpi=json_data['bpi']


# In[93]:

data_line=pd.Series(bpi)


# In[94]:

plt.figure(figsize=(15,10))
data_line.plot.line();
plt.xlabel('Dates',fontsize=20, fontweight='bold')
plt.ylabel('Prices',fontsize=20, fontweight='bold')


# In[ ]:



