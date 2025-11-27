import random
from numpy import array
def saisir():
    global n
    n=int(input("Donner n\n"))
def remplir(M,n):
    for l in range(n):
        for c in range(n):
            M[l,c]=random.randint(1,9)
def afficher(M,n):
    for c in range(n):
        for l in range(n):
            print(M[l,c],end="|")
        print()
def calculer_re_dia(M,n):
    s=0
    for i in range(n):
        s=s+M[i,abs(i-n+1)]
    return s
def inverse(M,n):
    for l in range(n):
        for c in range(l):
            aux=M[l,c]
            M[l,c]=M[c,l]
            M[c,l]=aux
    
            



saisir()
M=array([[int()]*n]*n)
remplir(M,n)
afficher(M,n)
print(calculer_re_dia(M,n))
inverse(M,n)