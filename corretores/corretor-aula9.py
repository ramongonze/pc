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
exercicios = ['exercicio_1', \
			  'exercicio_2', \
			  'exercicio_3', \
			  'exercicio_4', \
			  'exercicio_5', \
			  'exercicio_6', \
			  'exercicio_7'
			 ]

numExercicios = len(exercicios) # Número TOTAL de exercícios

"""
	A variável 'testes' deve ser uma lista onde cada elemento é uma lista com testes.
	--> testes[i] deve conter uma lista de testes correspondente à exercicios[i].
	Ex.: testes = [[1,2,3,4,5], [(0,1), (0,2), (0,4)], [x for x in range(10)], ...]

	--> O teste em si são os argumentos que a função irá receber. Caso a função do exercício receba
		mais que um parâmetro, então o elemento será uma tupla.
"""
testes = [list(range(1,20)) , \
		  list(range(1,20)) , \
		  [[randint(1,100) for j in range(1,i)] for i in range(1,101)], \
		  [[randint(1,100) for j in range(1,i)] for i in range(1,101)], \
		  [[randint(1,100) for j in range(1,i)] for i in range(1,101)], \
		  [([[randint(1,100) for j in range(1,1+randint(1,30))] for i in range(1,k+1)], randint(1,100)) for k in range(1,30)], \
		  [3.00, 3.15, 3.30, 3.45, 3.50, 3.65, 3.80, 4.00, 4.12, 4.30]
		 ]

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
				execucaoGabarito = 'saidaGabarito = gabarito.' + exercicios[i] + '(' + str(testes[i][j]) + ')'
				exec(execucaoGabarito)
				
				try:
					execucaoAluno = 'saidaAluno = aluno.' + exercicios[i] + '(' + str(testes[i][j]) + ')'
					signal.alarm(tempoAlarme) # Ativa o alarme
					exec(execucaoAluno)
					signal.alarm(0) # Cancela o alarme

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

	notaFinal += (notaParcial * 1.0/numExercicios)
####################################################################################################

# Se a nota do aluno for >= 0.99, arredonda para 1.0, para o caso de o aluno ter acertado todas 
# as questões e haver um erro de precisão no somatório das notas parciais.
if notaFinal >= 0.99:
	notaFinal = 1.0

# Imprime a nota final do aluno com 4 casas decimais.
# A nota está no intervalo [0,1]
print('%.2f'%notaFinal)

