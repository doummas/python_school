from numpy import array
from random import randint

def saisir():
    n = int(input("Donnner n\n"))
    while n<2 or n>20:
        n = int(input("Donnner n\n"))
    return n


def remplirM(M,n):
    for i in range(n):
        for j in range(n):
            M[i][j]=randint(0,9)
    print(M)


def remplirT(T,M,n):

    for i in range(n):
        ch=""
        T[i] = dict()
        T[i]["lig"] = str(M[i,0])
        for j in range(n-1):
            ch=ch+str(M[i,j+1])
        T[i]['lig'] = ch
        T[i]["test"] = t=test(ch)
    for i in range(n):
        print(T[i])

def test(ch):
    return tri_croi(ch) or tri_dcroi(ch)

def tri_croi(ch):
    i=0
    while (i<len(ch)-1) and (ch[i]<ch[i+1]):
        i=i+1
    return i==len(ch)-1
def tri_dcroi(ch):
    i=0
    while (i<len(ch)-1) and (ch[i]>ch[i+1]):
        i=i+1
    return i==len(ch)-1

n=saisir()
M=array([[int]*n]*n)
remplirM(M,n)
"""ch=dict(
    lig=str,
    test=bool
)"""
T=array([dict]*n)
remplirT(T,M,n)
