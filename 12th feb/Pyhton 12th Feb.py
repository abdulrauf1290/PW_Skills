#!/usr/bin/env python
# coding: utf-8
Q1. What is an Exception in python? Write the difference between Exceptions and Syntax errors.
---> 
    An exception is an event that occurs during the execution of a program, disrupting the normal flow of the program's instructions. When an exception is raised, the program jumps to a specific code block called an exception handler that can handle the exception and prevent the program from terminating abruptly.

The main difference between exceptions and syntax errors is as follows:

Exceptions occur during the runtime of a program, while syntax errors are detected by the Python interpreter before the program starts running.

Syntax errors are caused by violations of the Python language syntax rules, such as misspelled keywords or incorrect indentation. These errors prevent the program from being compiled or interpreted.

Exceptions, on the other hand, occur when the program is running and encounters an unforeseen condition or situation that it cannot handle, such as dividing by zero or accessing an undefined variable.

Syntax errors need to be fixed before the program can be executed, while exceptions can be handled and recovered from within the program using exception handling mechanisms like try-except blocks.|Q2. What happens when an exception is not handled? Explain with an example. When an exception is not handled in a program, it leads to an abrupt termination of the program and an error message is displayed, indicating the type of exception that occurred and the corresponding traceback.
# In[1]:


def divide(a, b):
    result = a / b
    return result

num1 = 10
num2 = 0

result = divide(num1, num2)
print("Result:", result)

 n this example, the divide() function attempts to divide num1 by num2. However, num2 is assigned a value of zero, which raises a ZeroDivisionError exception because dividing by zero is mathematically undefineQ3. Which Python statements are used to catch and handle exceptions? Explain with an example.---> 
In Python, the try and except statements are used to catch and handle exceptions. The try block is used to enclose the code that may raise an exception, and the except block is used to define the code that should be executed when a specific exception occurs.
# In[2]:


def divide(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

num1 = 10
num2 = 0

divide(num1, num2)

Q4. Explain with an example :
    a.try and else 
    b.finally
    c.raise
# In[3]:


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print("Result:", result)

num1 = 10
num2 = 5

divide(num1, num2)

in this example, the try block attempts to divide num1 by num2. If a ZeroDivisionError occurs, the code within the except block is executed and the error message is displayed. However, if no exception occurs, the code within the else block is executed, and the result is printed.b. Example with finally:
# In[4]:


file = None
try:
    file = open("example.txt", "r")
    
except FileNotFoundError:
    print("Error: File not found.")
finally:
    if file:
        file.close()
    print("File operation completed.")

In this example, the try block attempts to open a file named "example.txt" for reading. If a FileNotFoundError occurs, the code within the except block is executed, displaying an error message.c. Example with raise:
# In[5]:


def validate_age(age):
    if age < 0:
        raise ValueError("Invalid age: Age cannot be negative.")
    elif age < 18:
        raise ValueError("Invalid age: Age must be at least 18.")
    else:
        print("Age is valid.")

try:
    validate_age(25)
except ValueError as e:
    print(str(e))

in this example, the validate_age() function is used to validate an age value. If the age is negative or less than 18, a ValueError is raised with an appropriate error messageQ5. What are Custom Exception in python? Why do we need Custom Exceptions? Explain with an exampleCustom exceptions in Python are user-defined exceptions that extend the base Exception class or any of its subclasses. These exceptions are created to handle specific error conditions that are not covered by the built-in exception classes in Python They allow programmers to define their own error types and provide more meaningful and specific information about the exceptional conditions occurring in their programs.
# In[ ]:




