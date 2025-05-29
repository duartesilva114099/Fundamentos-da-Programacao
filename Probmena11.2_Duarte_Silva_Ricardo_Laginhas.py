def ano_bissexto(ano):  # Função que determina se um ano é bissexto
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)  # Um ano é bissexto se for múltiplo de 4 e não for múltiplo de 10

def dias_no_mes(mes, ano):  # Função que retorna o número de dias que um determinado mês pode ter
    if mes == 2:
        return 29 if ano_bissexto(ano) else 28  # Fevereiro tem 29 dias se o ano for bissexto, senão tem 28
    elif mes in [4, 6, 9, 11]:  # Abril, Junho, Setembro, Novembro
        return 30
    elif mes in [1, 3, 5, 7, 8, 10, 12]:  # Meses com 31 dias
        return 31
    else:
        return 0  # Se o mês for inválido (ex: 13), retorna 0

def data_valida(dia, mes, ano): # Função que verifica se a data (dia, mês, ano) é válida
    if mes < 1 or mes > 12:   # Verifica se o mês está entre 1 e 12
        return False
    
    max_dias = dias_no_mes(mes, ano) # Obtém o número máximo de dias para aquele mês e ano
    return 1 <= dia <= max_dias  # Verifica se o dia está no intervalo válido (de 1 até o máximo do mês)

def main():
    entrada = input("Digite uma data no formato dia/mês/ano: ")

    partes = entrada.split('/')   # Divide a string da data nas partes dia, mês e ano
    dia = int(partes[0])
    mes = int(partes[1])
    ano = int(partes[2])
 
    if data_valida(dia, mes, ano):  # Verifica se a data é válida e mostra o resultado
        print("Data válida.")
    else:
        print("Data inválida.")
        
            
main()