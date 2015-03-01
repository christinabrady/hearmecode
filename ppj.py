
# coding: utf-8

# In[4]:

def ppj(bread, pb, j):
    if bread >= 2 and pb >= 1 and j >= 1:
    	sandwich = min(bread/2, pb, j)
        return "I can make %i peanut butter and jelly sandwiches!" % (sandwich)
    else:
        return "Looks like I don't have lunch today."


# In[ ]:

print ppj(44,28,16)

