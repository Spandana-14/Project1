#!/usr/bin/env python
# coding: utf-8

# In[2]:


n=int(input("Enter the number of terms"))
a1=0
a2=1
count=0
if n<=0:
    print("Enter a positive number")
elif n==1:
    print("Fibonacci series upto", n ,":")
    print(a1)
else:
    print("Fibonacci series:")
    while count< n:
        print(a1)
        ath=a1+a2
        a1=a2
        a2=ath
        count+=1
    


# In[ ]:




