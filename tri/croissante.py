from numpy import array
from random import randint
def saisir():
    global n
    n=int(input("donner n\n"))
def remplir(T,n):
    for i in range(n):
        T[i] = randint(1,99)
def afficher(T,n):
    for i in range(n):
        print(T[i], end="|")
    print()
    aux=0
    change=False
    while not change :
        change = True
        for i in range(n-1):
            if T[i] > T[i+1]:
                '''aux = T[i+1]
                T[i+1] = T[i]
                T[i] = aux '''
                T[i+1], T[i] = T[i], T[i+1]
                change = False
        n = n-1
    print(T)

        
saisir()
T=array([int()]*n)
remplir(T,n)
afficher(T,n)