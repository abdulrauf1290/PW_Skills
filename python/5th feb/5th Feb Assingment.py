#!/usr/bin/env python
# coding: utf-8

# ## Assingment on OOP's
Q1. Explain Class and Object with respect to Object-Oriented Programming.Give a suitable example.---> In object-oriented programming (OOP), a class is a blueprint or a template for creating objects. It defines the properties (attributes) and behaviors (methods) that objects of that class can have. A class provides a way to encapsulate data and functions into a single unit
# In[1]:


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)

# Creating objects (instances) of the Rectangle class
rectangle1 = Rectangle(5, 3)
rectangle2 = Rectangle(7, 4)

# Accessing object properties
print(rectangle1.width)  # Output: 5
print(rectangle2.height)  # Output: 4

# Invoking object methods
area1 = rectangle1.get_area()
print(area1)  

perimeter2 = rectangle2.get_perimeter()
print(perimeter2) 

Q2.Name the Four Pillars of OOPs.---> The four pillars of object-oriented programming (OOP) are:
    1)Encapsulation: Encapsulation is the process of bundling data (attributes) and methods (behaviors) together within a class.
    2)Inheritance: Inheritance allows a class to inherit properties and methods from another class.
    3)Polymorphism: Polymorphism refers to the ability of objects of different classes to be treated as objects of a common base class.
    4)Abstraction: Abstraction involves simplifying complex systems by focusing on essential features while hiding unnecessary detailsQ3. Explain why the __init__() function is used. Give a suitable example
---> The __init__() function is a special method in Python classes that is automatically called when an object is created from the class.
# In[2]:


class myskills1:
    
    def __init__(self,phone_number , email_id, student_id ):
        self.phone_number = phone_number
        self.email_id = email_id
        self.student_id = student_id
    def return_student_details(self):
        return self.student_id, self.phone_number, self.email_id


# In[3]:


rohan=myskills1(456465,"rohan@gmail.com",101)


# In[4]:


rohan.return_student_details()

Q4. Why self is used in OOPs?
--->In object-oriented programming (OOP), the self parameter is used to refer to the instance of a class within its own methods. It is a convention in Python to use the name self as the first parameter of instance methods.Q5. What is inheritance? Give an example for each type of inheritance
---> Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class to inherit properties and behaviors from another class.
# In[5]:


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("The animal is eating.")

class Dog(Animal):
    def bark(self):
        print("The dog is barking.")

# Creating an object of the derived class
dog = Dog("Buddy")

# Accessing attributes and methods from the base class
print(dog.name)  
dog.eat()  

# Accessing method from the derived class
dog.bark()  


# In[ ]:




