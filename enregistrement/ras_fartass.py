# t3 classe
from numpy import array
from math import *


def saisir ():
    n=int(input("Donner le nombre des points \n"))
    while n>30 or n<2:
       n=int(input("Donner le nombre des points autre fois \n")) 
    return n


def remplir(T,n):
    for i in range(n):
        T[i] = dict()
        T[i]["x"] = float(input(f"Donner x{i}\n"))
        T[i]["y"] = float(input(f"Donner y{i}\n"))

def nombre(T,n):
    for i in range(n):
        a=float(input(f"Donner a pour la point {i} "))
        b=float(input(f"Donner b pour la point {i} "))
        c=float(input(f"Donner c pour la point {i} "))
        p=0
        if a*T[i]["x"] + b*T[i]["y"] + c ==0:
            p=p+1
    print(f"Le nombre des point est {p}")





n=saisir()
point=dict(
    x=float,
    y=float
)
T=array([point]*n)
remplir(T,n)
nombre(T,n)