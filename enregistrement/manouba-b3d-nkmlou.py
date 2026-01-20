from numpy import array

def saisir():
    global n
    n=int(input("Donnner n\n"))
    while n>200 or n<2:
        n=int(input("Donnner n autre fois\n"))


def remplir(T,n):
    for i in range(n):
        remplir2(T,i)

def remplir2(T,i):
    T[i] = {}
    section = "IMXTEL"
    T[i]["cin"] = (input("Donner votre cin\n"))
    while (vcin(T[i]["cin"],i,T) == False) or (len((T[i]["cin"])) != 8):
        print(vcin(T[i]["cin"],i,T))
        T[i]["cin"] = (input("Donner votre cin autre fois\n"))
    T[i]["nom"] = input("Donner votre nom\n")
    while valide(T[i]["nom"]) == False or len(T[i]["nom"])==0 :
        T[i]["nom"] = (input("Donner votre nom autre fois\n"))
    T[i]["prenom"] = input("Donner votre prenom\n")
    while valide(T[i]["prenom"]) == False or len(T[i]["prenom"])==0:
        T[i]["prenom"] = (input("Donner votre prenom autre fois\n"))
    T[i]["sexe"] = (input("Donner votre sexe\n")).upper()
        
    while T[i]["sexe"] != "M" and T[i]["sexe"] != "F":
        T[i]["sexe"] = (input("F ou M\n")).upper()
    year = int(input("Donner l'anne de naissance\n"))
    while year >2020 or year<1990:
        year = int(input("Donner l'anne de naissance autre fois\n"))
    mois = int(input("Donner le mois de naissance\n"))
    while mois>12 or mois<0:
        mois = int(input("Donner le mois de naissance autre fois\n"))
    jour = int(input("Donnner le jour de naissance\n"))
    while jour>31 or jour<0:
        jour = int(input("Donnner le jour de naissance autre fois\n"))
    if len(str(mois)) == 1:
        mois = "0" + str(mois)
    if len(str(jour)) == 1:
        jour = "0" + str(jour)
    T[i]["naissance"] = str(jour)+ "/" + str(mois) + "/" + str(year)
    T[i]["section"] = (input("Donner votre section \n")).upper()
    while section.find(T[i]["section"]) == -1:
        T[i]["section"] = input("Donner votre section autre fois \n")
    print(T[i])
            

def valide(ch):
    ch=ch.upper()
    i=0
    while i<len(ch) and "A"<=ch[i]<="Z":
        i=i+1
    return i==len(ch) 

def vcin(en,n,T):
    i=0
    while i<n and  T[i]["cin"] != en:
        i = i+1
    return i == n
def operation(T,n):
    t=True
    while t:
        choix=int(input("choisir une operation\n"))
        if choix== 1:
            verifier(T,n)
        elif choix == 2:
            ajouter(T,n)
        elif choix == 3:
            supprimer(T,n)
        elif choix ==4:
            for i in range(n):
                print(T[i])
        elif choix == 5:
            pourcentage(T,n)
        else :
            t = False

def pourcentage(T,n):
    m=0
    for i in range(n):
        if T[i]["sexe"] == "M":
            m = m + 1
    print(f"garcon pourcentage {(m*100)/n} % et fille pourcentage {100 - ((m*100)/n) } % ")
    

def supprimer(T,n):
    ele=input("Donner le cin d'eleve pour le supprimer\n")
    ind = icin(T,n,ele)
    aux = T[n-1]
    T[n-1] = T[ind]
    T[ind] = aux
    n = n-1
    for i in range(n): 
        print(T[i])


def icin(T,n,ele):
    i=0
    while i<n and  T[i]["cin"] != ele:
        i = i+1
    return i 

def ajouter(T,n):
    nn=n+1
    TT=array([eleve]*nn)
    for i in range(n):
        TT[i] = {}
        TT[i] = T[i]
    remplir2(TT,n)
    

    print(TT[n])
    
def verifier(T,n):
    en = input("Donner le cin d'eleve \n")
    i=0
    while (i<n) and  (T[i]["cin"] != en):
        i = i+1
    
    if i == n:
        print("Cette eleve n'existe pas")
    else :
        print(T[i])
    
eleve=dict(
    cin = str,
    nom = str,
    prenom = str,
    sexe = str(),
    naissance = str,
    section = str()

)
saisir()
T=array([eleve]*n)
remplir(T,n)
operation(T,n)


