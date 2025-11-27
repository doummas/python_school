from numpy import array


def saisir():
    global l,c
    l=int(input("Donner L\n"))
    while (l%2!=0) and (4<l<20):
        l=int(input("Donner L aute fois\n"))
    c=int(input("Donner c\n"))
    while (c%2==0) and (3<c<19):
        c=int(input("Donner c autre fois\n"))
     
        
        

def remplir(M,l,c,):
    for i in range(l):
        for j in range(c):
            M[i,j]=input("Donner une lettre voyelle majuscule\n")
            while not(isvalid(M[i,j])):
                M[i,j]=input("Donner une lettre voyelle majuscule autre fois\n")

def isvalid(ch):
    voyelle = "AEYUIO"
    i=0
    yes=False
    while (i<len(voyelle)) and (not(yes)):
        if voyelle[i] == ch:
            yes=True 
        else:
            i+=1
    return yes

def afficher(M,l,c):
    p=0
    for i in range(l):
        for j in range(c):
            print(M[i,j], end="|")
            p+=poid(M[i,j])

        print()
    print(p)

def poid(ch):
    return ord(ch) - 64

saisir()
M=array([[str]*c]*l)


remplir(M,l,c)
afficher(M,l,c)
    


