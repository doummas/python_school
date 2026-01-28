# t3 classe
from numpy import array


def saisir():
    n=int(input("Donner n\n"))
    while n<2 or n>20:
        n=int(input("Donner n autre fois \n"))
    return n


def remplirT(T,n):
    for i in range(n):
        T[i] = dict()
        T[i]["nom"]=input("Donner votre nom\n")
        while verifier(T[i]["nom"])==False:
            T[i]["nom"]=input("Donner votre nom autre fois\n")
        T[i]["prenom"]=input("Donner votre prenom\n")
        while verifier(T[i]["prenom"])==False:
            T[i]["prenom"]=input("Donner votre prenom autre fois\n")
        T[i]["id"] = int(input("Donner l'identiter\n"))
        while unique(T[i]["id"],i,T) == False :
            T[i]["id"] = int(input("Donner l'identiter autre fois\n"))
        T[i]["age"] = int(input("Donner l'age \n"))
        while T[i]["age"]>60 or T[i]["age"] <15:
            T[i]["age"] = int(input("Donner l'age autre fois \n"))
        T[i]["genre"] = (input("Donner genre\n")).upper()
        while T[i]["genre"] != "F" and T[i]["genre"] !="M":
            T[i]["genre"] = (input("M|F \n")).upper()
        T[i]["année_embauche"] = int(input("Donner année_embauche\n"))
        while not(1000<=T[i]["année_embauche"]<=9999):
            T[i]["année_embauche"] = int(input("Donner année_embauche autre fois\n"))
        

def remplirT1(T,T1,n):
    for i in range(n):
        T1[i]["matricule"] = T[i]["nom"][0] + T[i]["prenom"][0] + str(T[i]["id"]) + T[i]["genre"] + str(T[i]["année_embauche"])[2:]
        T1[i]["age"] = T[i]["age"]
        print(T[i])
        print(T1[i])

def unique(en,n,T):
    i=0
    while i<n and T[i]["id"] != en:
        i+=1
    return i == n and len(str(T[i]["id"])) == 8
        
def verifier(ch):
    ch=ch.upper()
    i=0
    while i<len(ch) and "A"<=ch[i]<="Z":
        i+=1
    return i == len(ch)


"""em=dict(
    nom=str,
    prenom=str,
    id=str,
    age=int,
    genre=str(),
    année_embauche = int
)"""

"""mat=dict(
    matricule = str,
    age = int
)"""
n=saisir()
T=array([dict]*n)
T1=array([dict]*n)
remplirT(T,n)
remplirT1(T,T1,n)