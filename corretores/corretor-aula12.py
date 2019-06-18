"""
	Corretor automático para os exercícios da aula 12.
	
	Entradas (linha de comando):
		- argv[1] = Caminho completo do arquivo do aluno (um arquivo .py).
		
		OBS.: - Deve ser passado somente o nome do arquivo, sem a extensão .py.
	    Exemplo:
	    	- Arquivo do aluno: "alunos/joao.py"

		Execução do script:
		$ python3 correor-aulaX.py alunos/joao

	Saída: Nota final do aluno para o exercício, no intervalo [0,100].

--------------------------------------------------------------------------------
	Estrutura básica para a correção de um exercício:
	
	testes = [...\
			  ...\
			  ...]
	nota_parcial = 0.0
	for t in testes:
		try:
			signal.alarm(tempo_alarme)
			saida = aluno.exercicio_x_y(t)
			signal.alarm(0) # Cancela o alarme
			
			assert(...)

			nota_parcial += (1/len(testes))
		except Exception:
			continue

	nota_final += nota_parcial
"""

import sys, signal

def signal_handler(signum, frame):
    raise Exception("Timed out!")

################### Definições ######################
signal.signal(signal.SIGALRM, signal_handler)
tempo_alarme = 2 # Quantidade de segundos para executar 1 exercício
num_questoes = 1 # Número de exercícios da aula
nota_final = 0.0
#####################################################

# Try-catch usado para verificar se há erro de sintaxe no arquivo do aluno
try:
	aluno = __import__(sys.argv[1])
except:
	print("Erro ao importar o arquivo do aluno.	")

def comparaStrings(s1, s2, tipo):
	"""
		s1: String 1
		s2: String 2
		tipo: Representação 1, 2 ou 3
	"""
	if tipo == 1:
		for i in range(len(s1)):
			if s1[1][i] != s2[1][s2.index(s1[0][i])]
				return False
	elif tipo == 2:
		for i in range(0,len(s1),2):
			if s1[i+1] != s2[s2.index(s1[i])+1]
				return False
	else:
		return sorted(s1) == sorted(s2)

	return True

################### Exercício 1 #####################
nota_parcial = 0.0
testes = [("ola mundo", 1), \
		  ("ola mundo", 2), \
		  ("ola mundo", 3), \
		  ("ola mundo", 4)]

gabarito = [(['a','o','u','d','l','m','n'], [1,2,1,1,1,1,1]), \
			['a',1,'o',2,'u',1,'d',1,'l',1,'m',1,'n',1], \
			[('a',1),('o',2),('u',1),('d',1),('l',1),('m',1),('n',1)], \
			None]

for i in range(len(testes)):
	try:
		signal.alarm(tempo_alarme)
		saida = aluno.exercicio_12_1(testes[i][0], testes[i][1])
		signal.alarm(0) # Cancela o alarme

		if i < 4:
			assert(comparaStrings(saida, gabarito[i], i+1))
		else:
			assert(saida == None)

		nota_parcial += (1/len(testes))
	except Exception:
		continue

nota_final += nota_parcial
#####################################################

################### Exercício 2 #####################
testes = [(['a','o','u','d','l','m','n'], [1,2,1,1,1,1,1]), \
		  ['a',1,'o',2,'u',1,'d',1,'l',1,'m',1,'n',1], \
		  [('a',1),('o',2),('u',1),('d',1),('l',1),('m',1),('n',1)]]

for i in range(len(testes)):
	try:
		signal.alarm(tempo_alarme)
		saida = aluno.exercicio_12_2(testes[i])
		signal.alarm(0) # Cancela o alarme

		assert(saida == (4,4))
		nota_parcial += (1/len(testes))
	except Exception:
		continue

nota_final += nota_parcial
#####################################################

################### Exercício 3 #####################
##### 3.1 #####
testes = [(['a','o','c','g','m','p','r'], [3,2,1,1,1,1,2]), \
		  ['a',3,'o',2,'c',1,'g',1,'m',1,'p',1,'r',2], \
		  [('a',3),('o',2),('c',1),('g',1),('m',1),('p',1),('r',2)]]

