
# coding: utf-8

# In[74]:

def ppj(bread, pb, j):
    message_5 = "Looks like I don't have lunch today."
    if bread == 0 or pb == 0 or j == 0:
        return message_5
    if bread < 0 or pb < 0 or j < 0:
        return "Error, cannot accept negative numbers. Please try again."
    if bread == 1 and pb >= 1 and j >= 1:
        print "I can make one open face sandwich."
    if bread > 1 and pb >= 1 and j >=1:
        bds = bread/2
        sandwich = min(bds, pb, j)
        extrabd = bread - sandwich
        extrapb = pb - sandwich
        extraj = j - sandwich
        openface = extrapb + extraj
        message_1 = "I can make a peanut butter and jelly sandwich!"
        message_2 = "I can make %i peanut butter and jelly sandwiches!" % (sandwich)
        message_3 = "I can make one peanut butter and jelly sandwich and one open face sandwich."
        message_4 = "I can make %i peanut butter and jelly sandwiches and 1 open face sandwich." % (sandwich)
        if sandwich == 0:
            return message_5
        elif sandwich == 1:
            if extrabd >= 1 and extrapb >= 1 and extraj >= 1:
                return message_3
            elif extrabd < 1 or extrapb < 1 or extraj < 1:
                return message_1
        elif sandwich > 1:
            if extrabd >= 1 and extrapb >= 1 and extraj >= 1:
                return message_4
            elif extrabd < 1 or extrapb < 1 or extraj < 1:
                return message_2


# In[66]:

print ppj(1,3,2)


