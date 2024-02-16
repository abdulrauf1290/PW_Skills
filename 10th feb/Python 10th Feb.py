#!/usr/bin/env python
# coding: utf-8
Q1. Which function is used to open a file? What are the different modes of opening a file? Explain each mode
of file opening. 
--->  In most programming languages, the function used to open a file is typically called open().When opening a file, you can specify different modes based on how you intend to use the file. The modes determine whether you want to read, write, or append to the file, and also whether you want to create a new file if it doesn't exist. The common modes for file opening are:

Read mode ('r'): This mode allows you to read the contents of an existing file. If the file doesn't exist, an error is raised.

Write mode ('w'): This mode is used to create a new file for writing. If a file with the same name already exists, its contents will be truncated (deleted) before writing to it. If the file doesn't exist, a new file will be created.

Append mode ('a'): This mode is used to open a file for appending data at the end. If the file doesn't exist, a new file will be created. Existing content is preserved, and new data is added to the end of the file.

Read and Write mode ('r+'): This mode allows you to read and write to an existing file. The file pointer is initially at the beginning of the file.

Write and Read mode ('w+'): This mode is similar to 'r+', but it also creates a new file for writing if it doesn't exist.

Append and Read mode ('a+'): This mode is similar to 'r+', but it also creates a new file for appending if it doesn't exist.Q2. Why close() function is used? Why is it important to close a file?---> The close() function is used to close an opened file in programming languages that require explicit file handling, such as Python.

It is important to close a file after you have finished using it for several reasons:

Resource management: When you open a file, the operating system allocates certain resources to handle the file operations, such as memory buffers and file descriptors. If you don't close the file, these resources may not be released immediately, leading to resource leaks. Closing the file ensures that these resources are properly released, preventing potential issues like running out of system resources.

Data integrity: Closing a file ensures that all the data you have written to or read from the file is flushed or saved to the underlying storage. If you don't close the file and terminate the program abruptly, some data may remain buffered in memory and not be permanently written to the file. Closing the file guarantees that the data is properly written and the file is in a consistent state.

Access by other processes: By closing the file, you release any locks or restrictions that your program may have placed on the file. This allows other processes or programs to access the file without conflicts. Failing to close a file might result in other processes being unable to open or modify the file until it is closed.Q3. Write a python program to create a text file. Write ‘I want to become a Data Scientist’ in that file. Then
close the file. Open this file and read the content of the file.
# In[1]:


file_name = 'data_scientist.txt'
content = 'I want to become a Data Scientist'


file = open(file_name, 'w')


file.write(content)


file.close()


file = open(file_name, 'r')
file_content = file.read()

# Print the content
print(file_content)


file.close()

Q4. Explain the following with python code: read(), readline() and readlines().---> In Python, read(), readline(), and readlines() are methods that can be used to read data from a file.
read(): The read() method is used to read the entire contents of a file as a single string. It reads from the current position of the file pointer until the end of the file. Here's an example:
# In[2]:


with open('data_scientist.txt', 'r') as file:
    content = file.read()

print(content)

readline(): The readline() method is used to read a single line from a file. It reads from the current position of the file pointer until it encounters a newline character (\n) or reaches the end of the file.
# In[3]:


# Open the file in read mode
file = open('data_scientist.txt', 'r')

# Read the first line of the file
line = file.readline()

# Print the line
print(line)

# Close the file
file.close()

readlines(): The readlines() method is used to read all the lines of a file and return them as a list of strings. Each line is treated as a separate element in the list. Here's an example:
# In[4]:


# Open the file in read mode
file = open('data_scientist.txt', 'r')

# Read all the lines of the file
lines = file.readlines()

# Print each line
for line in lines:
    print(line)

# Close the file
file.close()

Q5. Explain why with statement is used with open(). What is the advantage of using with statement and
open() together? ---> The with statement in Python is used in conjunction with the open() function to ensure proper handling of resources, such as files, and to provide automatic cleanup or closing of the resources. The advantage of using the with statement with open() is as follows:

Automatic cleanup: When a file is opened using open() within a with statement, the file is automatically closed at the end of the block, regardless of whether an exception occurs or not. This ensures that the file is properly closed, even in the event of an error or an exception being raised during file handling
Simplified code: Using the with statement makes the code more concise and readable.
Exception handling: The with statement also provides a convenient way to handle exceptions. If an exception occurs within the with block, the file will still be closed automatically, preventing any potential issues caused by leaving the file openQ6. Explain the write() and writelines() functions. Give a suitable example.---> write(): The write() function is used to write a string of data to a file. It appends the specified string to the end of the file, or overwrites the existing content if the file already exists
# In[6]:


file = open('data_scientist.txt', 'w')

file.write('Hello, World!\n')
file.write('This is a sample file.')

# Close the file
file.close()

writelines(): The writelines() function is used to write a list of strings to a file. Each string in the list corresponds to a separate line in the file.
# In[7]:


# Open the file in write mode
file = open('example.txt', 'w')

# Prepare a list of strings
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']

# Write the lines to the file
file.writelines(lines)

# Close the file
file.close()


# In[ ]:




