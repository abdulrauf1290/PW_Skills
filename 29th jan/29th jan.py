#!/usr/bin/env python
# coding: utf-8

# ## Python assingment 1
1. who developed python programmin Language?
-> Python was developed by Guido van Rossum.2. Which type of Programming does Pyton support?
-> Python is an interpreted programming language, upporting object-oriented, structured, and functional programming.3. is Python case senstive when dealing with identifers?
-> Yes, Python is a case-sensitive language, i.e.it treats uppercase and lowercase characters differently. This applies to identifiers too. You must avoid using the same name with different cases while naming identifiers.4. is python code complied or intrerrpreted?
->Python is an interpreted language.6. Name a few blocks of code used to define in python language?
-> The following are blocks: a module, a function body, and a class definition.7. State a charater used to give single-line comments in python?
-> We can write a single-line comment by adding a single '#' character before any statement or line of code8. Mention functios which can help us to find the version of python that we are currently workking on?
# In[1]:


import sys
print(sys.version)


# In[2]:


from platform import python_version
print("Current Python Version-", python_version())

9.Python supports the creation of anonymous functions at runtime, using a construct called _____________
->lambda10.What does pip stand for python
-> PIP is a package manager for Python package . It is used to manage(Install, Uninstall, Update, etc) additional packages that are not part of the Python standard library.11.Mention a few built-in functions in Python?
-> built-in functions given below
abs()	 : Returns the absolute value of a number
all()	 : Returns True if all items in an iterable object are true
any()	 : Returns True if any item in an iterable object is true
ascii()	 : Returns a readable version of an object. Replaces none-ascii characters with escape character
bin()	 : Returns the binary version of a number
bool()	  Returns the boolean value of the specified object
bytearray()	Returns an array of bytes
bytes()	Returns a bytes object
callable()	Returns True if the specified object is callable, otherwise False
chr()	Returns a character from the specified Unicode code.
classmethod()	Converts a method into a class method
compile()	Returns the specified source as an object, ready to be executed
complex()	Returns a complex number
delattr()	Deletes the specified attribute (property or method) from the specified object
dict()	Returns a dictionary (Array)12. What is the maximum possible length of an identifier in Python?
-> An identifier can have a maximum length of 79 characters in Python13. What are the benefits of using Python?
-> Python programming is powering the global job market because the benefits of Python are clear. Python is one of the top three programming languages in the world, and is poised to become the most popular, according to ZDNet.14. How is memory managed in Python?
Memory management in Python involves a private heap containing all Python objects and data structures. The management of this private heap is ensured internally by the Python memory manager.
15. How to install Python on Windows and set path variables?
-> To install Python on Windows:
Go to the official Python website (https://www.python.org/downloads/) and download the latest version of Python for Windows.
Run the Python installation file and follow the on-screen instructions. Make sure to select the option to add Python to your PATH environment variable.
To set the PATH environment variable:

Right-click on the Windows Start button and select "System" or search for "Environment Variables" in the Windows search bar.
Click on "Environment Variables."
Under "System Variables," scroll down and find the "Path" variable, then click on "Edit."
Click on "New" and add the path to the Python installation (e.g., "C:\Python38").
Click "OK" to close all windows and save the changes.
Now you can open a Command Prompt window and run Python from any location on your computer16. Is indentation required In python?
-> Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important. Python uses indentation to indicate a block of code.
# In[ ]:





# In[ ]:




