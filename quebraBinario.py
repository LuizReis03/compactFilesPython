# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def quebraBinario(valor):
    converte = int(valor)
    listaBinario = []
    listaQuebrada = []
    listaBinario.append(converte)
    
    for i in range(len(listaBinario)):
        if len(listaBinario) == 8:
            listaQuebrada.append(i)
    print(listaQuebrada)
            

quebraBinario('0001001101010')
