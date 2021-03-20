
import sys

n = int(input("Wprowadź liczbę, której pierwiastek chcesz otrzymać ze wzoru Newtona : ") )

def absolute(absol) :
    if absol < 0:
        return -absol
    else:
        return absol

x = n / 2
epsilon = 0.000001
i = 0

while (absolute (x - (n / x))> epsilon ):
    x = (x + (n / x)) / 2
    i = i+1

print("Pierwiastkiem z liczby " + str(n) +" jest liczba " + str(x))