def pgcd_euc(a,b):
    while b!=0:
        aux = a % b
        a=b
        b=aux
    return a
def pgcd_diff(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else :
            b=b-a
    return a 
def ppcm(a,b):
    if a<b:
        aux=a
        a=b
        b=aux
    i=1
    while (a*i) % b !=0:
        i=i+1
    return a*i

def prime(a):
    i=2
    while(i<=(a // 2) and (a%i!=0)):
        i=i+1
    return i>a//2 and a!=1
def facteur(a):
    i=2
    ch=""
    while a!=1:
        if a %i == 0:
            a=a // i
            ch=ch+str(i)+"*"
        else :
            i=i+1
    return ch[0:len(ch)-1]
print(facteur(120))