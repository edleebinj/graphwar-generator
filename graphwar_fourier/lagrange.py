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

def transf(lb,tr,p): #transform screen coordinates to cartesian coords
    res_two = tuple(map(operator.sub,tr,lb)) #topright - leftbottom
    res = tuple(tempe/2 for tempe in res_two)
    o_two = tuple(map(operator.add,tr,lb))
    o = tuple(temp/2 for temp in o_two)
    pt=((p[0]-o[0])*25/res[0],(p[1]-o[1])*14.6/res[1])
    return pt

#print(lagr(listoftuples))
''' test case
    1,2
    3,4
    (2)(x-3)/(1-3)+(4)(x-1)/(3-1)
'''
