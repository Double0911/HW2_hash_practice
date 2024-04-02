#!/usr/bin/env python
# coding: utf-8

# In[16]:


import hashlib

hash_list = {}

# 讀取 .txt 檔案，如果txt檔處存位置不一樣，就要改下面的路徑
with open("D:\台北醫學大學\作業集中處\作業集中處(四下)\基礎資料結構與演算法\hw2_data.txt","r") as file:
    for word in file:
        word = word.strip()
        if word in hash_list:   # 檢查hash中是否存在該字
            hash_list[word] += 1
        else:
            hash_list[word] = 1

for keyword, count in hash_list.items():
    print(f"{keyword} : {count}")


# In[ ]:





# In[ ]:




