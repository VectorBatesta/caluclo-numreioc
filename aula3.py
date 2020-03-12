# -*- coding: utf-8 -*-
import math

def funcao(x):
    retornar = -4 + 8 * x - 5 * math.pow(x,2) + math.pow(x,3)
    return retornar

def quantRaizes(funcao, inferior, superior, itermax, ea):
    iteracoes = 0
    while(iteracoes < itermax and abs(funcao(superior) - funcao(inferior)) > ea):
        iteracoes = iteracoes + 1
        middle = (superior + inferior) / 2
        if(funcao(inferior) * funcao(middle) < 0):
            superior = middle
        else:
            inferior = middle
    print("inferior: ", inferior, ", superior: ", superior, ", iteracoes: ", iteracoes)
    return iteracoes

inferior = 1/2
superior = 3
iteracoes = quantRaizes(funcao, inferior, superior, 500, pow(10,-20))
print(iteracoes)
