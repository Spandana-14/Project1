#!/usr/bin/env python
# coding: utf-8

# In[1]:


def frequent(s):
    a={}
    for i in s:
        if i in a:
            a[i] += 1
        else:
            a[i]=1
    a1=sorted(a,key=a.get,reverse=True)
    for i in a1:
        print(i,"=",a[i])

str=input("Enter a String=")
frequent(str)


# In[ ]:




