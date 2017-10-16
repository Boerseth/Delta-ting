# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 20:06:23 2017

@author: frode
"""
import numpy as np
import matplotlib.pyplot as plt

# Denne kan forbedres.
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

# Listen lister over punkt som skal interpoleres. Si du
# vil interpolere de  n  punktene
#
#      (x0,y0) , (x1,y1) , ... , (xn,yn)
#
# du putter da  x  og  y  verdier i hver sin liste,
#
#       [x0,x1,...,xn]   [y0,y1,...,yn]
#
# setter dem etter hverandre i ei ny liste,
#
#     [ [x0,x1,...,xn] , [y0,y1,...,yn] ]
#
# og setter dette inn i lista points:
#
# points = [
#           [ [x0,x1,...,xn], [y0,y1,...,yn] ]
#          ]
# 
# For flere interpoleringer bare legger du til nye linjer med
# x  og  y  verdier.
#
# points = [
#           [ [x0,x1,...,xn], [y0,y1,...,yn] ],
#           [ [x0,x1,...,xn], [y0,y1,...,yn] ],
#           [ [x0,x1,...,xn], [y0,y1,...,yn] ],
#           [ [x0,x1,...,xn], [y0,y1,...,yn] ]
#          ]
# 
points = [
        [[0,1,2,3],[4,3,0,1]],
        [[0,1,2,3],[0,1,1,0]],
        [[0,1,2,3],[1,2,4,2]]
        ]

## Fjern kommentartegnene hvis du vil plote punktene.
#for x_points , y_points in points:
#    plt.plot(x_points,y_points)
#plt.show()


# Disse listene fylles med data for hvert linjestykke i
# loopen nedenfor
x_mid_list = []
x_end_list = []
x_interp_list = []
y_interp_list = []
coef_list = []

# Hver loop tar vi et set med  x_points,y_points  og
# interpolerer med et polynom slik at det blir ei linje.
for x_points , y_points in points:    
    # deg:      int - degree, hvilken grad polynomet skal ha
    # x_endpts: liste - endepunkt langs x-aksen
    # x_interp: liste - mange x-verdier mellom endepunktene
    # x_mid:    flyttall - midt mellom endepunktene
    deg = len(x_points) - 1
    x_endpts = [ x_points[0], x_points[-1] ]
    x_interp = np.linspace(x_endpts[0], x_endpts[1])
    x_mid = np.average(x_endpts)
    
    # Polynomets koeffisienter regnes ut etter at vi forskyver
    # x-verdiene rundt  0.  Dette gir oss penere tall.
    #
    #  f(x)  =  c0  +  c1(x-h)  +  c2(x-h)^2  + ... +  cn(x-h)^n
    #
    x_points_shifted = [ x-x_mid for x in x_points ]
    x_interp_shifted = [ x-x_mid for x in x_interp ]
    
    # Funksjonene  polyfit  og  polyval  er magiske ting som
    # bare fungerer.
    coef = np.polyfit(x_points_shifted, y_points, deg)
    y_interp = np.polyval(coef, x_interp_shifted)
    """
        I lista  coef  plasseres da koeffisientene, men i en
        litt rar rekkefolge:

                coef = [ c_n , c_n-1 , ... , c_1, c_0 ]
        
        funksjonen polyval tar seg av det uansett, du trenger
        ikke tenke over dette, med mindre du vil fikse LaTeX-
        funksjonen over.

        Grunnen til detter er at evaluering av polynomet blir
        enkelt og raskt for en gitt  x  :
        
        y = 0
        for c in coef:
            y = y*x + c

        men igjen, ikke noe man trenger tenke over.
    """
    
    # Legg til alt vi nettop har regnet ut i listene.
    x_mid_list.append(x_mid)
    x_end_list.append(x_endpts)
    x_interp_list.append(x_interp)
    y_interp_list.append(y_interp)
    coef_list.append(coef)
    
    
"""
    En hendig funksjon er  zip().  Den tar to like lange lister,

                a = [ a0,       b = [ b0,
                      a1,             b1,
                      ...             ...
                      an ]            bn ]

    og lager ei liste med  ai,bi  par (tenk engelsk zipper):

                zip(a,b) = [ [a0,b0],
                             [a1,b1],
                             ...
                             [an,bn] ]
    
    Slik hentes  x_interp, y_interp  par ut sammen under.
"""
# For alle set med punkt vi nettop interpolerte, plot interpoleringen.
for x_int, y_int in zip(x_interp_list, y_interp_list):
    plt.plot(x_int, y_int, "-k")
plt.show()

# Selfe funksjonen er definert bare fra polynomets koeffisienter,
# midtpunktet, og endepunktene.
for coef, x_mid, x_endpts in zip(coef_list, x_mid_list, x_end_list):
    print polynomial_LaTeX(coef, x_mid, x_endpts)
