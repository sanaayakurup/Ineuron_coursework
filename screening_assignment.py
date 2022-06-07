# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 10:40:27 2022

@author: sanaayak
"""

#answer 1 
def replace_text(file):
    try:
        with open(file,'r') as f:
            data=f.read()
            print(data)
            data=data.replace('placement','screening')
            print(data)
        with open(file,'w') as f:
            f.write(data)
    except Exception as e:
            print(e)
            
    else:
            print('file was read and overwritten')
           
replace_text('example.txt')        #text in the file gets replaced     
    
#answer 2 Demonstrate use of abstract class, multiple inheritance and decorator in python using examples.    
#abstract class
from abc import ABC, abstractmethod

class ExampleofAbstractClass(ABC):
    @abstractmethod
    def do_something(self):
        print('Implement this')
        
class SubclassOne(ExampleofAbstractClass):
    def do_something(self):
        super().do_something()
        print('this is another subclass')

x = SubclassOne()
x.do_something()


##Multiple Inheritence 
class A1:
    def m(self):
        print("In A1")
 
class A2(A1):
    def m(self):
        print("In A2")
        super().m()
 
class A3(A1):
    def m(self):
        print("In A3")
        super().m()
 
class A4(A2, A3):
    def m(self):
        print("In A4")  
        super().m()
      
obj = A4()
obj.m()

#DECORATOR example 
def star_pattern(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent_patterns(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star_pattern
@percent_patterns
def printer_with_both(msg):
    print(msg)


printer_with_both("Hi!I am learning python")
        
