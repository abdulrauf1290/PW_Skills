#!/usr/bin/env python
# coding: utf-8
Q1. Explain why we have to use the Exception class while creating a Custom Exception.
Note: Here Exception class refers to the base class for all the exceptions.
---> The Exception class is used as the base class for all exceptions because it provides a consistent and standardized way to handle and propagate errors in a program. By creating a custom exception that inherits from the Exception class, we can define and handle specific types of errors in a structured manner. Q2. Write a python program to print Python Exception Hierarchy.
# In[1]:


def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)



print_exception_hierarchy(Exception)

Q3. What errors are defined in the ArithmeticError class? Explain any two with an example.he ArithmeticError class in Python is the base class for arithmetic-related errors. It provides a common base for more specific arithmetic exceptions. Two notable exceptions derived from the ArithmeticError class are FloatingPointError and ZeroDivisionError.
# In[2]:


a = 1.0
b = 0.0
try:
    result = a / b
except ZeroDivisionError  as e:
    print("Error:", e)


# In[3]:


a = 10
b = 0
try:
    result = a / b
except ZeroDivisionError as e:
    print("Error:", e)

Q4. Why LookupError class is used? Explain with an example KeyError and IndexError.The LookupError class in Python is used as the base class for exceptions that involve lookup operations. It provides a common base for more specific lookup-related exceptions. 


KeyError:
This exception is raised when a dictionary key is not found in a dictionary or other mapping object.
# In[4]:


my_dict = {'key1': 'value1', 'key2': 'value2'}
try:
    value = my_dict['key3']
except KeyError as e:
    print("Error:", e)

IndexError:
This exception is raised when an index is out of range of a sequence, such as a list, tuple, or string.
# In[5]:


my_list = [1, 2, 3]
try:
    value = my_list[3]
except IndexError as e:
    print("Error:", e)

Q5. Explain ImportError. What is ModuleNotFoundError?ImportError is an exception class in Python that is raised when an import statement fails to import a module or a specific attribute from a module
# In[6]:


try:
    import non_existent_module
except ImportError as e:
    print("Error:", e)

ModuleNotFoundError, introduced in Python 3.6, is a subclass of ImportError. It is raised when an import statement fails to find the specified module or package. ModuleNotFoundError provides more specific information about the module or package that could not be found, including the full import name.
# In[7]:


try:
    from my_package import non_existent_module
except ModuleNotFoundError as e:
    print("Error:", e)

Q6. List down some best practices for exception handling in python.
## use always a specific exception 
##print always a proper message
## print always a proper message
## always avoid to write a multiple exception handling
## print alwas a proper message
## Document all the error 
## cleanup all the resources

# In[ ]:




