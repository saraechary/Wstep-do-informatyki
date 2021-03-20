# Proszę napisać program, który umożliwia wykonywanie operacji na 2 dowolnych macierzach o wymiarach NxM: 
# dodawanie, odejmowanie, mnożenie przez siebie, mnożenie przez skalar. 
# Macierze należy pobrać z pliku i zapisać do osobnego pliku wszystkie wyniki działań w taki sposób, 
# żeby to było czytelne dla człowieka.
# Należy obsłużyć niezbędne wyjątki, np. niezgodność wymiarów.

import numpy as np
import random

# pobranie danych z pliku
with open("C:/Users/sarae/OneDrive/Pulpit/Python/Laboratorium 6/macierz1.txt", "r") as file:
    mtx1_read = [[int(num) for num in line.split(',')] for line in file if line.strip() != "" ]

with open("C:/Users/sarae/OneDrive/Pulpit/Python/Laboratorium 6/macierz2.txt", "r") as file:
    mtx2_read = [[int(num) for num in line.split(',')] for line in file if line.strip() != "" ]    

mtx1 = np.matrix(mtx1_read)
mtx2 = np.matrix(mtx2_read)
print(mtx1)
print("\n")
print(mtx2)



# część w której mogę wygenerować randomowe macierze przy wybieranych wartościach
# def gener_mtx(n, m):
#     tab = [[random.randint(1,9) for i in range (m)] for j in range (n)]  
#     return tab

# print("Matryca 1")
# n1 = int(input("Wymiar N: "))
# m1 = int(input("Wymiar M: "))
# print("Matryca 2")
# n2 = int(input("Wymiar N: "))
# m2 = int(input("Wymiar M: "))

# mtx1 = np.matrix(gener_mtx(n1,m1))
# mtx2 = np.matrix(gener_mtx(n2,m2))



# Przy dodawaniu i odejmowaniu muszą być te same wymiary
def dodawanie(mtx1, mtx2):
    try:
        mtx = mtx1 + mtx2
    except ValueError:
        return f"Macierze mają różne wymiary. Nie można ich dodać."
    return mtx

def odejmowanie(mtx1, mtx2):
    try:
        mtx = mtx1 - mtx2
    except ValueError:
        return f"Macierze mają różne wymiary. Nie można ich odjąć."
    return mtx


# Mnożenie przez skalar 
def mnozenie_przez_skalar(mtx, a):
    mtx = mtx*a
    return mtx


# Żeby mnożenie macierzy było możliwe to drugi wymiar musi być równy pierwszemu
# pierwsza macierz ma tyle samo kolumn, co druga wierszy 
def mnozenie(mtx1, mtx2):
    try:
        mtx = mtx1*mtx2
    except ValueError:
        return f"Drugi wymiar pierwszej macierzy jest różny od pierwszego wymiaru drugiej.\nNie można wykonać mnożenia"

    return mtx

# Rysowanie dodawania i odejmowania to te same funkcje tylko jedna jest z minusem
# Każda funkcja na rysowanie działa podobnie
# Drukują się też przypadki z dodawniem i mnożeniem tylko bez wyniku
# def draw_dodawanie(mtx1, mtx2, mtx):
#     draw = ''
#     le1 = len(mtx1)
#     le2 = len(mtx2)
    
#     if(le1 > le2): # która jest dłuższa
#         for i in range(0, le1):
#             if(le2//2 == i):
#                 try:
#                     draw += str(mtx1[i])[1:-1] + "\t+\t" + str(mtx2[i])[1:-1] + "\t=\t" + str(mtx[i])[1:-1] + "\n" #ucięcie klamr
#                 except IndexError:
#                     draw += ""
#             else:
#                 try:
#                     draw += str(mtx1[i])[1:-1] + "\t\t" + str(mtx2[i])[1:-1] + "\t\t" + str(mtx[i])[1:-1] + "\n"
#                 except IndexError:
#                     draw += str(mtx1[i])[1:-1] + "\t\t\t\t\t" + str(mtx[i])[1:-1] + "\n"
#     else: 
#         for i in range(0, le2):
#             if(le1//2 == i):
#                 try:
#                     draw += str(mtx1[i])[1:-1] + "\t+\t" + str(mtx2[i])[1:-1] + "\t=\t" + str(mtx[i])[1:-1] + "\n"
#                 except IndexError:
#                     draw += ""
#             else:
#                 try:
#                     draw += str(mtx1[i])[1:-1] + "\t\t" + str(mtx2[i])[1:-1] + "\t\t" + str(mtx[i])[1:-1] + "\n"
#                 except IndexError:
#                     draw += "\t\t\t\t\t" + str(mtx2[i])[1:-1] + "\t\t\n"
#     return draw

# def draw_odejmowanie(mtx1, mtx2, mtx):
#     draw = ''
#     le1 = len(mtx1)
#     le2 = len(mtx2)
#     if(le1 > le2):
#         for i in range(0, le1):
#             if(le2//2 == i):
#                 try:
#                     draw += str(mtx1[i])[1:-1] + "\t-\t" + str(mtx2[i])[1:-1] + "\t=\t" + str(mtx[i])[1:-1] + "\n"
#                 except IndexError:
#                     draw += ""
#             else:
#                 try:
#                     draw += str(mtx1[i])[1:-1] + "\t\t" + str(mtx2[i])[1:-1] + "\t\t" + str(mtx[i])[1:-1] + "\n"
#                 except IndexError:
#                     draw += str(mtx1[i])[1:-1] + "\t\t\t\t\t" + str(mtx[i])[1:-1] + "\n"
#     else: 
#         for i in range(0, le2):
#             if(le1//2 == i):
#                 try:
#                     draw += str(mtx1[i])[1:-1] + "\t-\t" + str(mtx2[i])[1:-1] + "\t=\t" + str(mtx[i])[1:-1] + "\n"
#                 except IndexError:
#                     draw += ""
#             else:
#                 try:
#                     draw += str(mtx1[i])[1:-1] + "\t\t" + str(mtx2[i])[1:-1] + "\t\t" + str(mtx[i])[1:-1] + "\n"
#                 except IndexError:
#                     draw += "\t\t\t\t\t" + str(mtx2[i])[1:-1] + "\t\t\n"
#     return draw

# def draw_mnozenie(mtx1, mtx2, mtx):
#     draw = ''
#     le1 = len(mtx1)
#     le2 = len(mtx2)
    
#     if(le1 > le2):
#         for i in range(0, le1):
#             if(le2//2 == i):
#                 try:
#                     draw += str(mtx1[i])[1:-1] + "\tx\t" + str(mtx2[i])[1:-1] + "\t=\t" + str(mtx[i])[1:-1] + "\n"
#                 except IndexError:
#                     draw += ""
#             else:
#                 try:
#                     draw += str(mtx1[i])[1:-1] + "\t\t" + str(mtx2[i])[1:-1] + "\t\t" + str(mtx[i])[1:-1] + "\n"
#                 except IndexError:
#                     draw += str(mtx1[i])[1:-1] + "\t\t\t\t\t\t\t" + str(mtx[i])[1:-1] + "\n"
#     else: 
#         for i in range(0, le2):
#             if(le1//2 == i):
#                 try:
#                     draw += str(mtx1[i])[1:-1] + "\tx\t" + str(mtx2[i])[1:-1] + "\t=\t" + str(mtx[i])[1:-1] + "\n"
#                 except IndexError:
#                     draw += ""
#             else:
#                 try:
#                     draw += str(mtx1[i])[1:-1] + "\t\t" + str(mtx2[i])[1:-1] + "\t\t" + str(mtx[i])[1:-1] + "\n"
#                 except IndexError:
#                     draw += "\t\t\t\t\t" + str(mtx2[i])[1:-1] + "\t\t\n"
#     return draw


# inny szybszy sposób na zapisanie 3 powyższych funkcji

def draw(mtx1, mtx2, mtx, opcja):
    draw = ''
    le1 = len(mtx1)
    le2 = len(mtx2)
    
    if(le1 > le2): # która jest dłuższa
        for i in range(0, le1):
            if(le2//2 == i):
                try:
                    draw += str(mtx1[i])[1:-1] + f"\t{opcja}\t" + str(mtx2[i])[1:-1] + "\t=\t" + str(mtx[i])[1:-1] + "\n" #ucięcie klamr
                except IndexError:
                    draw += ""
            else:
                try:
                    draw += str(mtx1[i])[1:-1] + "\t\t" + str(mtx2[i])[1:-1] + "\t\t" + str(mtx[i])[1:-1] + "\n"
                except IndexError:
                    draw += str(mtx1[i])[1:-1] + "\t\t\t\t\t" + str(mtx[i])[1:-1] + "\n"
    else: 
        for i in range(0, le2):
            if(le1//2 == i):
                try:
                    draw += str(mtx1[i])[1:-1] + f"\t{opcja}\t" + str(mtx2[i])[1:-1] + "\t=\t" + str(mtx[i])[1:-1] + "\n"
                except IndexError:
                    draw += ""
            else:
                try:
                    draw += str(mtx1[i])[1:-1] + "\t\t" + str(mtx2[i])[1:-1] + "\t\t" + str(mtx[i])[1:-1] + "\n"
                except IndexError:
                    draw += "\t\t\t\t\t" + str(mtx2[i])[1:-1] + "\t\t\n"
    return draw






while True:
    try:
        a = int(input("Wprowadź liczbę, jaką ma mieć twój skalar:\n"))
        a>0
        break
    except ValueError:
        print("Wprowadż liczbę całkowitą większą od zera.")

def draw_mnozenie_skalar(mtx1, mtx, a):
    draw = ''
    for i in range(0, len(mtx1)):
        if(len(mtx1)//2  == i):
            draw += str(mtx1[i])[1:-1] + "\tx" + str(a)+ "\t=\t" + str(mtx[i])[1:-1] + "\n" 
        else:
            draw += str(mtx1[i])[1:-1] + "\t\t\t" + str(mtx[i])[1:-1] + "\n" 
    return draw


mtx_dodawanie = dodawanie(mtx1, mtx2)
mtx_odejmowanie = odejmowanie(mtx1, mtx2)
mtx_mnozenie = mnozenie(mtx1, mtx2)
mtx_mnozenie_skalar1 = mnozenie_przez_skalar(mtx1, a)
mtx_mnozenie_skalar2 = mnozenie_przez_skalar(mtx2, a)

print("Dodawanie\n", mtx_dodawanie, "\n")
print("Odejmowanie\n", mtx_odejmowanie, "\n")
print("Mnożenie\n", mtx_mnozenie, "\n")
print("Mnożenie przez skalar pierwszej\n", mtx_mnozenie_skalar1, "\n")
print("Mnożenie przez skalar drugiej\n", mtx_mnozenie_skalar2, "\n")

# draw_dod = draw_dodawanie(mtx1, mtx2, mtx_dodawanie)
# draw_odej = draw_odejmowanie(mtx1, mtx2, mtx_odejmowanie)
# draw_mnoz = draw_mnozenie(mtx1, mtx2, mtx_mnozenie)
draw_dod = draw(mtx1, mtx2, mtx_dodawanie, "+")
draw_odej = draw(mtx1, mtx2, mtx_odejmowanie, "-")
draw_mnoz = draw(mtx1, mtx2, mtx_mnozenie, "x")
draw_skalar1 = draw_mnozenie_skalar(mtx1, mtx_mnozenie_skalar1, a)
draw_skalar2 = draw_mnozenie_skalar(mtx2, mtx_mnozenie_skalar2, a)

# # zapisywanie macierzy w pliku
f = open("Laboratorium 6\wyniki.txt", "w", encoding='utf-8') 
f.write(draw_dod + "\n")
f.write(draw_odej + "\n")
f.write(draw_mnoz + "\n")
f.write(draw_skalar1 + "\n")
f.write(draw_skalar2 + "\n")
f.close()