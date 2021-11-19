import sys

def numeroBasePorEstado(estado):
	return {
		'SP': [0,0,0,0,0,0,0,0,8],
		'RJ': [0,0,0,0,0,0,0,0,9]
	}.get(estado,[0,0,0,0,0,0,0,0,0]) #default

def incrementa(arrayDeInteiros, estado):
	#Transformar array de int em um Int
	numeroEmChar = [str(integer) for integer in arrayDeInteiros]
	numeroEmString = "".join(numeroEmChar)
	numeroInteiro = int(numeroEmString)

	numeroInteiro += 10

	novoArrayDeInteiros = numeroBasePorEstado(estado)

	tamanhoNumeroInteiro = len(str(numeroInteiro))
	tamanhoNovoArray = len(novoArrayDeInteiros)
	indice = tamanhoNovoArray - tamanhoNumeroInteiro

	for count in str(numeroInteiro):
		novoArrayDeInteiros[indice] = int(count)
		indice += 1

	return novoArrayDeInteiros

def gerarNumeros(estado):

	nomeDoArquivo = 'CPFs_' + estado +'.txt'
	arquivo = open(nomeDoArquivo, 'w')

	#Transformando array de Int em Str
	numeroBaseArray = numeroBasePorEstado(estado)
	numeroEmChar = [str(integer) for integer in numeroBaseArray]
	numeroBase = "".join(numeroEmChar)
	numeroBaseInt = int(numeroBase)

	numeroLimiteArray = numeroBasePorEstado(estado)
	numeroLimiteChar = [str(integer) for integer in numeroLimiteArray]
	numeroLimite = "".join(numeroLimiteChar)
	numeroLimiteInt = int(numeroLimite)
	numeroLimiteInt += 999999990

	while (int(numeroBase) < numeroLimiteInt):
		cpfFormatado = calculaDV(numeroBaseArray,'true')
		arquivo.write(cpfFormatado+' '+numeroBase+cpfFormatado[-2]+cpfFormatado[-1]+'\n')
		numeroBaseArray = incrementa(numeroBase, estado)
		numeroEmChar = [str(integer) for integer in numeroBaseArray]
		numeroBase = "".join(numeroEmChar)

	arquivo.close()

def calculaDV(numeroBase,formatar):    

   
   # Calculado o primeiro DV
   somaJ = ( numeroBase[0] * 10 ) + ( numeroBase[1] * 9 ) + ( numeroBase[2] * 8 ) + ( numeroBase[3] * 7 )  + ( numeroBase[4] * 6 ) + ( numeroBase[5] * 5 ) + ( numeroBase[6] * 4 )  + ( numeroBase[7] * 3 ) + ( numeroBase[8] * 2 )

   restoJ = somaJ % 11

   if ( restoJ == 0 or restoJ == 1 ):
      j = 0
   else:
      j = 11 - restoJ   

   numeroBase.append(j)

   # Calculado o segundo DV
   somaK = ( numeroBase[0] * 11 ) + ( numeroBase[1] * 10 ) + ( numeroBase[2] * 9 ) + ( numeroBase[3] * 8 )  + ( numeroBase[4] * 7 )  + ( numeroBase[5] * 6 ) + ( numeroBase[6] * 5 )  + ( numeroBase[7] * 4 )  + ( numeroBase[8] * 3 ) + ( j * 2 )

   restoK = somaK % 11
   
   if ( restoK == 0 or restoK == 1 ):
      k = 0
   else:
      k = 11 - restoK      

   numeroBase.append(k)
   
   cpf = ''.join(str(x) for x in numeroBase)

   if formatar:
      return cpf[ :3 ] + '.' + cpf[ 3:6 ] + '.' + cpf[ 6:9 ] + '-' + cpf[ 9: ]
   else:
      return cpf


if __name__ == '__main__':

	estado = sys.argv[1]
	gerarNumeros(estado)
	print('DONE!!')
