#INTEGRANTES: Morales Perez Mariela & Mendoza Trejo Jairo
#NUMEROS PRIMOS
def genprim(M):
	j=1
	i=1
	c=0
	while i<(M+1):
		while j<(M+1):
			if i%j==0:
				c=c+1
			j=j+1
		if c == 2:
			yield i
		c=0
		i=i+1
		j=1
a=[z for z in genprim(20)]
print("N U M E R O S	P R I M O S: ")
print(a)
print(" ")

#BADA BOOM!
def genBadaBoom(N):
	i=1
	while i<N:
		if i%3 ==0 and i%5==0:
			yield "Bada Boom!!"
		elif i%3==0:
			yield "Bada"
		elif i%5==0:
			yield "Boom"
		else:
			yield i
		i = i + 1
a = genBadaBoom(10)
z = [e for e in a]
print("B A D A B O O M!:")
print(z)
print(" ")

#COMBINACIONES DE ROPA
C=['ROJA','NEGRA','AZUL','MORADA','CAFE']
P=['NEGRO','AZUL','CAFE OBSCURO','CREMA']
A=['CINTURON','TIRANTES', 'LENTES', 'FEDORA']
print("C O M B I N A C I O E S		D E		R O P A")
R=[[x, y, z] for x in C for y in P for z in A]
print(R)
print('Cantidad total de conjuntos posibles:',len(R))
print(" ")

#SOMBREROS FEDORA
def fedora(L):
	if not L:
		return []
	if 'FEDORA' in L[0]:
		return [L[0]] + fedora(L[1:])
	else: return fedora(L[1:])
R=[[x, y, z] for x in C for y in P for z in A]
Z = fedora(R)
print("S O M B R E R O S	F E D O R A:")
print(Z)
print("Cantidad de conjuntos con sombrero Fedora:",len(Z))

#INTEGRANTES: Morales Perez Mariela & Mendoza Trejo Jairo
