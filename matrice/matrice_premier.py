from numpy import *
def saisir():
	global n
	n=int(input("Donner le nombre de colones et lignes\n"))
	while (n>100 or n<0):
		n=int(input("Donner un nombre valide\n"))
def remplir(n,M):
	for i in range(n):
		for j in range(n):
			M[i,j]=int(input("Donner un nombre\n"))
			while M[i,j] <0:
				M[i,j]=int(input("Donner un nombre positif\n"))
def afficher(T,M,n,t,U):
	for i in range(t):
		while U!="":
			
			T[i]=U[int(U) % 2 == 0]
			U=U[1:]
			print(T[i])


def filterr(M,n):
	global t, U
	U=""
	nb=M[i,j]-1
	t=0
	for i in range(n):
		for j in range(n):
			while nb !=1:
				if M[i,j] % nb != 0  and nb != 1 :
					U+=str(M[i][j])+" "
					t+=1
					nb=M[i,j]-1
					
					
					 
	
			


saisir()
M=array([[int()]*n]*n)
remplir(n,M)
T=array([int()]*n)
afficher(T)

