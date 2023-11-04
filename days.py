#!/usr/bin/env python
# coding: utf-8

# In[6]:


def days(data):
    count_days = {}
    for days in data:
        dia=days["Day_of_week"]
        if dia in count_days:
            count_days[dia] +=1
        else:
            count_days[dia] = 1
    labels = count_days.keys()
    values = count_days.values()
    return labels, values





