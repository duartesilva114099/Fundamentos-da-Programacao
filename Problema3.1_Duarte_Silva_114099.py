# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 00:51:49 2025

@author: Duarte Silva
"""
#convert.py
#   Programa para converter graus Celsius em Fahrenheit
#by: Duarte Silva

def temperatura():
    print("Este programa apresenta uma tabela com as temperaturas em graus Celsius vs Fahrenheit (máximo = 100ºC)")
    
    celsius = eval(input("\nQual é a temperatura em graus Celsius que deseja começar? "))
    
    print("\nCelsius | Fahrenheit\n--------------------") 
    for celsius in range (celsius,101,10):
        fahrenheit = 9/5 * celsius + 32
        
        print(celsius,"->",fahrenheit)

temperatura()
input("\n---------Prima enter para fechar o programa---------")