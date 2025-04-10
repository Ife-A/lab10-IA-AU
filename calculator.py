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
