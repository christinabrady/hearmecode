
# coding: utf-8

# In[74]:

def ppj(bread, pb, j):
    message_1 = "Looks like I don't have lunch today."
    if bread <= 1 or pb == 0:
        return message_1
    elif bread < 0 or pb < 0 or j < 0:
        return "Error, cannot accept negative numbers. Please try again."
    elif bread == 1 and pb >= 1 and j >= 1:
        return "I can make one open face sandwich."
    elif bread >= 2 and pb >= 1 and j < 1:
        pbsandwich = min(bread/2, pb)
        return "I can make %i peanut butter sandwiches" % (pbsandwich)
    elif bread >= 2 and pb >= 1 and j >=1:
        #step 1 calculate the number of ppj
        #step 2 calculate the number of open face
        #step 3 calculate the number of peanut butter snd
        bds = bread/2
        sandwich = min(bds, pb, j)
        extrabd = bread - sandwich*2
        extrapb = pb - sandwich
        extraj = j - sandwich
        pbsandwich = min(extrabd/2, extrapb)
        if sandwich == 1:
            if extrabd >=2 and extrapb >= 1 and extraj < 1:
                pbsandwich = min(extrabd/2, extrapb)
                return "I can make 1 pp&j and %i peanut butter sandwiches." % (pbsandwich)
            elif extrabd >= 1 and extrapb >= 1 and extraj >= 1:
                return "I can make 1 pp&j and 1 open face sandwich."
            elif extrabd <= 1 or extrapb < 1:
                return "I can make 1 pp&j."
        elif sandwich > 1:
            if extrabd >=2 and extrapb >= 1 and extraj < 1:
                pbsandwich = min(extrabd/2, extrapb)
                return "I can make %i pp&j and %i peanut butter sandwiches." % (sandwich, pbsandwich)
            elif extrabd >= 1 and extrapb >= 1 and extraj >= 1:
                return "I can make %i pp&j and 1 open face sandwich." %(sandwich)
            elif extrabd <= 1 or extrapb < 1:
                return "I can make %i pp&j." % (sandwich)


# In[66]:

print ppj(7,5,4)


 