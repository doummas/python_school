from numpy import array
def saisir():
    global n
    n=int(input("Donner le taille de tableau\n"))
    while n>50 or n<5:
        n=int(input("Donner le taille de tableau autre fois\n"))

def remplir(T,n):
    for i in range(n):
        T[i] = input("Donner une chaine\n ")
        while not(verif(T[i])):
            T[i] = input("Donner une chaine valid\n ")
    print(T)

def verif(chaine):
    i=0
    while i<len(chaine):

        if "A"<=chaine[i]<="Z":
            i+=1
        else :
            i+=50

    return (i==len(chaine)) and (3<=len(chaine)<=7)  

def trie(T,n):
    for i in range(n):
        asc=cal(T[i])
        if asc :
            print(T[i])
def cal(ch):
    ta=len(ch)
    T1=array([int()]*ta)
    for i in range(ta):
        T1[i] = ord(ch[i])

    test=False
    while not(test):
        test=True
        for i in range(ta-1):
            if T1[i] > T1[i+1]:
                aux = T1[i+1]
                T1[i+1] = T1[i]
                T1[i] = aux
                test = False
    test2= True
    na = T1[1] - T1[0]
    f = 1
    while  f<ta and test2 :
        test2 = False
        if T1[f-1] - T1[f] == -(na):
            f+=1
            test2=True
    return f == ta


saisir()
T=array([str]*n)
remplir(T,n)
trie(T,n)
