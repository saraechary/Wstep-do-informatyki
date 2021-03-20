# Zadanie 4.
# Należy porównać szybkość działania funkcji pozwalających na wyznaczenie 𝑁 − 𝑡𝑒𝑗 liczby ciągu
# Fibonacciego. Należy zaimplementować 3 funkcje: iteracyjną, rekurencyjną i rekurencyjną z pamięcią
# w postaci słownika. Porównując szybkości należy zmieniać 𝑁 od 0 do 𝑀, gdzie 𝑀 jest pobierane z
# pliku.

import time
from colorama import init
init()

# ciąg Fibonacciego iteracyjnie
def fibo_iter(n): 
    tab = []
    x = 0
    y = 1
    while len(tab) < n + 1:
        tab.append(x)
        temp = y
        y = x + y
        x = temp
    return tab[n]

# ciąg Fibonacciego rekurencyjnie
def fibo_rekurencyjne(n):  #USELESS
    if n <= 1:
        return n
    else:
        return fibo_rekurencyjne(n - 1) + fibo_rekurencyjne(n - 2)

# ciąg Fibonacciego rekurencyjnie z pamięcią
def fibo_rekurencyjne_mem(n, memo):
    if n not in memo:
        memo[n] = fibo_rekurencyjne_mem(n - 1, memo) + fibo_rekurencyjne_mem(n - 2, memo)
    return memo[n]

def start():
    memo = {0: 0, 1: 1}
    f = open("Laboratorium 8/file.txt", 'r')        
    lines = f.readlines()       # Jak tablica

    for i in range (0, len(lines)):
        n = int(lines[i])

        print(f"Wykonuję interacyjnie...\nPodaję \u001b[32m{n}\u001b[0m element ciągu:")
        start_time = time.time()
        print(f"\u001b[32m{fibo_iter(n)}\u001b[0m")
        print(f"Czas wykonania: \u001b[36m{time.time() - start_time}\u001b[0m s\n")

        print(f"Wykonuję rekurencyjnie...\nPodaję \u001b[32m{n}\u001b[0m element ciągu:")
        start_time = time.time()
        print(f"\u001b[32m{fibo_rekurencyjne(n)}\u001b[0m")
        print(f"Czas wykonania: \u001b[36m{time.time() - start_time}\u001b[0m s\n")

        print(f"Wykonuję rekurencyjnie z pamięcią...\nPodaję \u001b[32m{n}\u001b[0m element ciągu:")
        start_time = time.time()
        print(f"\u001b[32m{fibo_rekurencyjne_mem(n, memo)}\u001b[0m")
        print(f"Czas wykonania: \u001b[36m{time.time() - start_time}\u001b[0m s\n")


start()