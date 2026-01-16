from numpy import array
eleve=dict(
    nom = str,
    prenom = str,
    math = float,
    phy = float,
    info = float,
    m = float

)
def saisir ():
    return 2




def remplir(T,n):
    for i in range(n):
        T[i] = {}
        T[i]["nom"]=input("nom\n")
        while not(valide(T[i]["nom"])) or len(T[i]["nom"]) >15:
            T[i]["nom"]=input("nom\n")
            print(T[i]["nom"])
        T[i]["prenom"]=input("prenom\n")
        while not(valide(T[i]["prenom"])) or len(T[i]["prenom"]) >20 :
            T[i]["prenom"]=input("prenom\n")
        T[i]["math"]=float(input("note math\n"))
        while 0>T[i]["math"] or T[i]["math"]>20:
            T[i]["math"]=float(input("note math\n"))
        T[i]["phy"]=float(input("note phy\n"))
        while 0>T[i]["phy"] or T[i]["phy"]>20:
            T[i]["phy"]=float(input("note phy\n"))
        T[i]["info"]=float(input("note info\n"))
        while 0>T[i]["info"] or T[i]["info"]>20:
            T[i]["info"]=float(input("note info\n"))

def valide(ch):
    i=0
    ch = ch.upper()
    while  i<len(ch) and "Z">=ch[i]>="A":
        i = i+1
    return i==len(ch)

def afficher1(T,n):
    for i in range(n):
        print(f"{T[i]["nom"]} {T[i]["prenom"]}" )

def afficher2(T,n):
    ch=input("yes")
    for i in range(n):
        ch1=T[i]["nom"]+" "+T[i]["prenom"]
        if ch==ch1 :
            print(f"{T[i]["math"]} {T[i]["phy"]} {T[i]["info"]}" )
def moy(T,n):
    for i in range(n):
        T[i]["m"]= ((T[i]["math"]+T[i]["info"]+T[i]["phy"])/3)
        print("eleve",str(i+1),(T[i]["math"]+T[i]["info"]+T[i]["phy"])/3)

def tri(T,n):
    ech=True
    while(ech):
        ech=False
        for i in range(n-1):
            if T[i]["m"]>T[i+1]["m"]:
                aux = T[i]
                T[i] = T[i+1]
                T[i+1] = aux 
                ech = True

def supprimer(T,n):
    nb=0
    tri(T,n)
    for i in range(n-1):
        if T[i]["m"]<10 and T[i+1]["m"]>10:
            nb=n-i
    TT=array([eleve]*nb)
    for i in range(nb):
        TT[i] =T[i+n-nb]







n=saisir() 
T=array([eleve]*n)       
remplir(T,n)
print(T)
shut = True
while shut:
    c = int(input("donner choix\n"))
    while (c>5 or c<0):
        c = int(input("donner choix\n"))
    if c==1:
        afficher1(T,n)
    elif c==2:
        afficher2(T,n)
    elif c==3:
        moy(T,n)
    elif c == 4 :
        tri(T,n)
    elif c == 5:
        supprimer(T,n)
    elif c == 0 :
        shut = False

