## Nome: Pedro Gasparelo Leme - 14602421
## Nome: Gabriel Dezejácomo Maruschi - 14571525

# Codigo paara o curso de estatistica - Objetivo: analizar o tempo de processamento de diferentes algoritmos de ordenação dependendo do tamanho da entrada, sempre considerando um caso medio

## algoritmos a serem usados: BubbleSort/ SelectionSort -> BigO(n²) // MergeSort/QuickSort BigO(n Log[n]) // RadixSort BigO(nk). para n sendo o tamanho da entrada

import time
import matplotlib.pyplot as plt

## medir tempo inicio = time.perf_counter()

## definição das funções 

# BigO(n²)

def bubble_sort(arr): # ordena colocando o numero de maior valor na posição correta
    n = len(arr) # obtem tamanho do array para ser ordenado
    inicio = time.perf_counter() # inicia o contador de tempo antes da ordenação iniciar
    troca = False
    for i in range(n): 
        # passa pela lista do início até o penúltimo elemento
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # troca os elementos se estiverem fora de ordem
                aux = arr[j]
                arr[j] = arr[j + 1] 
                arr[j + 1] = aux
                troca = True
        if troca == False: # se nao teve troca, entao nao precisa mais 
            break
    fim = time.perf_counter()
    return (fim - inicio) #retorna o tempo total para que ocorra a ordenação

def selection_sort(arr): # ordena os numeros de menores valores na posicao correta primeiro
    n = len(arr) # obtem tamanho do array para ser ordenado
    inicio = time.perf_counter() # inicia o contador de tempo antes da ordenação iniciar
    for i in range(n):
        # encontra o índice do menor elemento na parte não ordenada
        pos_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[pos_min]:
                pos_min = j # guarda o indice do numero de menor valor 
        # Troca o menor elemento encontrado na sua posicao correta
        aux = arr[i]
        arr[i] = arr[pos_min]
        arr[pos_min] = aux
    fim = time.perf_counter()
    return (fim - inicio) #retorna o tempo total para que ocorra a ordenação

# BigO( n log[n] )

def merge_sort(arr):
    if len(arr) > 1: # se for igual a 1, retorna o proprio valor do array, voltando assim a arvore de recursao das metades separadas
        meio = len(arr) // 2
        esquerda = arr[:meio] # notação para array que copia todos os numeros do array original, da metade para frente
        direita = arr[meio:]  # notação para array que copia todos os numeros do array original, da metade para tras

        # Utiliza recursão para ordenar o array em metades
        merge_sort(esquerda)
        merge_sort(direita)

        # combina as duas metades ordenadas 
        i = j = k = 0
        while i < len(esquerda) and j < len(direita): # caso ainda esteja comparando os valores dos 2 arrays, pois eles ainda existem
            # verifica qual possui menor valor para colocar em ordem crescente no array de retorno
            if esquerda[i] < direita[j]:
                arr[k] = esquerda[i]
                i += 1
            else:
                arr[k] = direita[j]
                j += 1
            k += 1

        # caso ainda sobre valores em um array enquanto o outro ja foi finalizado, preenche o array de retorno com o restante
        while i < len(esquerda):
            arr[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            arr[k] = direita[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) <= 1: # se tamanho do array for igual a 1, significa que a partição realizada pela chamada consecutiva da funcao recursiva, ja foi realizada
        return arr
    else:
        pivo = arr[0] # escolhendo o pivot como o primeiro elemento
        # coloca todos os valores do pivot escolhido a esquerda, caso eles sejam menores que o pivot
        menores = [x for x in arr[1:] if x <= pivo] 
        maiores = [x for x in arr[1:] if x > pivo]
        return quick_sort(menores) + [pivo] + quick_sort(maiores) # retorna a recursao da ordenação da metade menor que o pivot e maior que ainda devem ser organizadas

#BioO(nk)

# definicao de uma função auxiliar que fara a contagem de digito a digito em especifico
def counting_sort_digito(arr, digito):
    n = len(arr) # obtem o tamanho da lista
    output = [0] * n # definicao da lista de saída, a qual esta inicialmente vazia
    count = [0] * 10 # definicao de um vetor para contar ocorrências de cada dígito (0-9)

    # loop que conta a frequência de cada dígito naquela casa decimal (unidade, dezena, etc.)
    for num in arr:
        index = (num // digito) % 10 # obtem o dígito atual do número
        count[index] += 1 # aumenta a contagem para aquele dígito

    # loop para acumular as posições, em quee count[i] contem a posicao final do digito i no output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Constroi o array de saída (de trás pra frente para garantir estabilidade)
    for i in range(n - 1, -1, -1):
        index = (arr[i] // digito) % 10 # Extrai o dígito da posição atual
        output[count[index] - 1] = arr[i] # Coloca o número na posição correta no output
        count[index] -= 1 # Decrementa a posição para o próximo igual

    # Copia o array ordenado de volta para o original
    for i in range(n):
        arr[i] = output[i]

# Função principal: Radix Sort
def radix_sort(arr):
    if len(arr) == 0: # Caso a lista esteja vazia
        return arr
    max_num = max(arr) # Encontra o maior número da lista
    digito = 1 # Começa pelas unidades (1 = 10^0)

    # Repete o counting sort para cada casa decimal (unidade, dezena, centena...)
    while max_num // digito > 0: # Enquanto houver dígitos a processar
        counting_sort_digito(arr, digito)
        digito *= 10 # Vai para a próxima casa decimal (10, 100, ...)

    return arr