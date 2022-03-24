# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def quebraBinario(valor):
    listaBit = []
    for i in valor:
        if len(listaBit) < 8:
            listaBit.append(i)
    return listaBit
            
        
    
    
    
arquivo = [0,0,0,0,0,0,1,1,0,1,0,0,0,1,0]
print(quebraBinario(arquivo))