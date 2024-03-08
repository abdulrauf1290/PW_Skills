#!/usr/bin/env python
# coding: utf-8

# ## OOP'S Task
Q1, Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed
and average_of_vehicle.
# In[2]:


class vehicle:
    
    def __init__(self,name_of_vehicle,max_speed,average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle


# In[3]:


car = vehicle("car" ,200 ,30)


# In[4]:


car.name_of_vehicle


# In[5]:


car.max_speed


# In[6]:


car.average_of_vehicle

Q2. Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.
Create a method named seating_capacity which takes capacity as an argument and returns the name of
the vehicle and its seating capacity.

# In[7]:


class Car(vehicle) :
    
    def searting_capacity(self,capacity):
        return f"{self.name_of_vehicle} has a seating capacity of {capacity} people."


# In[8]:


car = Car('fortuner',20,30)
car.searting_capacity(8)

Q3. What is multiple inheritance? Write a python code to demonstrate multiple inheritance.---> Multiple inheritance is a feature in object-oriented programming where a class can inherit attributes and methods from more than one parent class. This allows a derived class to have characteristics and behaviors from multiple source classes.
# In[9]:


''' an example code that demonstrates multiple inheritance in Python '''
class Vehicle:
    def __init__(self, name):
        self.name = name

    def drive(self):
        print(f"{self.name} is being driven.")

class FlyingVehicle:
    def fly(self):
        print(f"{self.name} is flying.")

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)

class FlyingCar(Car, FlyingVehicle):
    def __init__(self, name):
        super().__init__(name)

car = FlyingCar("SkyCar")
car.drive()
car.fly()

Q4. What are getter and setter in python? Create a class and create a getter and a setter method in this
class.---> Getters and setters are methods used to access and modify the attributes (variables) of a class, encapsulating them and providing controlled access to them.
# In[10]:


class Person:
    def __init__(self, name):
        self._name = name 

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name


person = Person("Sharukh")

print(person.get_name())  

person.set_name("Tiger")

print(person.get_name())  

Q5.What is method overriding in python? Write a python code to demonstrate method overriding.

---> Method overriding is a concept in object-oriented programming where a subclass provides its own implementation of a method that is already defined in its parent class. This allows the subclass to modify or extend the behavior of the inherited method.
# In[11]:


class Vehicle:
    def drive(self):
        print("Driving the vehicle.")

class Car(Vehicle):
    def drive(self):
        print("Driving the car.")

class Truck(Vehicle):
    def drive(self):
        print("Driving the truck.")

car = Car()
truck = Truck()

car.drive()  
truck.drive() 


# In[ ]:




