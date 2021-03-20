# Liczby zespolone są reprezentowane przez krotkę (ℜ, ℑ). 
# Gdzie: ℜ - część rzeczywista liczby, ℑ - część urojona liczby. 
# Proszę napisać funkcje realizujące podstawowe operacje na liczbach zespolonych, 
# m.in. dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie, wypisywanie i wczytywanie.
# Używając tych funkcji proszę napisać funkcję rozwiązującą równanie kwadratowe o współczynnikach zespolonych.

import math
import cmath

def dodawanie(z1, z2):
    z = z1 + z2
    print(draw_answer(z1, z2, z, '+'))
    return z

def odejmowanie(z1, z2):
    z = z1 - z2
    print(draw_answer(z1, z2, z, '-'))
    return z
    
def mnozenie(z1, z2):
    z = z1*z2
    print(draw_answer(z1, z2, z, '*'))
    return z

def dzielenie(z1, z2):
    z = z1/z2
    print(draw_answer(z1, z2, z, "/"))
    return z

def potega(root, power):
    z = root**power
    print(f"{root}^{power} = {z}")
    return z


def draw_answer(z1, z2, z, option):
    draw = ''
    draw += ''.join(f"{z1}{option}{z2} = {z}")
    return draw

# Tutaj jest główną funkcję z interfejsem i wpisywaniem liczb przez użytkownika.
# na dole wywołują się wszystkie funkcje. 

def rownanie_kwadratowe():
    print("‖――――――――――――――――――――――――‖")
    print("‖Podaj parametry równania‖")
    print("‖      kwadratowego:     ‖")
    print("‖――――――――――――――――――――――――‖")

    while True:             # Jak tutaj użytkownik coś źle wpisał to wywalalo na sam początek to jednak jest walidacja
        try:
            ar, ai = input(">a: ").split()
            br, bi = input(">b: ").split()
            cr, ci = input(">c: ").split()
        except ValueError:
            print("Podaj liczby poprawnie!")
        else:
            a = float(ar) + float(ai)*1j
            b = float(br) + float(bi)*1j
            c = float(cr) + float(ci)*1j
            break
    print(f"a: {a}, b: {b}, c: {c}")

    delta = b**2 - 4*a*c
    print(delta)
    
    if a == 0:  # liniowa
        x = -c/b
        print(f"F. Liniowa z x = {x}")
    elif b == 0:
        x1 = cmath.sqrt(-1*c/a)
        x2 = -1*(cmath.sqrt(-1*c/a))
        print("Dwa rozwiązania:")
        print(f"x1: {x1}\nx2: {x2}")
    else:
        if delta != 0:
            x1 = (-1*b + cmath.sqrt(delta))/(2*a)
            x2 = (-1*b - cmath.sqrt(delta))/(2*a)
            print("Rozwiązania:")
            print(f"x1: {x1}\nx2: {x2}")
        else:
            x = (-1*b /(2*a))
            print("Rozwiązanie:")
            print(f"x: {x}")

def podstawowe_operacje():
    print("‖――――――――――――――――――――――――‖")
    print("‖                        ‖")
    print("‖ Wpisz liczby zespolone ‖")
    print("‖   w podanej postaci:   ‖")
    print("‖                        ‖")
    print("‖          ℜ ℑ           ‖")
    print("‖ ℜ - część rzeczywista  ‖")                                             
    print("‖   ℑ - część urojona    ‖")                                             
    print("‖                        ‖")
    print("‖――――――――――――――――――――――――‖")

    re1, im1 = input("z1: ").split()                
    re2, im2 = input("z2: ").split()                
    z1 = float(re1) + float(im1)*1j                 
    z2 = float(re2) + float(im2)*1j  

    print("‖――――――――――――――――――――――――‖")
    print("‖                        ‖")
    print("‖   Którą liczbę chcesz  ‖")
    print("‖   podnieść do potęgi?  ‖")
    print("‖                        ‖")
    print("‖        wpisz:          ‖")
    print("‖         z1             ‖")
    print("‖         z2             ‖")
    print("‖                        ‖")
    print("‖――――――――――――――――――――――――‖")
    
    power_root = str(input("z1 lub z2: "))          # Użytkownik wybiera, którą liczbę chce podnieść do potęgi
    while power_root not in ['z1', 'z2']:           
        power_root = str(input("Wpisz poprawną liczbę! [z1 lub z2]: "))

    if(power_root == 'z1'):
        power_root = z1
    elif(power_root == 'z2'):
        power_root = z2

    print("‖――――――――――――――――――――――――‖")
    print("‖   Do której potęgi?    ‖")
    print("‖――――――――――――――――――――――――‖")

    power_ = int(input(f"{power_root}^"))

    dodawanie(z1, z2)
    odejmowanie(z1, z2)
    mnozenie(z1, z2)
    dzielenie(z1, z2)
    potega(power_root, power_)

def start():
    print("‖――――――――――――――――――――――――‖")
    print("‖ Którą operację chcesz  ‖")
    print("‖        wykonać?        ‖")
    print("‖                        ‖")
    print("‖1 - podstawowe operacje ‖")
    print("‖2 - równanie kwadratowe ‖")
    print("‖――――――――――――――――――――――――‖")

    option = int(input("> "))

    while option not in [1, 2]:
        option = int(input("Podaj poprawną opcję: "))
    if option == 1:
        podstawowe_operacje()
    else:
        rownanie_kwadratowe()

# START
start()