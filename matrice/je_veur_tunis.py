from numpy import array

def saisir():
    global nc,nl,text
    nl=3
    text=input("Donner un text pour le crypter\n")

    while len(text) % 3 != 0:
        text = text + " "
    nc=len(text) // 3

def remplir(M,nc,nl,text):
    i=0
    for l in range(nc):
        for c in range(nl):
            M[l,c]=text[i]
            i+=1

        

def afficher(M,nc,nl):
    text=""
    for l in range(nc):
        for c in range(nl):
            print(M[l,c], end="|")

        print()

    for c in range(nl):
        for l in range(nc):
            text=text + M[l,c]
    print(text)

saisir()
M=array([[str()]*nl]*nc)
remplir(M,nc,nl,text)
afficher(M,nc,nl)