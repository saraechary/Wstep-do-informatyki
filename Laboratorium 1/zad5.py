
import sys
t = int(input("Wprowadź wybraną liczbę, aby sprawdzić czy jest iloczynem dwóch dowolnych wyrazów ciągu Fibonacciego : "))

zmienne = False 

c, d =0, 1
while (d < 100000):
    # print(str(d))
    temp = c+d
    c=d
    d=temp

    if (t == c*d) :
        zmienne = True
        break  

if (zmienne == True) :
     print ("tak" )
else:
     print ("nie jest")

    # for t in range (0, t):
    #     if t == d * (c+d):
    #         print("Ta liczba " + str(t) + " jest iloczynem dwóch dowolnych wyrazów ciągu Fibonacciego")

    #     else:
    #         print("Ta liczba " + str(t) + " nie jest iloczynem dwóch dowolnych wyrazów ciągu Fibonacciego")

