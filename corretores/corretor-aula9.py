"""
	Corretor automático para os exercícios da aula 09.
	
	Entradas (linha de comando):
		- argv[1] = Caminho completo do arquivo do aluno (um arquivo .py).
		- argv[2] = Caminho completo do arquivo do gabarito (um arquivo .py).
		
		OBS.: - Devem ser passados somente os nomes dos arquivos, sem a extensão .py.
			    Exemplo:
			    	- Arquivo do aluno: "alunos/joao.py"
			    	- Arquivo do gabarito: "gabaritos/gabarito-aula09.py"
  
  			    	Execução do script:
			    		$ python3 aula09.py alunos/joao gabaritos/gabarito-aula09

	Saída: Nota final do aluno para o exercício 9, no intervalo [0,100].
"""

import sys, signal

def signal_handler(signum, frame):
    raise Exception("Timed out!")

signal.signal(signal.SIGALRM, signal_handler)
tempoAlarme = 2 # Quantidade de segundos para executar 1 exercício

# Try-catch usado para verificar se há erro de sintaxe no arquivo python do aluno
try:
	# Variáveis
	aluno = __import__(sys.argv[1])
	gabarito = __import__(sys.argv[2])
	nota_final = 0.0
	num_questoes = 7
	########################################
	
	# Exercício 1
	nota_parcial = 0.0
	for i in range(10):
		try:
			signal.alarm(tempoAlarme) # 2 segundos para executar a função
			assert(aluno.exercicio_1(i) == gabarito.exercicio_1(i))
			nota_parcial += (1.0/10)
			signal.alarm(0) # Cancela o alarme
		except Exception:
			continue
	
	nota_final += nota_parcial
	########################################
	
	# Exercício 2
	nota_parcial = 0.0
	for i in range(10):
		try:
			signal.alarm(tempoAlarme) # 2 segundos para executar a função
			assert(aluno.exercicio_2(i) == gabarito.exercicio_2(i))
			nota_parcial += (1.0/10)
			signal.alarm(0) # Cancela o alarme
		except Exception:
			continue
	
	nota_final += nota_parcial
	########################################
	
	# Exercício 3
	tuplas = [2,4,6,8,10]
	nota_parcial = 0.0
	for i in tuplas:
		try:
			signal.alarm(tempoAlarme) # 2 segundos para executar a função
			respAluno = aluno.exercicio_3(tuple(range(i)))
			respGabarito1 = gabarito.exercicio_3(tuple(range(i)))
			respGabarito2 = respGabarito1[:-1] # String sem o \n no final

			assert(respAluno == respGabarito1 or respAluno == respGabarito2)
			nota_parcial += (1.0/len(tuplas))
			signal.alarm(0) # Cancela o alarme
		except Exception:
			pass
	
	nota_final += nota_parcial
	########################################
	
	# Exercício 4
	nota_parcial = 0.0
	tuplas = [(1,2,3,4,5), (5,4,3,2,1), (1,1,1,1,1), (2,2,2,2,2),\
	 (0,1,2,3,4), (9,6,1,2,7,7,8,6,6)]
	for t in tuplas:
		try:
			signal.alarm(tempoAlarme) # 2 segundos para executar a função
			assert(aluno.exercicio_4(t) == gabarito.exercicio_4(t))
			nota_parcial += (1.0/len(tuplas))
			signal.alarm(0) # Cancela o alarme
		except Exception:
			continue
	
	nota_final += nota_parcial
	########################################
	
	# Exercício 5
	nota_parcial = 0.0
	listas = [[1,2,3,4,5], [3,2,1], [8], []]
	for l in listas:
		try:
			signal.alarm(tempoAlarme) # 2 segundos para executar a função
			assert(aluno.exercicio_5_1(t) == gabarito.exercicio_5_1(t))
			nota_parcial += (1.0/(2.0*len(listas)))
			signal.alarm(0) # Cancela o alarme
		except Exception:
			pass
	
		try:
			signal.alarm(tempoAlarme) # 2 segundos para executar a função
			assert(aluno.exercicio_5_2(t) == gabarito.exercicio_5_2(t))
			nota_parcial += (1.0/(2.0*len(listas)))
			signal.alarm(0) # Cancela o alarme
		except Exception:
			pass
	
	nota_final += nota_parcial
	########################################
	
	# Exercício 6
	listas_de_tuplas = [ [[(10,20,30), (40,50,60), (70,80,90)], 100],\
	 [[(1,1,1), (1,1,1)], 1], [[(3,2,1), (6,5,4), (9,8,7)], -1]]
	nota_parcial = 0.0
	for l, n in listas_de_tuplas:
		try:
			signal.alarm(tempoAlarme) # 2 segundos para executar a função
			assert(aluno.exercicio_6(l, n) == gabarito.exercicio_6(l, n))
			nota_parcial += (1.0/len(listas_de_tuplas))
			signal.alarm(0) # Cancela o alarme
		except Exception:
			pass
	
	nota_final += nota_parcial
	########################################
	
	# Exercício 7
	cotacoes = [1.00, 3.98, 4.5, 0.5]
	nota_parcial = 0.0
	for c in cotacoes:
		try:
			signal.alarm(tempoAlarme) # 2 segundos para executar a função
			respAluno = aluno.exercicio_7(c)
			respGabarito1 = gabarito.exercicio_7(c)
			respGabarito2 = respGabarito1[:-1] # String sem o \n no final

			assert(respAluno == respGabarito1 or respAluno == respGabarito2)
			nota_parcial += (1.0/len(cotacoes))
			signal.alarm(0) # Cancela o alarme
		except Exception:
			pass
	
	nota_final += nota_parcial
	########################################
	
	# Se a nota do aluno for >= 99, arredonda para 100, para o caso de o aluno
	# ter acertado todas as questões e haver um erro de precisão no somatório
	# das notas parciais
	if nota_final >= 99.0:
		nota_final = 100.0

	# Imprime a nota final do aluno com 2 casas decimais.
	# A nota está no intervalo [0,100]
	print("%.2f"%((nota_final/num_questoes)*100))
except:
	print("Erro de sintaxe no python")