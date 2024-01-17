import math
import random

print(random.randint(1,99))
x = int(input())
y = int(input())
def adunare():
    print(x + y)
def scadere():
    if(x > y):
        print(x - y)
    else:
        print(y - x)       
def inmultire():
    print(x * y)
def inpartire():
    print(x / y)
def modulo():
    print(x % y)
def ridicarelaputere():
    print(math.pow(x,y))
def factorial():
    print(math.factorial(x))        
adunare()
scadere()
inmultire()
inpartire()
modulo()
ridicarelaputere()
factorial()