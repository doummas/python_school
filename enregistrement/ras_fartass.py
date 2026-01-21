from numpy import array

def saisir():
    global n
    n=int(input("Donner le taille \n "))
    while n>40 or n<8:
        n=int(input("Donner le taille \n "))


def remplir(T,n):
    for i in range(n):
        T[i]["nom"] = input("Donner le nom d'eleve\n")
        while valide(T[i],["nom"] == False):
            T[i]["nom"] = input("Donner le nom d'eleve autre fois\n ")
        T[i]["prenom"] = input("Donner le prenom\n")
        while valide(T[i],["prenom"] == False):
            T[i]["prenom"] = input("Donner le prenom d'eleve autre fois\n ")
        T[i]["moyenne"] = float(input("Donner le moyenne\n"))
        while T[i]["moyenne"] >20 or T[i]["moyenne"]<0:
            T[i]["moyenne"] = float(input("Donner le moyenne autre fois\n"))
def valide(ch):
    ch=ch.upper()
    i=0
    while i<len(ch) and "A"<=ch[i]<="Z":
        i=i+1
    return i==len(ch) 


eleve=dict(
    nom = str,
    prenom = str,
    moyenne = float,
    rang = int

)

T=array([eleve]*n)