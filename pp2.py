entrada = input() 
#entrada= open('3.txt')
linhas_simbolos = ""
pilha = list()
alerta = 0
abreCh =0
abrePar =0
abreCol = 0
#linha = entrada.readline()
while entrada:
	#print(entrada)
	linha = entrada
	
	for simbolo in linha:
		#print(simbolo)
		if (simbolo != '\n'):
			if (simbolo == "("): 
				pilha.append(simbolo)
				linhas_simbolos += simbolo
			if (simbolo == ")"): 
				linhas_simbolos += simbolo
				if (len(pilha)!= 0):
					abrePar = pilha.pop()
					#print(abrePar)
					if(abrePar != "("):
						pilha.append(abrePar)
				elif(len(pilha)== 0):
					alerta += 1
			if (simbolo == "["):
				pilha.append(simbolo)
				linhas_simbolos += simbolo
			if (simbolo == "]"):
				linhas_simbolos += simbolo
				if (len(pilha)!= 0):
					abreCol = pilha.pop()
					#print(abreCol)
					if(abreCol != "["):
						pilha.append(abreCol)
				elif(len(pilha)== 0):
					alerta += 1
			if (simbolo == "{"):
				pilha.append(simbolo)
				linhas_simbolos += simbolo
			if (simbolo == "}"):
				linhas_simbolos += simbolo
				if (len(pilha)!= 0):
					abreCh = pilha.pop()
					#print(abreCh)
					if(abreCh != "{"):
						pilha.append(abreCh)
				elif(len(pilha)== 0):
					alerta += 1
	
	entrada = input()
	

	if(len(pilha) == 0 and alerta == 0 and linha[0]!="\n"): print("True")
	if(len(pilha) == 0 and alerta == 0 and linha[0]=="\n"): print("True")
	if(len(pilha) != 0 or alerta != 0 and linha[0]!="\n"): print("False")
	#print("antes de limpar",pilha)
	pilha.clear()
	alerta = 0
	#linha = entrada.readline()
	#print("depois de limpar ",pilha) 


#print(linhas_simbolos)
abreCh =0
abrePar =0
abreCol = 0

pilha.clear()
pilha = list()
for simbolosGeral in linhas_simbolos:
	if (simbolosGeral != '\n'):
		if (simbolosGeral == "("): pilha.append(simbolosGeral)
		if (simbolosGeral == ")"):
			if (len(pilha)!= 0):
				abrePar = pilha.pop()
				#print(abrePar)
				if(abrePar != "("):
					pilha.append(abrePar)
			elif(len(pilha)== 0):
				#print("do parentese",len(pilha))
				alerta += 1
		if (simbolosGeral == "["): pilha.append(simbolosGeral)
		if (simbolosGeral == "]"):
			if (len(pilha)!= 0):
				abreCol = pilha.pop()
				#print(abreCol)
				if(abreCol != "["):
					pilha.append(abreCol)
			elif(len(pilha)== 0):
				#print("do colchete",len(pilha))
				alerta += 1
		if (simbolosGeral == "{"): pilha.append(simbolosGeral)
		if (simbolosGeral == "}"):
			if (len(pilha)!= 0):
				abreCh = pilha.pop()
				#print(abreCh)
				if(abreCh != "{"):
					pilha.append(abreCh)
			elif(len(pilha)== 0):
				#print("do chave",len(pilha))
				alerta += 1


if(len(pilha) == 0 and alerta == 0): print("True")
if(len(pilha) != 0 or alerta != 0): print("False")
#if(linhas_simbolos == 0): print("False")
pilha.clear()
