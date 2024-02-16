#!/usr/bin/env python
# coding: utf-8

# ## Python Assingment on Function
Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
range of 1 to 25.
# In[1]:


''' function that returns a list of odd numbers in the range of 1 to 25'''
def get_odd_number():
    odd_numbers = []
    for num in range(1,26):
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers


# In[2]:


get_odd_number()

Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs
to demonstrate their use.---> * args and **kwags are used in functions to allow them to acept an arbitrary number of arguments or keyword arguments respectively
     *args is used to pass a variable number of arguments to a function.it allows us to pass any number of positional arguments to a function.The arguments are passed as a tuple.
# In[3]:


'''an example of function that used *args to return a list of odd numbers within a given range'''
def odd_numbers(*args):
    start, end = args
    return [num for num in range(start,end+1) if num % 2 != 0]


# In[4]:


odd_numbers(1,30)

-----> **kwargs is used to pass a variable number of keyword arguments to a function. it allows us to pass any number of named arguments to a function.The arguments are passed as a        dictionary
# In[5]:


''' function that uses **kwargs to print the key value pairs of a dictionary'''
def print_dict(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")


# In[6]:


print_dict(name='Abdul', age=21, city='Jharkhand')

Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method
used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,
16, 18, 20].
---> An iterator is an object that can be iterated(looped) upon.it is used to represent a stream of data. An iterator object in python can be crated by implementing the --iter--() and --next--() methods in a class
# In[1]:


''' To print the first five elements of the given list[2,4,6,8,10,12,14,16,18,20] we can create an iterator object using the iter() function and then use the next() function to iterate over the first five elements'''
l = [2,4,6,8,10,12,14,16,18,20]

iterator_obj= iter(l)
for i in range(5):
    print(next(iterator_obj))

Q4. Write a python program using reduce function to compute the product of a list containing numbers
from 1 to 25.
# In[2]:


from functools import reduce
numbers= list(range(1,26))
multiply = lambda x,y:x*y
Product = reduce(multiply,numbers)
print("Product of numbers from 1 to 25:",Product)

Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the
filter function.
[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
# In[3]:


my_list = [2,3,6,9,27,60,90,120,55,46]
filtered_lst = list(filter(lambda x: (x % 2 == 0) and (x % 3 == 0),my_list))
print(filtered_lst)

Q6. Write a python program to find palindromes in the given list of strings using lambda and filter
function.
['python', 'php', 'aba', 'radar', 'level']
# In[9]:


strings = ['python', 'php', 'aba', 'radar', 'level']

palindromes = list(filter(lambda string: string == string[::-1], strings))

print(palindromes)


# In[ ]:




