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

	Saída (stdout): Nota final do aluno para o exercício, no intervalo [0,1] (porcentagem).
		   			Em caso de erro, a saída será uma string com o erro correspondente.
"""

import sys, signal
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
exercicios = ['exercicio_1_1', 'exercicio_1_2',\
			  'exercicio_2',\
			  'exercicio_3_1_1', 'exercicio_3_1_2',\
			  'exercicio_3_2_1', 'exercicio_3_2_2',\
			  'exercicio_3_3_1', 'exercicio_3_3_2',\
			  'exercicio_3_4_1', 'exercicio_3_4_2',\
			  'exercicio_3_5_1', 'exercicio_3_5_2',\
			  'exercicio_3_6_1', 'exercicio_3_6_2',\
			  'exercicio_3_7_1', 'exercicio_3_7_2',\
			  'exercicio_3_8_1', 'exercicio_3_8_2',\
			  'exercicio_3_9_1', 'exercicio_3_9_2',\
			  'exercicio_3_10_1', 'exercicio_3_10_2',\
			  'exercicio_3_11_1', 'exercicio_3_11_2',\
			  'exercicio_3_12_1', 'exercicio_3_12_2'
			 ]

numExercicios = len(exercicios) # Número TOTAL de exercícios

"""
	A variável 'testes' deve ser uma lista onde cada elemento é uma lista com testes.
	--> testes[i] deve conter uma lista de testes correspondente à exercicios[i].
	Ex.: testes = [[1,2,3,4,5], [(0,1), (0,2), (0,4)], [x for x in range(10)], ...]

	--> O teste em si são os argumentos que a função irá receber. Caso a função do exercício receba
		mais que um parâmetro, então o elemento será uma tupla.
"""
testes = [[(n,0) for n in range(20)], \
		  [n for n in range(20)], \
		  [n for n in range(1,31)], \
		  [n for n in range(1,31)], \
		  [n for n in range(1,31)], \
		  [n for n in range(1,31)], \
		  [n for n in range(1,31)], \
		  [n for n in range(1,21)], \
		  [n for n in range(1,21)], \
		  [(n, x) for n in range(1,11) for x in range(10)], \
		  [(n, x) for n in range(1,11) for x in range(10)], \
		  [n for n in range(1,21)], \
		  [n for n in range(1,21)], \
		  [n for n in range(1,31)], \
		  [n for n in range(1,31)], \
		  [n for n in range(20)], \
		  [n for n in range(20)], \
		  [n for n in range(1,31)], \
		  [n for n in range(1,31)], \
		  [n for n in range(1,31)], \
		  [n for n in range(1,31)], \
		  [n for n in range(1,31)], \
		  [n for n in range(1,31)], \
		  [(n, x) for n in range(1,11) for x in range(1,11)], \
		  [(n, x) for n in range(1,11) for x in range(1,11)], \
		  [n for n in range(1,31)], \
		  [n for n in range(1,31)]
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

	notaParcial = 0
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
				execucaoGabarito = 'saidaGabarito = gabarito.' + exercicios[i] + '(' + str(testes[i][j]) + ')'
				exec(execucaoGabarito)
				
				try:
					execucaoAluno = 'saidaAluno = aluno.' + exercicios[i] + '(' + str(testes[i][j]) + ')'
					signal.alarm(tempoAlarme) # Ativa o alarme
					exec(execucaoAluno)
					signal.alarm(0) # Cancela o alarme

					assert(saidaGabarito == saidaAluno)
					notaParcial += 1
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
					notaParcial += 1
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
		notaFinal += (notaParcial/nTestes)
####################################################################################################

notaFinal /= numExercicios

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
