from numpy import array
def saisir():
    n=int(input("Donnner n\n"))
    while n>200 or n<1:
        n=int(input("Donnner n autre fois\n"))
    return n


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
            n=n+1
            ajouter(T,n-1)
            print(n)
        elif choix == 3:
            supprimer(T,n)
            n=n-1
        elif choix ==4:
            for i in range(n):
                print(T[i])
            print(n)
        elif choix == 5:
            pourcentagemf(T,n)
        elif choix == 0 :
            t = False
        else :
            print("" \
            "1/verifier par le cin\n" \
            "2/ajouter un eleve\n" \
            "3/supprimer un eleve\n" \
            "4/voir tous les eleve\n" \
            "5/pourcentage des genres\n")

def pourcentagemf(T,n):
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


def icin(T,n,ele):
    i=0
    while i<n and  T[i]["cin"] != ele:
        i = i+1
    return i 

def ajouter(T,n):
    remplir2(T,n)
    print(n)

    
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
n=saisir()
T=array([eleve]*200)
remplir(T,n)
operation(T,n)


