import sys
# n = int(input("Podaj liczbę") )

# def fib(n) :
#     a = 0
#     b = 1
#     print(1. , a)
#     print(2. , b)
#     for i in range (1, n-1):
#         a , b = b, a + b
#         print (i+2, b)
#     print(str(b))
#     return b

m = 1000000
a, b =0, 1
while b< m:
    print(str(b))
    a, b =b, a+ b