#!/usr/bin/env python
# coding: utf-8
Q1. Write a program to accept percentage from the user and display the grade according to the following criteria
# In[1]:


marks = int(input("Enter Your Marks "))

if marks > 90 :
    print("A")
elif marks > 80 and marks <=90 :
    print("B")
elif marks >= 60 and marks <= 80 :
    print("C")
else :
    marks < 60
    print("D")

Q2. write a program to accept the cost price of a bike and display the road tax t be paid according to the following criteria
# In[2]:


cost_price = int(input("what is price of bike"))
if cost_price > 100000 :
    print("15%")
elif cost_price > 50000 and cost_price <= 100000 :
    print("10%")
else :
    cost_price <= 50000 
    print("5%")

Q3. Accept any city from the user and display monuments of that city 
# In[7]:


City = str(input("Enter The City Name"))
if City == "Delhi" :
    print("Read Fort")
elif City == "Agra" :
    print("Taj Mahal")
elif City == "jaipur" :
    print("Jal Mahal")
elif City == "Aurangabad" :
    print("Bibi Ka Maqbara")
else : 
    print("Enter valid city name ")


# Q4.Check how many ties a given number can be divided by 3 before it is less than or equal to 10

# In[8]:


number = int(input("Enter a number: "))
count = 0

while number > 10:
    number /= 3
    count += 1

print("The number can be divided by 3", count, "times before it is less than or equal to 10.")

Q5.why and when to use wile loop in python give a detailed description with example 
--> A while loop is a type of loop in Python that allows us to repeatedly execute a block of code as long as a specified condition is true. The condition is checked at the beginning of each iteration, and the loop continues to run until the condition is no longer true.

The while loop is useful when we want to repeatedly execute a block of code until a specific condition is met. For example, we can use a while loop to repeatedly prompt the user for input until they enter a valid input. We can also use a while loop to repeatedly perform calculations or operations until a certain result is achieved.
For example, here is a while loop that calculates the factorial of a given number:

number = int(input("Enter a positive integer: "))
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print("The factorial of", number, "is", factorial)Q.6 Use Nested While loop to print 3 diffrent pattern
# In[9]:


n = 6
i = 1

while i <= n:
    j = 1
    while j <= i:
        print(i, end=' ')
        j += 1
    print()
    i += 1

Pattern 2:
# In[10]:


n = 5
i = 1

while i <= n:
    j = 1
    while j <= i:
        print('*', end=' ')
        j += 1
    print()
    i += 1

Pattern 3:
# In[11]:


n = 5
i = 1

while i <= n:
    j = 1
    while j <= i:
        print(j, end=' ')
        j += 1
    print()
    i += 1

Q7. Reverse a while loop to display numbers from 10 to 1
# In[12]:


n = 10
while n >= 1:
    print(n)
    n -= 1


# In[ ]:





# In[ ]:




