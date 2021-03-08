#!/usr/bin/env python
# coding: utf-8

# In[3]:


#importando as bibliotecas necessárias
import pandas as pd


# In[4]:


import matplotlib as plt


# In[5]:


#importando o dataframe
df = pd.read_csv('lotofacil_Atual.csv')


# In[11]:


#visualisando as cinco primeiras linhas do arquivo
df.head(5)


# In[16]:


#analisando o dataframe...
df.describe()


# In[19]:


df.count()


# In[21]:


df.dtypes


# In[23]:


#criando um dataframe específico somente com as dezenas sorteadas
df = df['dezenas']


# In[24]:


#dataframe minerado
df

# In[27]:


#imprimindo o gráfico de todo dataframe
df.value_counts().plot.bar()


# In[46]:


df = df.head(100)


# In[74]:


import numpy as np


# In[75]:


print(df.value_counts(1).plot.bar())


# In[88]:


#def contagem_numeros(df, numero):
    #contator = 0
    #dfs = df.split(',')

    #for n in df:
        #if n == numero:
            #contator = contator + 1
        
    #return(contator)

#quantidade = contagem_numeros(df)


# In[ ]:




