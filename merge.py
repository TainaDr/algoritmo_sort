import random
import time

lista_numeros = []

#Gera a lista
for numero in range(1, 100000):
    lista_numeros.append(numero)

#Embaralha os números da lista
random.shuffle(lista_numeros)
#Salva a lista embaralhada em um arquivo txt
with open("lista_numeros_embaralhados.txt", "w") as arquivo:
    for numero in lista_numeros:
        arquivo.write(f"{numero}\n")

#Função de ordenação --> Merge Sort
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
#Divide a lista ao meio, separando em duas sublistas, esquerda e direita
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
#Combina as duas metades ordenadas
    return merge(esquerda, direita)

# Função para mesclar as duas listas ordenadas em uma lista final ordenada
def merge(esquerda, direita):
    resultado = [] #Lista onde o resultado será armazenado
    i = j = 0 #Índices para percorrer esquerda (i) e direita (j)
    global contador #Contador para contar o número de comparações
    contador = 0
#Compara os elementos das duas listas e insere o menor no resultado
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            contador += 1
            i += 1
        else:
            resultado.append(direita[j])
            contador += 1
            j += 1
#Adiciona os elementos restantes da lista esquerda (se houver)
    resultado.extend(esquerda[i:])
#Adiciona os elementos restantes da lista direita (se houver)
    resultado.extend(direita[j:])
    return resultado

#Marca o tempo de início da ordenação
inicio = time.time()
#Ordena a lista utilizando merge sort
lista_ordenada = merge_sort(lista_numeros)
#Marca o tempo de término da ordenação
fim = time.time()

#Imprime o tempo total de execução
print("--------------------------------")
print(f"Tempo de execução: {fim - inicio:.2f} segundos")
print("--------------------------------")
print(f"Quantidade de comparações: {contador}")

#Salva a lista ordenada em um arquivo txt
with open("numeros_ordenados.txt", "w") as arquivo:
    for numero in lista_ordenada:
        arquivo.write(f"{numero}\n")
