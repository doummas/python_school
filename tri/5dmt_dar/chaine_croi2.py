from numpy import array
def saisir():

    nb = int(input("Donner un Nombre\n"))
    while (len(str(nb))) != 5 :
        nb = int(input("Nb must be 5 caractere\n"))
    return str(nb)


def tri(nb):
    test = False
    new =""
    while not(test):
        test = True
        max = nb[0]
        for i in range(len(nb)):
            if nb[i] > max:
                max = nb[i]
                nb = nb[0:i]+nb[i+1:len(nb)]
                new = new + max
                test = False

    print(new)
    




nb=saisir()
tri(nb)