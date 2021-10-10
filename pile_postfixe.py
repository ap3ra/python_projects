# -*- coding: utf-8 -*-
"""
@author: apera
"""

def creePile(n):
    res = [None] * (n+1)
    res[0] = 0
    return res

def estVide(p):
    return p[0] == 0

def empile(x,p):
    p[0] = p[0] + 1
    p[p[0]] = x
    
def depile(p):
    p[0] = p[0] - 1
    return p[p[0] + 1]

def taille(p):
    return p[0]

def sommet(p):
    return(p[p[0]])

def evalue(expr):
    p = creePile(len(expr))
    res = 0
    for lexeme in expr:
        if lexeme == "+":
            x,y = depile(p),depile(p)
            res = x + y
            empile(res,p)
        elif lexeme == "*":
            x,y = depile(p), depile(p)
            res = x*y
            empile(res, p)
        else:
            empile(lexeme, p)
    return res


print(evalue([7,2,'+',3,'*'])) #Resultat 27
