#!/usr/bin/env python
# coding: utf-8

# In[7]:


sample_list = [1, 2, 3, 4, 5, 6, 7] 
print("Original list: ",sample_list )
result = map(lambda x: x + x + x, sample_list) 
print("Triple of said list numbers:")
print(list(result))


# In[ ]:




