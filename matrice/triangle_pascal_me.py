from numpy import array

def saisir():
    global n
    n = int(input("Donner N\n"))
    while n>20:
        n = int(input("Donner N autre fois"))
def remplir(M,n):
    
    for i in range(n):
        M[i,0]=1
        for j in range(i,n):
            M[i,i]=1
            M[i,j]=0
    M[0,0]=1
    M[n-1,n-1]=1
    for i in range(2,n):
        for j in range(1,i):
            M[i,j]=M[i-1,j]+M[i-1,j-1]
            
            
def afficher(M,n):
    for i in range(n):
        for j in range(i):
            print(M[i,j],end='|')
        print()

saisir()
M=array([[int]*n]*n)
remplir(M,n)
afficher(M,n)
            
            
        
