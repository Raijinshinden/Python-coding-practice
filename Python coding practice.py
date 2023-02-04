#!/usr/bin/env python
# coding: utf-8

# The purpose of this code is to check if a certain value exists in the dictionary as a key.

# In[2]:


content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
is_in_dictionary_1 = '9+' in content_ratings
is_in_dictionary_2 = 987 in content_ratings

if '17+' in content_ratings:
    result = "It exists"
    print(result)


# As you can see, the value '17+' does exist in the dictionary, so the string "It exists" was printed.
