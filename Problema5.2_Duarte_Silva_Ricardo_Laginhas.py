# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 13:03:33 2025

@author: Duarte Silva
"""

#Problema 5.2

def conta_palavras():
    frase=input("Escreva uma frase: ")
    palavras=frase.split()      #Dividir a frase em palavras
    
    print(f"\nA frase contém {len(palavras)} palavras.")   #funçã len() conta o número de elementos na frase
    
conta_palavras()
input("\n---------Prima enter para fechar o programa---------")