gabarito = ([('a',3),('o',2)],[('c',1),('g',1),('m',1),('p',1),('r',2)])

for i in range(len(testes)):
	try:
		signal.alarm(tempo_alarme)
		saida = aluno.exercicio_12_3_1(testes[i])
		signal.alarm(0) # Cancela o alarme

		assert(saida == gabarito)
		nota_parcial += (1/len(testes)/6)
	except Exception:
		continue

nota_final += nota_parcial
###############

##### 3.2 #####
testes = [((['a','o','c','g','m','p','r'], [3,2,1,1,1,1,2]), 'a'), \
		  (['a',3,'o',2,'c',1,'g',1,'m',1,'p',1,'r',2], 'a'), \
		  ([('a',3),('o',2),('c',1),('g',1),('m',1),('p',1),('r',2)], 'a')]

gabarito = 3

for i in range(len(testes)):
	try:
		signal.alarm(tempo_alarme)
		saida = aluno.exercicio_12_3_2(testes[i][0], testes[i][1])
		signal.alarm(0) # Cancela o alarme

		assert(saida == gabarito)
		nota_parcial += (1/len(testes)/6)
	except Exception:
		continue

nota_final += nota_parcial
###############

##### 3.3 #####
testes = [((['a','c','g','m','p','r'], [3,1,1,1,1,2]), 'o', -1), \
		  ((['a','o','c','g','m','p','r'], [3,0,1,1,1,1,2]), 'o', 0), \
		  (['a',3,'o',2,'c',1,'m',1,'p',1,'r',2], 'g', -1), \
		  (['a',3,'o',2,'c',1,'g',1,'m',0,'p',1,'r',2], 'm', 0), \
		  ([('o',2),('c',1),('g',1),('m',1),('p',1),('r',2)], 'a', -1), \
		  ([('a',0),('o',2),('c',1),('g',1),('m',1),('p',1),('r',2)], 'o', 0)]

gabarito = [(['a','c','g','m','p','r'], [3,1,1,1,1,2]), \
		    (['a','o','c','g','m','p','r'], [3,0,1,1,1,1,2]), \
		    ['a',3,'o',2,'c',1,'m',1,'p',1,'r',2], \
		    ['a',3,'o',2,'c',1,'g',1,'m',0,'p',1,'r',2], \
		    [('o',2),('c',1),('g',1),('m',1),('p',1),('r',2)], \
		    [('a',0),('o',2),('c',1),('g',1),('m',1),('p',1),('r',2)]]

for i in range(len(testes)):
	try:
		signal.alarm(tempo_alarme)
		saida = aluno.exercicio_12_3_3(testes[i][0], testes[i][1], testes[i][2])
		signal.alarm(0) # Cancela o alarme

		if i in [0,1]:
			assert(comparaStrings(saida, gabarito[i], 1))
		elif i in [2,3]:
			assert(comparaStrings(saida, gabarito[i], 2))
		else:
			assert(comparaStrings(saida, gabarito[i], 3))
		
		nota_parcial += (1/len(testes)/6)
	except Exception:
		continue

nota_final += nota_parcial
###############

##### 3.4 #####
testes = ["programação", "ábcãàó", "quick sort"]

gabarito = 2

for i in range(len(testes)):
	try:
		signal.alarm(tempo_alarme)
		saida = aluno.exercicio_12_3_4(testes[i][0], testes[i][1])
		signal.alarm(0) # Cancela o alarme

		assert(saida == gabarito)
		nota_parcial += (1/len(testes)/6)
	except Exception:
		continue

nota_final += nota_parcial

###############

##### 3.5 #####
testes = [((['a','o','c','g','m','p','r'], [3,2,1,1,1,1,2]), 'b'), \
		  (['a',3,'o',2,'c',1,'g',1,'m',1,'p',1,'r',2], 'a'), \
		  ([('a',3),('o',2),('c',1),('g',1),('m',1),('p',1),('r',2)], 'z')]

gabarito = [(['a','o','c','g','m','p','r'], [3,2,1,1,1,1,2]), \
		    ['a',3,'o',2,'c',1,'g',1,'m',1,'p',1,'r',2], \
		    [('a',3),('o',2),('c',1),('g',1),('m',1),('p',1),('r',2)]]

