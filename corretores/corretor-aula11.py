"""
	Entradas (linha de comando):
		- argv[1] = Caminho completo do arquivo do aluno (um arquivo .py).
		- argv[2] = Caminho completo do gabarito (um arquivo .py).
		
		OBS.: - Deve ser passado somente o nome do arquivo, sem a extensão .py.
	    Exemplo:
	    	- Arquivo do aluno: "alunos/joao.py"
	    	- Gabarito: "gabaritos/aulaX"

		Execução do script:
		$ python3 corretor-aulaX.py alunos/joao gabaritos/aulaX

	Saída (stdout): 
		1ª linha: String contando o caractere '0' se o aluno não obteve 0 em nenhuma questão ou os 
				  números dos exercícios que ele obteve zero, por exemplo: '1.1,2,3,4.4'
		2ª linha: Nota final do aluno para o exercício, no intervalo [0,1] (porcentagem).
		   		  Em caso de erro, a saída será uma string com o erro correspondente.
"""

import sys, signal, random
from random import randint
from random import seed
seed(7)

def signalHandler(signum, frame):
    raise Exception('Timed out!')

################################# Definições ######################################################
signal.signal(signal.SIGALRM, signalHandler)
tempoAlarme = 1 # Quantidade de segundos para executar 1 exercício
notaFinal = 0.0

"""
	A variável 'exercicios' deve ser uma lista de strings com os nomes das funções dos exercícios.
	Ex.: exercicios = ["exercicio_1_1", "exercicio_1_2", "exercicio_2", ...]
"""
exercicios = ['exercicio_1',\
			  'exercicio_2',\
			  'exercicio_3',\
			  'exercicio_4',\
			  'exercicio_5_1',\
			  'exercicio_5_2',\
			  'exercicio_5_3',\
			 ]

numExercicios = len(exercicios) # Número TOTAL de exercícios

"""
	A variável 'testes' deve ser uma lista onde cada elemento é uma lista com testes.
	--> testes[i] deve conter uma lista de testes correspondente à exercicios[i].
	Ex.: testes = [[1,2,3,4,5], [(0,1), (0,2), (0,4)], [x for x in range(10)], ...]

	--> O teste em si são os argumentos que a função irá receber. Caso a função do exercício receba
		mais que um parâmetro, então o elemento será uma tupla.

	--> Se a função não receber nenhum parâmetro, a sua lista de testes deverá ser uma lista vazia.
"""

caracteres = '       ' + 'aeiouAEIOU' + 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' + '?!.,;:'
testes = [['{:02}/{:02}/{:02}'.format(randint(1,28), randint(1,12), randint(1900,2500)) for i in range(20)],\
		  [''.join(random.choice(caracteres) for i in range(randint(1,30))) for j in range(20)],\
		  ['123.456.789-12', '147.895.685-98', '123.456789.12', '01234567890', '111.111.111-11', '328.265.015-93'],\
		  list(range(0,101)),\
		  [],\
		  [],\
		  list(range(1,19))
		 ]

# Armazena quais exercícios o aluno alcançou nota 0 (zero)
erros = ''

####################################################################################################

# Try-catch usado para verificar se há erro de sintaxe no arquivo do aluno
try:
	aluno = __import__(sys.argv[1])
except:
	print('Erro ao importar o arquivo do aluno.')

# Try-catch usado para verificar se há erro de sintaxe no arquivo do aluno
try:
	gabarito = __import__(sys.argv[2])
except:
	print('Erro ao importar o gabarito.')


############################################# Correção #############################################
for i in range(numExercicios):
	nTestes = len(testes[i]) # Números de testes para o i-ésimo exercício

	notaParcial = 0.0
	if nTestes == 0:
		# A função não recebe parâmetros

		execucaoGabarito = 'saidaGabarito = gabarito.' + exercicios[i] + '()'
		exec(execucaoGabarito)
		
		try:
			execucaoAluno = 'saidaAluno = aluno.' + exercicios[i] + '()'
			signal.alarm(tempoAlarme) # Ativa o alarme
			exec(execucaoAluno)
			signal.alarm(0) # Cancela o alarme

			assert(saidaGabarito == saidaAluno)
			notaParcial = 1
		except Exception:
			None
	else:
		# A Função possui pelo menos 1 parâmetro

		for j in range(nTestes):
			if type(testes[i][j]) != type((0,0)):
				# A função possui somente 1 parâmetro
				if type(testes[i][j]) == type(''):
					execucaoGabarito = 'saidaGabarito = gabarito.' + exercicios[i] + "('" + testes[i][j] + "')"
				else:
					execucaoGabarito = 'saidaGabarito = gabarito.' + exercicios[i] + '(' + str(testes[i][j]) + ')'
				exec(execucaoGabarito)
				
				try:
					if type(testes[i][j]) == type(''):
						execucaoAluno = 'saidaAluno = aluno.' + exercicios[i] + "('" + testes[i][j] + "')"
					else:
						execucaoAluno = 'saidaAluno = aluno.' + exercicios[i] + '(' + str(testes[i][j]) + ')'

					signal.alarm(tempoAlarme) # Ativa o alarme
					exec(execucaoAluno)
					signal.alarm(0) # Cancela o alarme

					if i == 1: # Exercício 2
						assert(saidaGabarito[0] == saidaAluno[0])
						for l in range(1,4):
							for pair in saidaGabarito[l]:
								assert(pair in saidaAluno[l])
					else:
						assert(saidaGabarito == saidaAluno)

					notaParcial += (1/nTestes)
				except Exception:
					continue
			else:
				# A função possui mais de 1 parâmetro
				nParam = len(testes[i][j]) # Número de parâmetros da função

				execucaoGabarito = 'saidaGabarito = gabarito.' + exercicios[i] + '('
				execucaoAluno = 'saidaAluno = aluno.' + exercicios[i] + '('
				for parametro in range(nParam):
					execucaoGabarito = execucaoGabarito + str(testes[i][j][parametro]) + ','
					execucaoAluno 	 = execucaoAluno    + str(testes[i][j][parametro]) + ','

				execucaoGabarito = execucaoGabarito[:-1] + ')' # Substitui a última vírgula por ')'
				execucaoAluno 	 = execucaoAluno[:-1] + ')' # Substitui a última vírgula por ')'

				exec(execucaoGabarito)

				try:
					signal.alarm(tempoAlarme) # Ativa o alarme
					exec(execucaoAluno)
					signal.alarm(0) # Cancela o alarme

					assert(saidaGabarito == saidaAluno)
					notaParcial += (1/nTestes)
				except Exception:
					continue

	# Seleciona o número do exercício e adiciona em erros
	if notaParcial == 0:
		tokens = exercicios[i].split('_')
		ex = ''
		for j in range(1,len(tokens)):
			ex = ex + tokens[j] + '.'
		ex = ex[:-1]
		erros = erros + ex + ','
	else:
		notaFinal += (notaParcial * 1.0/numExercicios)
####################################################################################################

# Se a nota do aluno for >= 0.99, arredonda para 1.0, para o caso de o aluno ter acertado todas 
# as questões e haver um erro de precisão no somatório das notas parciais.
if notaFinal >= 0.99:
	notaFinal = 1.0

if erros == '':
	# O aluno não obteve nota zero em nenhum exercício
	print('0', end='#')
else:
	print(erros[:-1], end='#')

# Imprime a nota final do aluno com 4 casas decimais.
# A nota está no intervalo [0,1]
print('%.2f'%notaFinal)
