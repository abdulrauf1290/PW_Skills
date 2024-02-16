#!/usr/bin/env python
# coding: utf-8

# ## Python Task 1
Q1. Create a function which will take a list as an argument and return the product of all the numbers
after creating a flat list.
Use the below-given list as an argument for your function.
list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,
22, 61, 34)}, [56, 'data science'], 'Machine Learning'] 
# In[1]:


def calculate_product(lst):
    flat_list = []
    
    # Function to flatten the nested lists and extract numeric keys and values from dictionaries
    def flatten_list(input_list):
        for item in input_list:
            if isinstance(item, list):
                flatten_list(item)
            elif isinstance(item, dict):
                for key, value in item.items():
                    if isinstance(key, (int, float)):
                        flat_list.append(key)
                    if isinstance(value, (int, float)):
                        flat_list.append(value)
            else:
                flat_list.append(item)
    
    flatten_list(lst)
    
    product = 1
    for num in flat_list:
        if isinstance(num, (int, float)):
            product *= num
    
    return product


# In[2]:


list1 = [1, 2, 3, 4, [44, 55, 66, True], False, (34, 56, 78, 89, 34), {1, 2, 3, 3, 2, 1}, {1: 34, "key2": [55, 67, 78, 89], 4: (45, 22, 61, 34)}, [56, 'data science'], 'Machine Learning']

result = calculate_product(list1)
print(result)

Q2. Write a python program for encrypting a message sent to you by your friend. The logic of encryption
should be such that, for a the output should be z. For b, the output should be y. For c, the output should
be x respectively. Also, the whitespace should be replaced with a dollar sign. Keep the punctuation
marks unchanged.
Input Sentence: I want to become a Data Scientist. 
# In[3]:


def encrypt_message(message):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            encrypted_char = chr(ord('a') + (ord('z') - ord(char)))
        elif char.isspace():
            encrypted_char = '$'
        else:
            encrypted_char = char
        
        encrypted_message += encrypted_char
    
    return encrypted_message

input_sentence = "I want to become a Data Scientist."
lowercase_sentence = input_sentence.lower()
encrypted_sentence = encrypt_message(lowercase_sentence)
print(encrypted_sentence)


# In[ ]:





# In[ ]:




