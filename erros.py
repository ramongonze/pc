"""
	Script que recebe um arquivo com exercícios que os alunos zeraram e produz um relatório
	com o número de alunos que zeraram cada um dos exercícios.

	Entrada:
		argv[1]: Número do exercício
		argv[2]: Número de alunos
		argv[3]: Arquivo onde cada linha contém o número de um exercício

	Saída (stdout):
		Relatório com o número de alunos que zerou os exercícios, para todos os exercícios
"""

import sys

aula = sys.argv[1]
numAlunos = sys.argv[2]
arquivo = open(sys.argv[3])
erros = {}
for linha in arquivo:
	linha = linha.replace('\n', '')
	if linha in erros:
		erros[linha] += 1
	else:
		erros[linha] = 1
		
for erro in erros:
	print('Exercício ' + erro + ': ' + str(erros[erro]) + '/' + numAlunos)
