from numpy import *

def saisir():
	global n
	n=int(input("Donner le nombre de colones et lignes\n"))
	while n>100 or n<0:
		n=int(input("Donner un nombre valide\n"))
def remplir(n,M):
	for i in range(n):
		for j in range(n):
			M[i,j]=int(input("Donner un nombre\n"))
			while M[i,j] <0:
				M[i,j]=int(input("Donner un nombre positif\n"))
def transfer(M,n,T):
	global K
	K=0
	for i in range (n):
		for j in range(n):
			if premier(M[i,j]):
				T[K]=M[i,j]
				K+=1
def premier(a):
	i=2
	while (i<=a//2) and (a%i != 0):
		i+=1
	return (i > a // 2) and (a!= 1)
	
def affichage(M,n,T,K):
	print("Voici la matrice")
	for i in range(n) :
		for j in  range(n):
			print(M[i,j], end="|")
		print()
		
	print("Voici le tableau")
	for l in range(K):
		print(T[l],end="|")
		
saisir()
M=array([[int()]*n]*n)
remplir(n,M)
T=array([int()]*(n*n))
transfer(M,n,T)
affichage(M,n,T,K)
