"""
	Este programa recebe um arquivo.py como parâmetro e faz as seguintes operações:
	- Remove linhas que contenham 'input' ou 'print'
	- Reescreve o arquivo inteiro mantendo somente as funções (isto é feito para
	  remover erro de sintaxe do python para comandos fora de funções) 

	argv[1] -> Nome do arquivo com o exercício do aluno
"""

import sys, os


arquivo = open(sys.argv[1])
codigoSemPrintEInput = []
for linha in arquivo:
	if "print" in linha or "input" in linha:
		continue
	codigoSemPrintEInput.append(linha)
arquivo.close()

codigoFinal = []
linha = 0
nLinhas = len(codigoSemPrintEInput)
while linha < nLinhas:
	if "def " in codigoSemPrintEInput[linha]:
		# É a definição de uma função de exercício

		# Copia todas as linhas que possuem um '\t'
		funcao = codigoSemPrintEInput[linha]
		linha += 1
		while linha < nLinhas and (codigoSemPrintEInput[linha][0] == '\t' or codigoSemPrintEInput[linha][0] == ' '):
			funcao += codigoSemPrintEInput[linha]
			linha += 1

		# Verifico se a função tem pelo menos 1 linha
		if funcao.count("\n") >= 2: 
		
			# Testa se a sintaxe da função está correta
			# Caso sim, continua com ela no arquivo original
			# Caso não, remove ela do arquivo original
			try:
				testaFuncao = open("teste.py", "w")
				testaFuncao.write(funcao)
				testaFuncao.close()

				t = __import__("teste")
				codigoFinal.append(funcao)
				os.remove("teste.py")
			except:
				None

	linha += 1

saida = open(sys.argv[1], 'w')
for funcao in codigoFinal:
	saida.write(funcao)
saida.close()