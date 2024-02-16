#!/usr/bin/env python
# coding: utf-8

# ## Python Task 2
Q1. You are writing code for a company. The requirement of the company is that you create a python
function that will check whether the password entered by the user is correct or not. The function should
take the password as input and return the string “Valid Password” if the entered password follows the
below-given password guidelines else it should return “Invalid Password”.
Note: 1. The Password should contain at least two uppercase letters and at least two lowercase letters.
2. The Password should contain at least a number and three special characters.
3. The length of the password should be 10 characters long.
# In[2]:


import re

def check_password(password):
    # Check length
    if len(password) != 10:
        return "Invalid Password"

    # Check uppercase letters
    if len(re.findall(r'[A-Z]', password)) < 2:
        return "Invalid Password"

    # Check lowercase letters
    if len(re.findall(r'[a-z]', password)) < 2:
        return "Invalid Password"

    # Check numbers
    if len(re.findall(r'\d', password)) < 1:
        return "Invalid Password"

    # Check special characters
    if len(re.findall(r'[!@#$%^&*(),.?":{}|<>~\[\]_\-=+]', password)) < 3:
        return "Invalid Password"

    # If all conditions pass, return "Valid Password"
    return "Valid Password"

# Test the function with different passwords
print(check_password("Abcd12345!"))  # Invalid Password
print(check_password("weakpass"))    # Invalid Password
print(check_password("Abcdefghij"))  # Invalid Password
print(check_password("Abcd123!@#")) 

Q2. Solve the below-given questions using at least one of the following:
1. Lambda functioJ
2. Filter functioJ
3. Zap functioJ
4. List ComprehensioI
B Check if the string starts with a particular letter
B Check if the string is numericY
B Sort a list of tuples having fruit names and their quantity. [("mango",99),("orange",80), ("grapes", 1000)-
B Find the squares of numbers from 1 to 10Y
B Find the cube root of numbers from 1 to 10Y
B Check if a given number is evenY
B Filter odd numbers from the given list.
[1,2,3,4,5,6,7,8,9,10-
B Sort a list of integers into positive and negative integers lists.
[1,2,3,4,5,6,-1,-2,-3,-4,-5,0]
# In[3]:


# Check if the string starts with a particular letter

string_list = ["apple", "banana", "cherry", "grape"]
starting_letter = "b"
result = list(filter(lambda x: x.startswith(starting_letter), string_list))
print(result)


# In[4]:


#  Check if the string is numericY

string_list = ["apple", "123", "3.14", "banana", "42"]
result = list(filter(lambda x: x.isnumeric(), string_list))
print(result)


# In[5]:


# Sort a list of tuples having fruit names and their quantity:

fruits = [("mango", 99), ("orange", 80), ("grapes", 1000)]
sorted_fruits = sorted(fruits, key=lambda x: x[1])
print(sorted_fruits)


# In[6]:


# Find the squares of numbers from 1 to 10:

squares = [x**2 for x in range(1, 11)]
print(squares)


# In[7]:


# Find the cube root of numbers from 1 to 10:

import math
cube_roots = [math.pow(x, 1/3) for x in range(1, 11)]
print(cube_roots)


# In[8]:


#Check if a given number is even:

number = 7
is_even = lambda x: x % 2 == 0
result = is_even(number)
print(result)


# In[9]:


#Filter odd numbers from the given list:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)


# In[10]:


#Sort a list of integers into positive and negative integers lists:

numbers = [1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, 0]
positive_numbers = [x for x in numbers if x > 0]
negative_numbers = [x for x in numbers if x < 0]
print(positive_numbers)
print(negative_numbers)


# In[ ]:




