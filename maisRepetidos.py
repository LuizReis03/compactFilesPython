"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

def maisRepetidos(valor):
    repetidos = []
    for i in valor:
        if not i in repetidos:
            repetidos.append(i)
    for i in repetidos:
        print(valor.count(i))

arquivo = [4,4,4,4,6,8,8,7]
maisRepetidos(arquivo)