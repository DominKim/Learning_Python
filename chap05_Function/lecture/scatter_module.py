#!/usr/bin/env python
# coding: utf-8

# In[1]:


from statistics import mean # 통계함수
from math import sqrt       # 수학함수

# 평균 함수
def Avg(dataset):
    return mean(dataset)

# 분산과 표준편차 함수
def var_std(dataset):
    avg = Avg(dataset)  # 산술평균
    
    # list + for
    diff = [(x-avg) ** 2 for x in dataset] # (x변량 -  평균) ** 2
    diff_sum = sum(diff)
    
    var = diff_sum / (len(dataset) - 1) # 분산
    std = sqrt(var) # 표준편차
    return var, std
# .py 파일 만들때 사용
get_ipython().system('jupyter nbconvert --to python scatter_module.ipynb')


# In[ ]:




