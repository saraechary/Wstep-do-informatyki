# Proszę napisać program wczytujący tablicę dwuwymiarową o ustalonym wymiarze 𝑛 𝑥 𝑛 wypełnioną liczbami naturalnymi. 
# Dla danej tablicy należy napisać funkcję, która zwraca wiersz i kolumnę dowolnego elementu, 
# dla którego iloraz sumy elementów w kolumnie w którym leży element do sumy elementów wiersza w którym leży element jest największa.
# Wymiar tablicy powinien być definiowany przez użytkownika.

import random

# część kodu gdzie definiowana jest wartość wpisywana przez użytkownika, służaca do stworzenia tabeli n x n
while True:
    try:
        n = int(input("Wprowadź liczbę, jaką chcesz aby miał wymiar twojej tablicy:\n"))
        n>0
        break
    except ValueError:
        print("Wprowadż liczbę całkowitą większą od zera.")

# generuje tablice o wymiarach n x n wypełnioną "0" a następnie uzupełniam ją losowymi liczbami 
def generujtab(n):
    tablica = [[0 for x in range(n)] for y in range(n)]
    for i in range (0, n): #0 indeks
        for j in range (0, n):
            tablica[i][j] = random.randint(1,9)
    print(draw_tab(tablica))        
    return tablica    

# efekt głownie estetyczny, ładne wypisanie wartości tabelki
def draw_tab(tab):
    draw = ''    
    for i in range (0, len(tab)):
        for j in range (0, len(tab[i])):
            if(j == len(tab[i]) - 1):
                draw += ''.join(str(tab[i][j]))
                draw += ''.join("\n")
            else:
                draw += ''.join(str(tab[i][j]))
                draw += ''.join(" | ")
    return draw

# policzenie sumy elementów w kolejnych wierszach
def sumawiersz(tablica):
    sumatab = []
    suma = 0
    for i in range (0, len(tablica)):
        for j in range (0, len(tablica)):
            suma += tablica[i][j]
        sumatab.append(suma)
        suma = 0     
    
    return sumatab

# policzenie sumy elementów w kolejnych kolumnach
def sumakolumn(tablica):
    sumatab = []
    suma = 0
    for j in range (0, len(tablica)):
        for i in range (0, len(tablica)):
            suma += tablica[i][j]
        sumatab.append(suma)
        suma = 0     
    
    return sumatab

# "głowna" funkcja programu, liczy ilorazy sumy kolumn i sumy wierszy
def iloraz(tablica):
    sumakol = sumakolumn(tablica)
    sumawier = sumawiersz(tablica)
    najwieksza = 0 
    ilotab = []
    kol  = 0
    wier = 0
    for i in range (0, len(sumakol)):
        for j in range (0, len(sumawier)):
            ilo = round(sumakol[i]/sumawier[j], 3)
            ilotab.append(ilo)  
            print(f"{ilo} = {sumakol[i]} / {sumawier[j]}")    #służy głównie do weryfikacji, widzę iterujące się pętle
            if (ilo > najwieksza):
                najwieksza = ilo
                kol = i
                wier = j
    
    return f'Największy iloraz sumy kolumny {kol} i sumy wiersza {wier} wynosi {najwieksza}.\n{ilotab}'
    


tablica = generujtab(n)
# print(draw_tab(generujtab(n)))        
print(sumakolumn(tablica))
print(sumawiersz(tablica))
print(iloraz(tablica))        

