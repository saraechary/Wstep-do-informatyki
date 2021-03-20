# x*x - 2 = 0 
a = 2
b = 1
epsilon = 0.0000001

while ((a-b)>=epsilon):
    c = (a+b)/2
    if (c*c-2>0) :
        a = c
    elif (c*c -2 < 0) :
        b = c
print (c)        
