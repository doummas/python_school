from random import randint
from numpy import array


def saisir():
    global n
    n=int(input("Donner n\n"))
    while n<4 and n>20:
        n=int(input("Donner n autre fois\n"))

def remplir(M,n):
    for l in range(n):
        for c in range(n):
            M[l,c] = randint(10,99)


def afficher(M,n):
    Ml=array([[int()]*n]*n)
    Mc=array([[int()]*n]*n)
    for l in range(n):
        maxl=maximuml(M,n,l)
        maxc=maximumc(M,n,l)
        for c in range(n):
            if M[l,c] == maxl:
                Ml[l,c] = 1
            else:
                Ml[l,c] = 0
            if M[c,l] == maxc:
                Mc[c,l] = 1
            else:
                Mc[c,l]
            print(M[l,c],end='|')
        print()
    for l in range(n):
        for c in range(n):
            if (Ml[l,c] == Mc[l,c]) and (Mc[l,c] == 1):
                print(M[l,c])


def maximuml(M,n,l):
    max=M[l,0]
    for c in range(n):
        if M[l,c] > max:
            max = M[l,c]
    return max
def maximumc(M,n,l):
    max = M[0,l]
    for  c in range(n):
        if M[c,l] > max:
            max = M[c,l]
    return max


saisir()
M=array([[int()]*n]*n)
remplir(M,n)
afficher(M,n)
