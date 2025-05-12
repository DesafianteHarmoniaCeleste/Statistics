## Nome: Pedro Gasparelo Leme - 14602421
## Nome: Gabriel Dezejácomo Maruschi - 14571525

# Codigo paara o curso de estatistica - Objetivo: analizar o tempo de processamento de diferentes algoritmos de ordenação dependendo do tamanho da entrada, sempre considerando um caso medio

## algoritmos a serem usados: BubbleSort/ SelectionSort -> BigO(n²) // MergeSort/QuickSort/HeapSort BigO(n Log[n]) // RadixSort BigO(nk). para n sendo o tamanho da entrada

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


