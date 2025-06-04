import random
import time

def quicksort(lista):
    if len(lista) <= 1:
        return lista

    global contador
    pivo = lista[-1]
    menores = []
    iguais = []
    maiores = []

    for i in lista:
        if i < pivo:
            contador += 1
            menores.append(i)
        elif i > pivo:
            contador += 1
            maiores.append(i)
        else:
            contador += 1
            iguais.append(i)

    # Aqui entra a recursão de verdade:
    return quicksort(menores) + iguais + quicksort(maiores)

contador = 0
listaDesordenada = []
with open("lista.txt", "r") as arquivo:
    conteudo = arquivo.read()
    listaDesordenada = [int(i) for i in conteudo.split(", ")]
start_time = time.time()
quicksort(listaDesordenada)
print((time.time() - start_time).__round__(5), "s")
print(contador)

# def gerarLista(nomeArquivo):
#     arquivo = open(nomeArquivo, "w")
#     lista = []
#     for i in range(100000):
#         lista.append(random.randint(1, 100001))
#     arquivo.write(str(lista))
#     arquivo.close()

# gerarLista("lista.txt")
# with open("lista.txt", "r") as arquivo:
