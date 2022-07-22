#listoftuples=[(0,1),(2,5),(4,17)]
from symfit import parameters, variables, sin, cos, Fit
import numpy as np
import matplotlib.pyplot as plt
import operator
def pa(a): #add parenthesis
    par="("+str(a)+")"
    return par
def lagr(lots): #create lagrange interpolation function. input lists of tuples
    resultf=""
    for h,i in lots:
        resultf+="+"+pa(i)
        for j,k in lots:
            if(j!=h):
                resultf+=pa("x"+"-"+str(j))
        resultf+="/("
        for l,m in lots:
            if(l!=h):
                resultf+=pa(str(h)+"-"+str(l))
        resultf+=")"
    
    return resultf

def transf(o,tr,p): #transform screen coordinates to cartesian coords
    res = tuple(map(operator.sub,tr,o)) #topright - origin
    pt=((p[0]-o[0])*25/res[0],(p[1]-o[1])*14.6/res[1])
    return pt

#print(lagr(listoftuples))
''' test case
    1,2
    3,4
    (2)(x-3)/(1-3)+(4)(x-1)/(3-1)
'''