for i in range(len(testes)):
	try:
		signal.alarm(tempo_alarme)
		saida = aluno.exercicio_12_3_5(testes[i][0], testes[i][1])
		signal.alarm(0) # Cancela o alarme

		assert(comparaStrings(saida, gabarito[i], i+1))
		nota_parcial += (1/len(testes)/6)
	except Exception:
		continue

nota_final += nota_parcial

###############

##### 3.6 #####
testes = [((['a','o','c','g','m','p','r'], [3,2,1,1,1,1,2]), [('o', 5),('k', 3)]), \
		  (['a',3,'o',2,'c',1,'g',1,'m',1,'p',1,'r',2], [('g', 9),('z',1)]), \
		  ([('a',3),('o',2),('c',1),('g',1),('m',1),('p',1),('r',2)], [('r', 4),('c',5)])]

gabarito = [(['a','o','c','g','m','p','r'], [3,5,1,1,1,1,2]), \
		  	['a',3,'o',2,'c',1,'g',9,'m',1,'p',1,'r',2], \
		  	[('a',3),('o',2),('c',5),('g',1),('m',1),('p',1),('r',4)]]

for i in range(len(testes)):
	try:
		signal.alarm(tempo_alarme)
		saida = aluno.exercicio_12_3_6(testes[i][0], testes[i][1])
		signal.alarm(0) # Cancela o alarme

		assert(comparaStrings(saida, gabarito[i], i+1))
		nota_parcial += (1/len(testes)/6)
	except Exception:
		continue

nota_final += nota_parcial
###############
#####################################################

################### Exercício 4 #####################
##### 4.1 #####
testes = [(['a','o','c','g','m','p','r'], [3,2,1,1,1,1,2]), \
		  ['a',3,'o',2,'c',1,'g',1,'m',1,'p',1,'r',2], \
		  [('a',3),('o',2),('c',1),('g',1),('m',1),('p',1),('r',2)]]

gabarito = ([('a',3),('o',2)],[('c',1),('g',1),('m',1),('p',1),('r',2)])

for i in range(len(testes)):
	try:
		signal.alarm(tempo_alarme)
		saida = aluno.exercicio_12_4_1(testes[i])
		signal.alarm(0) # Cancela o alarme

		assert(saida == gabarito)
		nota_parcial += (1/len(testes)/6)
	except Exception:
		continue

nota_final += nota_parcial
###############

##### 4.2 #####
testes = [((['a','o','c','g','m','p','r'], [3,2,1,1,1,1,2]), 'a'), \
		  (['a',3,'o',2,'c',1,'g',1,'m',1,'p',1,'r',2], 'a'), \
		  ([('a',3),('o',2),('c',1),('g',1),('m',1),('p',1),('r',2)], 'a')]

gabarito = 3

for i in range(len(testes)):
	try:
		signal.alarm(tempo_alarme)
		saida = aluno.exercicio_12_4_2(testes[i][0], testes[i][1])
		signal.alarm(0) # Cancela o alarme

		assert(saida == gabarito)
		nota_parcial += (1/len(testes)/6)
	except Exception:
		continue

nota_final += nota_parcial
###############

##### 4.3 #####
testes = [((['a','c','g','m','p','r'], [3,1,1,1,1,2]), 'o', -1), \
		  ((['a','o','c','g','m','p','r'], [3,0,1,1,1,1,2]), 'o', 0), \
		  (['a',3,'o',2,'c',1,'m',1,'p',1,'r',2], 'g', -1), \
		  (['a',3,'o',2,'c',1,'g',1,'m',0,'p',1,'r',2], 'm', 0), \
		  ([('o',2),('c',1),('g',1),('m',1),('p',1),('r',2)], 'a', -1), \
		  ([('a',0),('o',2),('c',1),('g',1),('m',1),('p',1),('r',2)], 'o', 0)]

