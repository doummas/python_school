from numpy import array
def saisir(name):
    n=int(input(f"Donner le taille de {name}\n"))
    while not(2<n<20):
        n=int(input(f"Donner le taille de {name} autre fois\n"))
    return n

def remplir(T,n):
    T[0]=int(input("Donner T[0]\n"))
    for i in range(1,n):
        T[i]=int(input(f"Donner T[{i}]\n"))
        while T[i]<T[i-1]:
            T[i]=int(input(f"Donner T[{i}]\n"))
    print(T)

def fusion(V1,V2,n,m):
    i=0
    j=0
    k=0
    V3=""
    while (i!=n) and (j!=m):
        if V1[i]<V2[j]:
            V3 += str(V1[i])
            i+=1
        elif V1[i] == V2[j]:
            V3 += str(V1[i])
            i+=1
            j+=1
        else :
            V3 += str(V2[j])
            j+=1
        k+=1
    if j==m:
        for c in range(i,n):
            V3 += str(V1[c])
            k+=1
    elif i==n:
        for c in range(j,m):
            V3 += str(V1[c])
            k+=1
    V3t=array([int()]*k)
    for i in range(k):
        V3t[i]=V3[i]
        print(V3t[i], end='|')



n=saisir("V1")
m=saisir("V2")
V1=array([int()]*n)
V2=array([int()]*m)
remplir(V1,n)
remplir(V2,m)
fusion(V1,V2,n,m)