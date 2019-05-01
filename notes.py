# argv[1] = Caminho completo do gabarito (.py) da aula
# argv[2] = Caminho completo do arquivo .py do aluno

import sys

gabarito = __import__(sys.argv[1])
ex_aluno = __import__(sys.argv[2])
exercicio=6

# Contém os exercícios existentes
# Cada elemento i é uma lista.
# Ex.:
#		Exercício 2:
#		2.1.1
#		2.1.2
#		2.2
#		2.3
#		exercicios[1] = [[1,2], 2, 3]
#
# exercicios[i] = -1 quando o exercício não é para ser
# corrigido automaticamente.
exercicios = [
	[1], # Exercício 1
	[2], # Exercício 2
	[-1], # Exercício 3
	[1,2,3,4,5,6,7,8,9,10,11,12] # Exercício 4
]

for ex in exercicios:
	ex += 1

	if type(ex) == type([]):
		# O exercício possui sub-exercícios
		for sub_ex in ex:

	else:
		# O exercício não possui sub-exercícios
		
