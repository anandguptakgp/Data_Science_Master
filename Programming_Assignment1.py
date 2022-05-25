#!/usr/bin/env python
# coding: utf-8

# ### 1.	Write a Python program to print "Hello Python"?

# In[2]:


print("Hello Python")


# ### 2. Write a Python program to do arithmetical operations addition and division.?
# 
# 
# 
# 

# In[6]:


a = 8
b= 2
sum = a+b
division = a/b

print("The sum of a and b is", sum)
print("The value of a divided by b is", division)


# ### 3.	Write a Python program to find the area of a triangle?
# 

# In[9]:


height = int(input("Enter an height: "))
base = int(input("Enter an base: "))
Area = 0.5*height*base
print('Area of triangle is', Area )


# ### 4.	Write a Python program to swap two variables?
# 

# In[21]:


a = 3
b = 2
a, b = b, a
print('Value of a:',a)
print('Value of b:',b)


# ### 5.	Write a Python program to generate a random number?

# In[35]:


import random
lis = list(range(0,10,1))
print(random.choice(lis))


# In[ ]:





# In[ ]:




