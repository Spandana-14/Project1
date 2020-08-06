#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math 
def area_of_circle(r): 
    a = r**2 * math.pi
    return a

r = float(input("Enter the radius of the circle: "))
print("The area of the circle with radius " +str(r)+ " is: " +str(area_of_circle(r)) )


# In[ ]:




