import math
import numpy as np

def myEquation1(x):    
    return -1 * (x**3)

def myEquation2(x):    
    return -3 * (x**2)

def newton(a, iteration, my_func, my_func2):    
    iteration = iteration + 1    
    if my_func(a) < 0.0000001 and my_func(a) > (-1 * 0.0000001):        
        print("case close")        
        print("iteration: ", str(iteration).ljust(3), "  x: ", str(a).ljust(25))    
    elif my_func(a) != 0:        
        a_1 = a - (my_func(a)/my_func2(a))        
        #print("iteration: ", str(iteration).ljust(3), "  x1: ", str(a).ljust(25), "  x2: ", str(a_1).ljust(25))        
    
        newton(a_1, iteration, my_func, my_func2)
    
newton(-100, 0, myEquation1, myEquation2)
