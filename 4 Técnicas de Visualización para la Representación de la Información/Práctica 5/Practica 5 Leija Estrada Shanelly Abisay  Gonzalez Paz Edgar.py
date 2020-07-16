#!/usr/bin/env python
# coding: utf-8

# # Práctica No. 05 Visualización de Datos Numéricos con Matplotlib

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


Pzafalsas = pd.read_csv('PiezasBilletesFalsosMX.csv', sep=",", index_col= 0)


# In[3]:


Pzafalsas.head()


# In[6]:


anio = [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
pza20 = list(Pzafalsas['20'])
pza50 = list(Pzafalsas['50'])
pza100 = list(Pzafalsas['100'])
pza200 = list(Pzafalsas['200'])
pza500 = list(Pzafalsas['500'])
pza1000 = list(Pzafalsas['1000'])
Etiquetas = ['20 MXN', '50 MXN', '100 MXN', '200 MXN', '500 MXN', '1000 MXN']
mipaleta = [ '#FF0000', '#0F3C4A', '#089495', '#F7F1DA', '#F6954D', '#FC5928']


# In[7]:


from matplotlib.pyplot import figure
figure(figsize=(12,6))
plt.stackplot(anio, pza20, pza50, pza100, pza200, pza500, pza1000, labels= Etiquetas, colors= mipaleta, alpha=.7)
plt.legend()
plt.title('Piezas falsas captadas al año por denominación (billete nacional)')
plt.xlabel('Años')
plt.ylabel('Piezas')
plt.show()


# In[ ]:




