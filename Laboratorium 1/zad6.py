
import sys

a = int(input("Wprowadź wybraną liczbę, aby sprawdzić czy jest to liczba pierwsza : "))

def czy_pierwsza(s):
    if s == 2 :
        return str(s) + " jest to liczba pierwsza"
        
    if s % 2 == 0 or s <= 1:
        return  str(s) + " nie jest to liczba pierwsza"

    # pierw = int(s**0.5) + 1
    for dzielnik in range(3, 10000):
        if (s % dzielnik == 0):
            return str(s) + " nie jest to liczba pierwsza"
        else:
             return str(s) + " jest to liczba pierwsza"
    
print (czy_pierwsza(a))


# if True:
#     print("Jest to liczba pierwsza")

# if False :
#     print("To nie jest liczba pierwsza")
