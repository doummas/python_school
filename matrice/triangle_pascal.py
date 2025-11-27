from numpy import array
def saisir():
    global n 
    n=int(input("Donner n=>"))
def remplir(M,n):
    for i in range(n):
        for j in range(i):
            if (j == 0) or (i == j):
                M[i,j]=1
            else:
                M[i,j]=M[i-1,j-1]+M[i-1,j]


def afficher(M,n):
    for l in range(n):
        for c in range(l):
            print(M[l,c],end="|")
        print()


saisir()
M=array([[int()]*n]*n)
remplir(M,n)
afficher(M,n)