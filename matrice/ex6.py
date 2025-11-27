import random
from numpy import array
def saisir():
    global n
    n=int(input("Donner n\n"))
    while not(3<=n<=20):
        n=int(input("Donner n\n"))
def remplir(M,n):
    for l in range(n):
        for c in  range(n):
            M[l,c]=random.randint(10,99)

def afficher(M,n):
    maxl=array([[int()]*n]*n)
    maxc=array([[int()]*n]*n)

    for l in range(n):
        
        max1=maximuml(M,l,n)
        max2=maximumc(M,l,n)
        for c in range (n):
            if M[l,c] == max1:
                maxl[l,c] = 1
            else:
                maxl[l,c] = 0
            if M[c,l] == max2:
                maxc[c,l] = 1
            else :
                maxc[c,l] = 0
            print(M[l,c], end="|")
        print()
    for l in range(n):
        for c in range(n):
            if (maxl[l,c] == maxc[l,c]) and (maxl[l,c]==1):
                print(M[l,c])
            
                
            

def maximuml(M,l,n):
    max=M[l,0]
    for i in range(n):
        if M[l,i] > max:
            max=M[l,i]
    return max
def maximumc(M,c,n):
    max=M[0,c]
    for i in range (n):
        if M[i,c] > max:
            max=M[i,c]
    return max



saisir()
M=array([[int()]*n]*n)
remplir(M,n)
afficher(M,n)