gabarito = [(['a','c','g','m','p','r'], [3,1,1,1,1,2]), \
		    (['a','o','c','g','m','p','r'], [3,0,1,1,1,1,2]), \
		    ['a',3,'o',2,'c',1,'m',1,'p',1,'r',2], \
		    ['a',3,'o',2,'c',1,'g',1,'m',0,'p',1,'r',2], \
		    [('o',2),('c',1),('g',1),('m',1),('p',1),('r',2)], \
		    [('a',0),('o',2),('c',1),('g',1),('m',1),('p',1),('r',2)]]

for i in range(len(testes)):
	try:
		signal.alarm(tempo_alarme)
		saida = aluno.exercicio_12_4_3(testes[i][0], testes[i][1], testes[i][2])
		signal.alarm(0) # Cancela o alarme

		if i in [0,1]:
			assert(comparaStrings(saida, gabarito[i], 1))
		elif i in [2,3]:
			assert(comparaStrings(saida, gabarito[i], 2))
		else:
			assert(comparaStrings(saida, gabarito[i], 3))
		
		nota_parcial += (1/len(testes)/6)
	except Exception:
		continue

nota_final += nota_parcial
###############

##### 4.4 #####
testes = ["programação", "ábcãàó", "quick sort"]

gabarito = 2

for i in range(len(testes)):
	try:
		signal.alarm(tempo_alarme)
		saida = aluno.exercicio_12_4_4(testes[i][0], testes[i][1])
		signal.alarm(0) # Cancela o alarme

		assert(saida == gabarito)
		nota_parcial += (1/len(testes)/6)
	except Exception:
		continue

nota_final += nota_parcial

###############

##### 4.5 #####
testes = [((['a','o','c','g','m','p','r'], [3,2,1,1,1,1,2]), 'b'), \
		  (['a',3,'o',2,'c',1,'g',1,'m',1,'p',1,'r',2], 'a'), \
		  ([('a',3),('o',2),('c',1),('g',1),('m',1),('p',1),('r',2)], 'z')]

gabarito = [(['a','o','c','g','m','p','r'], [3,2,1,1,1,1,2]), \
		    ['a',3,'o',2,'c',1,'g',1,'m',1,'p',1,'r',2], \
		    [('a',3),('o',2),('c',1),('g',1),('m',1),('p',1),('r',2)]]

for i in range(len(testes)):
	try:
		signal.alarm(tempo_alarme)
		saida = aluno.exercicio_12_4_5(testes[i][0], testes[i][1])
		signal.alarm(0) # Cancela o alarme

		assert(comparaStrings(saida, gabarito[i], i+1))
		nota_parcial += (1/len(testes)/6)
	except Exception:
		continue

nota_final += nota_parcial

###############

##### 4.6 #####
testes = [((['a','o','c','g','m','p','r'], [3,2,1,1,1,1,2]), [('o', 5),('k', 3)]), \
		  (['a',3,'o',2,'c',1,'g',1,'m',1,'p',1,'r',2], [('g', 9),('z',1)]), \
		  ([('a',3),('o',2),('c',1),('g',1),('m',1),('p',1),('r',2)], [('r', 4),('c',5)])]

gabarito = [(['a','o','c','g','m','p','r'], [3,5,1,1,1,1,2]), \
		  	['a',3,'o',2,'c',1,'g',9,'m',1,'p',1,'r',2], \
		  	[('a',3),('o',2),('c',5),('g',1),('m',1),('p',1),('r',4)]]

for i in range(len(testes)):
	try:
		signal.alarm(tempo_alarme)
		saida = aluno.exercicio_12_4_6(testes[i][0], testes[i][1])
		signal.alarm(0) # Cancela o alarme

		assert(comparaStrings(saida, gabarito[i], i+1))
		nota_parcial += (1/len(testes)/6)
	except Exception:
		continue

nota_final += nota_parcial
###############
#####################################################

################### Exercício 5 #####################
#####################################################

#####################################################

# Se a nota do aluno for >= 99, arredonda para 100, para o caso de o aluno
# ter acertado todas as questões e haver um erro de precisão no somatório
# das notas parciais
if nota_final >= 99.0:
	nota_final = 100.0

# Imprime a nota final do aluno com 2 casas decimais.
# A nota está no intervalo [0,100]
print("%.2f"%((nota_final/num_questoes)*100))
