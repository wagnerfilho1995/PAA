#-*- coding: utf-8 -*-

def lcs(x, y):

	#	Salve o numero de linhas e de colunas que a sua matriz tera
	linha = len(x)	#	Linhas = Nº elementos da torre 1
	coluna = len(y) #	Colunas = Nº elementos da torre 2

	#	Inicialize a matriz dando uma coluna e uma linha a mais
	M = [[None]*(coluna+1) for i in range(0, linha+1)]

	for i in range(linha+1):
		for j in range(coluna+1):
			#	Caso os dois seja 0, coloque 0
			if i == 0 or j == 0:
				M[i][j] = 0
			#	Caso os dois se combinem, coloque o valor do elemento na matriz, subindo em diagonal uma posição + 1 
			elif x[i-1] == y[j-1]:
				M[i][j] = M[i-1][j-1]+1
			#	Caso Contrário, faça o maximo entre a 
			else:
				M[i][j] = max(M[i-1][j] , M[i][j-1])
	#	A resposta será o último elemento da matriz posição[ultima linha, ultima coluna]
	return M[linha][coluna]

#	MAIN
t = [int(i) for i in input().split()]
k = 1
while t[0] + t[1] > 0:

	x = [int(i) for i in input().split()]
	y = [int(i) for i in input().split()]

	print( "Twin Towers #{}".format(k) )
	print( "Number of Tiles : {}\n".format ( lcs( x,y ) ))
	k += 1
	t = [int(i) for i in input().split()]