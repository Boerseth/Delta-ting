# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 20:06:23 2017

@author: frode
"""
import numpy as np
import matplotlib.pyplot as plt


def LatexPol(coeffs, N, lim, mid, fg, xy):
    retString = ""
    for j in N:
        retString += fg + "_{} ("+xy+") & = \Big("
        i = len(coeffs[j]) - 1
        #Gar gjennom alle koeffisientene i for lokken:
        for coeff in coeffs[j]:
            if coeff >= 0 and i < len(coeffs[j]) - 1:
                retString += " + "
            coeffStr = re.sub('[\[\]]', '', str( coeff ))
            if coeffStr.find('e') > -1:
                coeffStr = re.sub('e', " \cdot 10^{", coeffStr)
                coeffStr += "}"
            retString += " " + coeffStr
            if i != 0:
                retString += " ("+xy+" - " + str(mid[j]) + ")"
                if i > 1:
                    retString +="^{" + str(i) + "}"
            i -= 1
        retString += " \Big)"
        retString += avgrenseLatex(lim[j][0], lim[j][1], xy)
        retString += "\\\\ \n"
    return retString

def polynomial_LaTeX(coef, x_mid, x_end):
    coef = coef[::-1]
    ret_string = "f_{}(x) &= "
    ret_string += "\\Big( "
    ret_string += str(coef[0])
    for i in range(1, len(coef)):
        if coef[i] > 0.0:
            ret_string += " + " + str(coef[i]) + "(x -" + str(x_mid) + ")"
            if i != 1:
                ret_string += "^{" + str(i) + "} "
        else: # Negativ coef, trenger ikke minus-tegn
            ret_string += str(coef[i])
            ret_string += "(x -" + str(x_mid) + ")^{" + str(i) + "} "
    ret_string += "\\Big) "
    ret_string += "\\sqrt{ "
    ret_string += "\\frac{ (x - " + str(x_end[0])
    ret_string += ")(" + str(x_end[1]) + " - x)"
    ret_string += " }{ |(x - " + str(x_end[0])
    ret_string += ")(" + str(x_end[1]) + " - x)|"
    ret_string += " } }\\\\  "
    return ret_string

points = [
        [[0,1,2,3],[4,3,0,1]],
        [[0,1,2,3],[0,1,1,0]],
        [[0,1,2,3],[1,2,4,2]]
        ]

for x_points , y_points in points:
    plt.plot(x_points,y_points)
plt.show()

x_mid_list = []
x_end_list = []
x_interp_list = []
y_interp_list = []
coef_list = []

for x_points , y_points in points:    
    deg = len(x_points) - 1
    x_endpts = [ x_points[0], x_points[-1] ]
    x_interp = np.linspace(x_endpts[0], x_endpts[1])
    x_mid = np.average(x_endpts)
    
    x_points_shifted = [ x-x_mid for x in x_points ]
    x_interp_shifted = [ x-x_mid for x in x_interp ]
    
    
    coef = np.polyfit(x_points_shifted, y_points, deg)
    y_interp = np.polyval(coef, x_interp_shifted)
    
    x_mid_list.append(x_mid)
    x_end_list.append(x_endpts)
    x_interp_list.append(x_interp)
    y_interp_list.append(y_interp)
    coef_list.append(coef)
    
    

for x_int, y_int in zip(x_interp_list, y_interp_list):
    plt.plot(x_int, y_int, "-")
plt.show()

for coef, x_mid, x_endpts in zip(coef_list, x_mid_list, x_end_list):
    print polynomial_LaTeX(coef, x_mid, x_endpts)
    









































"""
points = [
        [[0,1,2,3],[4,3,0,1]],
        [[0,1,2,3],[0,1,1,0]],
        [[0,1,2,3],[1,2,4,2]]
        ]

for x_points, y_points in points:
    plt.plot(x_points, y_points)
plt.show()

x_mid_list = []
x_endpts_list = []
x_interp_list = []
y_interp_list = []
coef_list = []

for x_points, y_points in points:
    deg = len(x_points) - 1
    x_endpts = [ x_points[0], x_points[-1] ]
    x_interp = np.linspace( x_endpts[0], x_endpts[1] )
    x_mid = np.average( x_endpts )
    
    x_points_shifted = [ x-x_mid for x in x_points ]
    x_interp_shifted = [ x-x_mid for x in x_interp ]
    
    coef = np.polyfit(x_points_shifted, y_points, deg)
    y_interp = np.polyval(coef,x_interp_shifted)
    
    x_mid_list.append(x_mid)
    x_end_list.append(x_end)
    x_interp_list.append(x_interp)
    y_interp_list.append(y_interp)
    coef_list.append(coef)
    

for x_int, y_int in zip(x_interp_list, y_interp_list):
    plt.plot(x_int, y_int, "-")
plt.show()

for coef, x_mid, x_endpts in zip(coef_list, x_mid_list, x_endpts_list):
    print polynomial_LaTeX(coef, x_mid, x_endpts)
    
    
    
    
    
    
    

def polynomial_LaTeX(coef, x_mid, x_end):
    coef = coef[::-1]
    ret_string = "f_{}(x) &= "
    ret_string += "\\Big( "
    ret_string += str(coef[0])
    for i in range(1, len(coef)):
        if coef[i] > 0.0:
            ret_string += " + " + str(coef[i]) + "(x -" + str(x_mid) + ")"
            if i != 1:
                ret_string += "^{" + str(i) + "} "
        else: # Negativ coef, trenger ikke minus-tegn
            ret_string += str(coef[i])
            ret_string += "(x -" + str(x_mid) + ")^{" + str(i) + "} "
    ret_string += "\\Big) "
    ret_string += "\\sqrt{ "
    ret_string += "\\frac{ (x - " + str(x_end[0])
    ret_string += ")(" + str(x_end[1]) + " - x)"
    ret_string += " }{ |(x - " + str(x_end[0])
    ret_string += ")(" + str(x_end[1]) + " - x)|"
    ret_string += " } }\\\\  "
    return ret_string
"""