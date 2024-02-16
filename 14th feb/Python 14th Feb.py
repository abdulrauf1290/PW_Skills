#!/usr/bin/env python
# coding: utf-8
Q2.Why threading module used? rite the use of the following functions
1.activeCount()
2.currentThread()
3.enumerate()---> The threading module in Python is used for creating and managing threads, which are separate flows of execution within a program.
activeCount(): This function returns the number of Thread objects currently alive.
currentThread(): This function returns the Thread object representing the currently executing thread.
enumerate(): This function returns a list of all Thread objects currently alive.3.Explain the following functions

1.run()
2.start
3.join
4.isAlive()run(): The run() method is a fundamental method of a thread class. It contains the code that will be executed when the thread is started. 

start(): The start() method is used to initiate the execution of a thread. When you call start() on a thread object, it schedules the thread to run independently.

join(): The join() method is used to wait for a thread to complete its execution. When you call join() on a thread object, the calling thread (usually the main thread) will be blocked until the target thread finishes executing.

isAlive(): The isAlive() method is used to check whether a thread is currently running or not. It returns True if the thread is still active and executing its code, and False otherwise
# Q4. write a python program to create two threads. Thread one must print the list of squares and thread
# two must print the list of cubes.

# In[1]:


import threading

def print_squares():
    for num in range(1, 6):
        square = num ** 2
        print(f"Square of {num}: {square}")

def print_cubes():
    for num in range(1, 6):
        cube = num ** 3
        print(f"Cube of {num}: {cube}")

thread1 = threading.Thread(target=print_squares)

thread2 = threading.Thread(target=print_cubes)

thread1.start()
thread2.start()


thread1.join()
thread2.join()

print("Program execution completed.")

Q5. State advantages and disadvantages of multithreadingAdvantages of Multithreading:

Improved performance through parallel processing.

Enhanced responsiveness and user experience.

Efficient resource sharing and utilization.

Simplified program structure and coordination.

Disadvantages of Multithreading:

Increased complexity and difficulty in development.

Higher risk of bugs and synchronization issues.

Overhead and resource consumption.

Limited scalability in certain scenarios. 6. Explain deadlocks and race conditions.A deadlock occurs when two or more threads or processes are indefinitely blocked, waiting for each other to release resources. It typically happens when each thread holds a resource that another thread requires to proceed, creating a circular dependency. 
# In[ ]:





# In[ ]:




