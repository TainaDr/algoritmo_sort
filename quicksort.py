# 
import random
import time
from timeit import main
start_time = time.time()

contador_comparacoes = 0
# Função para ler a lista do arquivo
def ler_lista_do_arquivo(nome_arquivo):
    lista = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                lista.append(int(linha.strip()))
        print(f"Lista carregada do arquivo '{nome_arquivo}'")
        return lista
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado!")
        return None
    except ValueError:
        print("Erro ao ler os números do arquivo!")
        return None
# Função para salvar a lista no arquivo
def salvar_lista_em_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for numero in lista:
            arquivo.write(str(numero) + '\n')
    print(f"Lista salva no arquivo '{nome_arquivo}'")
# Função para ordenar a lista
def quicksort(lista):
    global contador_comparacoes
    if len(lista) <= 1:
        return lista
    pivo = lista[-1]
    maiores = []
    menores = []
    listaPivos = []
    
    for i in lista:
        if i < pivo:
            contador_comparacoes += 1
            menores.append(i)
        elif i > pivo:
            contador_comparacoes += 1
            maiores.append(i)
        else:
            contador_comparacoes += 1
            listaPivos.append(i)
    
    return quicksort(menores) + listaPivos + quicksort(maiores)

def gerarLista():
    lista = []
    # numeros = int(input(print("insira o tamanho da lista: ")))
    for i in range(1, 100001):
        lista.append(i)
    # print(lista)
    return lista

def main():
    # Lista para armazenar os resultados
    tempos = []
    comparacoes = []
    
    print("\nExecutando quicksort 5 vezes com lista de 100.000 números...")
    print("-" * 50)
    
    for i in range(5):
        # Resetar contador de comparações
        global contador_comparacoes
        contador_comparacoes = 0
        
        # Gerar e embaralhar lista
        lista = gerarLista()
        random.shuffle(lista)
        
        # Executar quicksort e medir tempo
        print(f"\nExecução {i+1}:")
        tempo_inicio = time.time()
        lista_ordenada = quicksort(lista)
        tempo_fim = time.time()
        
        # Guardar resultados
        tempo_execucao = tempo_fim - tempo_inicio
        tempos.append(tempo_execucao)
        comparacoes.append(contador_comparacoes)
        
        # Mostrar resultados desta execução
        print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
        print(f"Número de comparações: {contador_comparacoes}")
    
    # Mostrar estatísticas finais
    print('')
    print("RESULTADOS FINAIS:")
    print(f"Tempo médio: {sum(tempos)/5:.4f} segundos")
    print(f"Média de comparações: {sum(comparacoes)/5:.0f}")

if __name__ == "__main__":
    main()