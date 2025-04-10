# https://github.com/Ife-A/lab10-IA-AU
# Partner 1: ifeanyichukwu Alutu
# Partner 2: Ayan Uzzaman


import math


# First example
def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a==0:
        raise ZeroDivisionError
    return b/a
def log(a, b):
    if a<=0 or a==1:
        raise ValueError
    return math.log(b, a)
def exp(a, b):
    return a**b

# Partner 1: Ifeanyichukwu Alutu
# Partner 2: Ayan Uzzaman

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): 
    return a+b


def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b



def logarithm(a,b):
    if a < 1 or b < 1:
        raise ValueError

    return math.log(b,a)

def exponent(a,b):
    return a**b


