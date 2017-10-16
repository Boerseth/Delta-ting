# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 14:25:42 2017

@author: frode
"""

import numpy as np

fraser = [
        "En ridder er i mot",
        "En person som stiller er ikke til stede",
        "Noen spør om ludøl",
        "Jeg er ikke bitter",
        "Alt var bedre før",
        "Hva har vi lært?",
        "Kast styret",
        "Stilling må stemmes over to ganger",
        "Jone er til stede",
        "Ole Martin kommenterer samme sak for 3. gang",
        "Einar skypes inn for å argumentere",
        "En person stiller gjennom skype",
        "Mathias godtar benking",
        "Noen blir benket",
        "En førsteklassing presenterer stattutendringsforslag",
        "Kun en person stiller til en stilling",
        "En person stiller til flere stillinger",
        "Fire eller flere kandidater til en stilling",
        "En førsteklassing blir valgt inn i styret",
        "Peter skypes inn for å argumentere",
        "Økonomisjef må forklare fortegn i budskjett",
        "Genvors varer i over 5 timer",
        "Går tom for kaffe",
        "Noen må være ingeniør",
        "Tom for tørre kjeks",
        "To kandidater får like mange stemmer",
        "Patrick har glemt pisken",
        "Akklamasjon",
        "Statuttdiskusjon går over tiden",
        "Saksopplysning",
        "Noen sovner",
        "Noen gjør øving",
        "Trump blir nevnt i noen som helst kontekst",
        ]


latex_string = ""

for k in range(50):
    board = np.random.choice(fraser, size=25, replace=False)
    latex_string += "\\begin{tabular}{|c|c|c|c|c|}\n"
    latex_string += "\\hline\n"
    latex_string += " B & I & N & G & O "
    latex_string += "\\\\ \n"
    for i in range(5):
        latex_string += "\\hline\n"
        for j in range(5):
            if i==2 and j==2:
                latex_string += "\\begin{minipage}{0.18\\textwidth}\n"
                latex_string += "\\centering \n"
                latex_string += "\\mbox{}\\\\ \n"
                latex_string += "\tGRATIS\\\\ \n"
                latex_string += "\\mbox{}\\\\ \n"
                latex_string += "\\end{minipage}\n"
            else:
                latex_string += "\\begin{minipage}{0.18\\textwidth}\n"
                latex_string += "\\centering \n"
                latex_string += "\\mbox{}\\\\ \n"
                latex_string += "\t"+board[i*5 + j]+"\\\\ \n"
                latex_string += "\\mbox{}\\\\ \n"
                latex_string += "\\end{minipage}\n"
            if j != 4:
                latex_string += "&\n"
        latex_string += "\\\\ \n"
    latex_string += "\\hline\n"
    latex_string += "\\end{tabular}\n"
    latex_string += "\n"
    latex_string += "\\vspace{\\fill} \n"
    latex_string += "\n"
    board = np.random.choice(fraser, size=25, replace=False)
    latex_string += "\\begin{tabular}{|c|c|c|c|c|}\n"
    latex_string += "\\hline\n"
    latex_string += " B & I & N & G & O "
    latex_string += "\\\\ \n"
    for i in range(5):
        latex_string += "\\hline\n"
        for j in range(5):
            if i==2 and j==2:
                latex_string += "\\begin{minipage}{0.18\\textwidth}\n"
                latex_string += "\\centering \n"
                latex_string += "\\mbox{}\\\\ \n"
                latex_string += "\tGRATIS\\\\ \n"
                latex_string += "\\mbox{}\\\\ \n"
                latex_string += "\\end{minipage}\n"
            else:
                latex_string += "\\begin{minipage}{0.18\\textwidth}\n"
                latex_string += "\\centering \n"
                latex_string += "\\mbox{}\\\\ \n"
                latex_string += "\t"+board[i*5 + j]+"\\\\ \n"
                latex_string += "\\mbox{}\\\\ \n"
                latex_string += "\\end{minipage}\n"
            if j != 4:
                latex_string += "&\n"
        latex_string += "\\\\ \n"
    latex_string += "\\hline\n"
    latex_string += "\\end{tabular}\n"
    latex_string += "\\newpage\n"
    
f1=open('./tables.tex', 'w+')
f1.write(latex_string)
f1.close()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        