from numpy import array
def saisir():

    nb = int(input("Donner un Nombre\n"))
    while (len(str(nb))) != 5 :
        nb = int(input("Nb must be 5 caractere\n"))
    return str(nb)

def tab_trans(nb,T):
    for i in range(5):
        T[i] = nb[i]
def tri(nb,T):
    test = False
    new = ""
    while not(test):
        test = True 
        for i in range(4):
            if T[i+1] > T[i]:
                aux = T[i+1]
                T[i+1] = T[i]
                T[i] = aux
                test = False
    for i in range(5):
        new += T[i]
    print(new)

nb=saisir()
T=array([str]*5)
tab_trans(nb,T)
tri(nb,T)