#!/usr/bin/env python
# coding: utf-8

# In[1]:


firstName = str(input("Enter your first name:"))
lastName = str(input("Enter your last name:"))
age = int(input("Enter your age:"))
date_of_birth = int(input("Enter your birth year:"))
userinfo = []
userinfo.append(firstName)
userinfo.append(lastName)
userinfo.append(age)
userinfo.append(date_of_birth)

for i in range(len(userinfo)):
    print(userinfo[i])
if(age > 18):
    print("You can go out to the street.")
else:
    print("You can't go out because it's too dangerous.")


# In[ ]:




