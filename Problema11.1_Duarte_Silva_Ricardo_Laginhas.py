def QuadradoElementos(numeros): # Função que eleva ao quadrado cada elemento da lista
    for i in range(len(numeros)):
        numeros[i] = numeros[i] ** 2 #Lê os números do ficheiro e devolve os respetivos quadrados

def SomatorioLista(numeros): # Função que calcula o somatório dos elementos da lista
    return sum(numeros) #Apenas soma os quadrados devolvidos pela função anterior

def ConverteEmNumeros(ListaCaracteres): # Função que converte strings para números do tipo float
    for i in range(len(ListaCaracteres)):
        ListaCaracteres[i] = float(ListaCaracteres[i].strip())

def main():
    nome_ficheiro = input("Nome do ficheiro a ler: ")  # Pede o nome do ficheiro na forma nome.txt
    try:
        with open(nome_ficheiro, 'r') as ficheiro:
            linhas = ficheiro.readlines()

        linhas = [linha.strip() for linha in linhas if linha.strip() != ''] #Ignora os espaços extra e linhas não escritas
        ConverteEmNumeros(linhas)  # Converte as linhas para números
        QuadradoElementos(linhas)  # Calcula os quadrados
        resultado = SomatorioLista(linhas)   # Soma os quadrados
        print("Soma dos quadrados dos números do ficheiro:", resultado)

    except FileNotFoundError:
        print("Erro: ficheiro não encontrado.")
    except ValueError:
        print("Erro: o ficheiro contém valores inválidos (não numéricos).")
        
main()
