#!/usr/bin/env python
# coding: utf-8

# ## Python Assingment OOP'S part 2
2. What is Abstraction in OOps? Explain with an example.

---> abstraction refers to thea process of simplifying complex systems by breaking them down into more manageable and understandable parts. It involves focusing on essential characteristics and hiding unnecessary details.
# In[1]:


from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, speed, fuel):
        self.speed = speed
        self.fuel = fuel
    
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def refuel(self):
        pass

class Car(Vehicle):
    def move(self):
        print("The car is moving.")

    def refuel(self):
        print("The car is refueling.")

class Motorcycle(Vehicle):
    def move(self):
        print("The motorcycle is moving.")

    def refuel(self):
        print("The motorcycle is refueling.")


# In[2]:


car = Car(speed=60, fuel=50)
car.move()    
car.refuel() 

motorcycle = Motorcycle(speed=80, fuel=30)
motorcycle.move()    
motorcycle.refuel()  

Q2. Differentiate between Abstraction and Encapsulation. Explain with an example. 

---> Abstraction:
Abstraction focuses on creating simplified representations of complex systems by hiding unnecessary details and exposing only essential features.

Encapsulation:
Encapsulation is the practice of bundling related data and behaviors into a single unit, typically called a class.
# In[3]:


class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Encapsulated attribute
        self.__balance = balance  # Encapsulated attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance


# In[4]:


# Create an instance of the BankAccount class
account = BankAccount("123456789", 1000)


print(account.get_balance())  

account.deposit(500)
print(account.get_balance())  

account.withdraw(200)
print(account.get_balance())

Q3. What is abc module in python? Why is it used?

---> The abc module in Python stands for "Abstract Base Classes." It provides mechanisms for defining abstract base classes (ABCs) in Python. An abstract base class is a class that cannot be instantiated directly but serves as a blueprint for defining subclasses.
The abc module in Python is used for several reasons: 
Defining common interfaces: Abstract base classes (ABCs) allow you to define a common set of methods that related classes should implement.
Enforcing method implementation: Abstract base classes can enforce that certain methods must be implemented by subclasses.
Enabling polymorphism: Abstract base classes enable polymorphism, which means that objects of different classes can be treated interchangeably based on their shared interface defined in the abstract base class.
Providing documentation and guidance: Abstract base classes serve as documentation and guidance for developers who need to create subclasses. Q4. How can we achieve data abstraction?

---> ata abstraction can be achieved through the use of classes, objects, and access modifiers. Here are the key steps to achieve data abstraction:

Define a Class: Create a class that represents the abstraction you want to achieve. This class should encapsulate the relevant data and behaviors.

Encapsulate Data: Encapsulate the data within the class by declaring them as private or protected using access modifiers. Private data can only be accessed and modified within the class itself, while protected data can also be accessed by subclasses.

Provide Public Methods: Define public methods, also known as accessor and mutator methods or getters and setters, to provide controlled access to the encapsulated data. These methods allow external code to interact with the class's data without directly accessing or modifying it.

Hide Implementation Details: Make sure to hide the implementation details of the class and expose only the essential functionality. The external code interacting with the class should only need to know about the public methods and not the internal workings of the class.
Q5. Can we create an instance of an abstract class? Explain your answer. 

---> No, we cannot create an instance of an abstract class in Python. Abstract classes are designed to be incomplete and act as blueprints for other classes to inherit from. They serve as a template for creating subclasses that provide concrete implementations for the abstract methods defined in the abstract base class. 
# In[ ]:




