from numpy import array
import random
def saisir():
    global n,mot
    n=int(input("Donner n=>"))
    mot=input("Donner un mot\n")
    while verif(mot)==False:
        mot=input("reDonner un mot\n")
    while not(2<n<16):
        n=int(input("Donner valid n=>"))

def verif(mot):
    i=0
    mot=mot.upper()
    while (i<=len(mot)) and ("A"<mot[i]<"Z"):
        i+=1
    return i == len(mot)
def remplir(M,n):
    for l in  range(n):
        for c in range(n):
            M[l,c]=chr(random.randint(65,90))
def chercher(M,n,mot):
    com=""
    tom=""
    i=0
    for l in range(n):
        for c in  range(n):
            com=com+M[l,c]
        while i<len(mot) and com[i].find!=-1 :
            i+=i
    return i == len(mot)



            
saisir()
M=array([[str()]*n]*n)
remplir(M,n)
chercher(M,n)
if chercher(M,n) == True:
    print("Le mot est dans la chaine=>")
else:
    print("Le mot n'exite pas")