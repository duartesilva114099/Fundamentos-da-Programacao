# -*- coding: utf-8 -*-
"""
Created on Wed May  7 17:51:37 2025

@author: Duarte Silva
"""

def consumo_medio():
    with open("consumo_combustivel.txt", "r") as file:  #abre o ficheiro de dados "consumo_combustivel.txt" e lê os dados (r de read)
        linhas = file.readlines()                #lê todas as linhas presentes no ficheiro e guarda-as numa lista de strings
        
        odometro_inicio = float(linhas[0].strip())   #Pega na primeira linha do ficheiro, remove espaços em branco e converte para decimal
        trajetos = [list(map(float, line.split())) for line in linhas[1:]] #Pega na segunda linha do ficheiro, separa por espaços, converte em decimal e cria uma lista de dados 
        odometros_finais = [trajeto[0] for trajeto in trajetos]  #cria uma lista com os valores finais do odómetro
        combustiveis = [trajeto[1] for trajeto in trajetos]   #cria uma lista com os valores de combustível consumido

        odometros = [odometro_inicio] + odometros_finais            #Coloca o odómetro inicial na lista dos odómetros finais
        calcular_consumo_medio(odometros, combustiveis)
        
def calcular_consumo_medio(odometros, combustiveis):
    distancia_total = odometros[-1] - odometros[0]      #[-1] faz retornar o último valor da lista calculando a distância total da viagem
    combustivel_total = sum(combustiveis)               # soma os valores dos combustiveis
    consumo_medio_total = (combustivel_total / distancia_total) * 100
    print(f"Consumo médio total a cada 100 kms: {consumo_medio_total:.2f} litros\n")        #Consumo médio total com 2 casas decimais

    for i in range(1, len(odometros)):   #ciclo que começa no primeiro elemento e acaba em len(odometros) que é o comprimento da lista odometros 
        distancia = odometros[i] - odometros[i-1]   #Calcula a distância do trajeto: odometro atual menos o odómetro anterior
        consumo_medio = (combustiveis[i-1] / distancia) * 100   #Calcula o consumo médio de 100km. Começa na posição i-1 porque a lista tem uma entrada a menos
        print(f"Trajeto {i}: {consumo_medio:.2f} litros por 100 Km")
    
consumo_medio()