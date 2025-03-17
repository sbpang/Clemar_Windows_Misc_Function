#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from os import listdir
newfilename=[]
filepath = input("Enter File Path:")


# In[2]:


filename=listdir(filepath)
inputvalue = input("input date to be replaced")
replacevalue = input("input the new date")


# In[3]:


for i in filename:
    newfilename.append(i.replace(inputvalue, replacevalue))


# In[4]:


for item in range(len(filename)):
    os.rename(filepath+"\\"+filename[item],filepath+"\\"+newfilename[item])


# In[5]:





# In[ ]:




