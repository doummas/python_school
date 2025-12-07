from numpy import array
def saisir_kelma():
    mot = input("Donner une mot maj\n")
    while not(verif(mot)) and (double(mot)) and (mot.find("W") == -1) and (2<len(mot)<11):
        mot = input("3ewd a3ti el mo\n")
    return mot

def verif(ch):
    i=0
    while i<len(ch):
        if "A"<=ch[i]<="Z":
            i+=1
        else :
            i +=50
        return i == len(ch)
def double(ch):
    ch1=""
    ch=str(ch)
    double = True
    for i in range(len(ch)-1,-1,-1):
        ch1+=ch[i]
    ch1=str(ch1)
    for i in range(len(ch)):
        c = ch[i]
        if len(ch) - (ch.find(ch1[i])) == ch1.find(c):
            double = False
    return double



def remplir(M,l,c,mot):
    mot=str(mot)
    alpha="ABCDEFGIJKLMNOPQRSTUVXYZ"
    for i in range(len(alpha)):
        if mot.find(alpha[i]) != -1:
            alpha=alpha[:i]+alpha[i+1:]
        elif mot.find():
            pass
        
    
    alpha=alpha[:len(alpha)]
    a=0
    T=array([str()]*25)
    T2=array([str()]*(25-len(mot)))
    for i in range(25):
        if i == len(mot)-1:
            T[i]=alpha[a]
            a+=1
        else:
            T[i]=mot[i]

    for i in range(l):
        for j in range(c):
            M[i,j]=T[i]
        

def crypter(M,l,c):
    message=input("Donner le message vous dever cry\n")
    f=0
    while not(verif):
        message=input("Donner le message vous dever cryp autre fois\n")
    print(tashfir(message,M))


def tashfir(msg,M):
    v=""
    Mc=array([[int()]*l]*c)
    for i in range(l):
        for j in range(c):
            Mc[i,j] = str(i) +str(j)
            if M[i,j] == "V":
                v= str(i) +str(j)
    a=0
    final=""
    while msg[a]<len(msg)-1:
        for i in range(l):
            for j in range(c):
                if msg[a] == M[i,j]:
                    final+=Mc[i,j]
                    a+=1
                elif msg[a] == "W":
                    final+=v
    return final




            



mot=saisir_kelma()
l=5
c=5
M=array([[str()]*5]*5)
remplir(M,l,c,mot)
crypter(M,l,c)
