# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 01:52:24 2025

@author: Duarte Silva
"""
#futval.py
#   Programa para calcular o futuro valor de um investimento.
#by: Duarte Silva

def investir():
        print("Este programa calcula o valor futuro de um investimento.")
    
        inicial = eval(input("\nInsira o valor do investimento inicial: "))
        juros = eval(input("\nInsira a taxa de juros anual em percentagem: "))
        anos = eval(input("\nInsira a duração do investimento em anos: "))
    
        for i in range (anos):
            inicial = inicial * (1 + (juros/100))
            
        print("\nO valor do investimento em", anos, "anos é", inicial)

investir()
input("\n---------Prima enter para fechar o programa---------")