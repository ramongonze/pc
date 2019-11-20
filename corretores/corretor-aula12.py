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
from copy import deepcopy
seed(7)

def signalHandler(signum, frame):
    raise Exception('Timed out!')


# Funções auxiliares
def comparaStrings(s1, s2, tipo):
	"""
		s1: String 1
		s2: String 2
		tipo: Representação 1, 2 ou 3
	"""

	if s1 == None and s2 == None:
		return True
	elif s1 == None and s2 != None:
		return False
	elif s1 != None and s2 == None:
		return False

	if tipo == 1:
		for i in range(len(s1)):
			if s1[1][i] != s2[1][s2.index(s1[0][i])]:
				return False
	elif tipo == 2:
		for i in range(0,len(s1),2):
			if s1[i+1] != s2[s2.index(s1[i])+1]:
				return False
	else:
		return sorted(s1) == sorted(s2)

	return True

def str2Rep(s1, n):
	"""
		Converte uma string para uma representação de string.
		s1: string
		n: {1,2,3} - Número da representação desejada
	"""
	letters = set(s1)
	if n == 1:
		ans = [[], []]
		for l in letters:
			ans[0].append(l)
			ans[1].append(s1.count(l))
		ans = tuple(ans)
	elif n == 2:
		ans = []
		for l in letters:
			ans += [l, s1.count(l)]
	elif n == 3:
		ans = []
		for l in letters:
			ans.append((l, s1.count(l)))
	else:
		ans = None
	return ans

def str2Dic(s1):
	"""
		Transforma uma string em um dicionário com a contagem de cada símbolo.
		s1: string
	"""
	ans = {}
	for c in s1:
		if c not in ans:
			ans[c] = 1
		else:
			ans[c] += 1
	return ans

def ehRepresentacao1(P):
	"""
		Retorna True se P é uma representação de string do tipo 1 ou False caso contrário.
	"""

	if len(P) != 2 or type(P[0]) != type([]) or type(P[1]) != type([]):
		return False

	for i in range(len(P[0])):
		if type(P[0][i]) != type(''):
			return False

	for i in range(len(P[1])):
		if type(P[1][i]) != type(1):
			return False

	return True

################################# Definições ######################################################
signal.signal(signal.SIGALRM, signalHandler)
tempoAlarme = 1 # Quantidade de segundos para executar 1 exercício
notaFinal = 0.0

"""
	A variável 'exercicios' deve ser uma lista de strings com os nomes das funções dos exercícios.
	Ex.: exercicios = ["exercicio_1_1", "exercicio_1_2", "exercicio_2", ...]
"""
exercicios = ['exercicio_12_1', \
			'exercicio_12_2', \
			'exercicio_12_3_1', \
			'exercicio_12_3_2', \
			'exercicio_12_3_3', \
			'exercicio_12_3_4', \
			'exercicio_12_3_5', \
			'exercicio_12_3_6', \
			'exercicio_12_4_1', \
			'exercicio_12_4_2', \
			'exercicio_12_4_3', \
			'exercicio_12_4_4', \
			'exercicio_12_4_5', \
			'exercicio_12_4_6', \
			'exercicio_12_5_1', \
			'exercicio_12_5_2', \
			'exercicio_12_5_3', \
			'exercicio_12_5_4', \
			'exercicio_12_5_5'
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
letras = 'abcdefghijklmnopqrstuvwxyz'
algarismos = '0123456789'
nomes = ['Abcde', 'Bcdef', 'Cdefg', 'Defgh', 'Efghi', 'Fghij', 'Ghijk', 'Hijkl', 'Ijklm', 'Jklmn', 'Klmno', 'Lmnop', 'Mnopq', 'Nopqr', 'Opqrs', 'Pqrst', 'Qrstu', 'Rstuv', 'Stuvw', 'Tuvwx', 'Uvwxy', 'Vwxyz', 'Wxyza', 'Xyzab', 'Yzabc', 'Zabcd']
numeros = ['123456789', '234567890', '345678901', '456789012', '567890123', '678901234', '789012345', '890123456', '901234567', '012345678', '213456789', '324567890', '435678901', '546789012', '657890123', '768901234', '879012345', '980123456', '091234567', '102345678', '321456789', '432567890', '543678901', '654789012', '765890123', '876901234', '987012345', '098123456', '109234567', '210345678', '432156789', '543267890', '654378901', '765489012', '876590123', '987601234', '098712345', '109823456', '210934567', '321045678', '543216789', '654327890', '765438901', '876549012', '987650123', '098761234', '109872345', '210983456', '321094567', '432105678']
agenda = dict([(nomes[i], [numeros[randint(0, len(numeros)-1)]]) for i in range(len(nomes))])
testes = [[(''.join(random.choice(letras) for i in range(randint(1,30))), randint(1,3)) for j in range(20)], \
		  [str2Rep(''.join(random.choice(letras) for i in range(randint(1,30))), randint(1,3)) for j in range(20)], \
		  [str2Rep(''.join(random.choice(letras) for i in range(randint(1,30))), randint(1,3)) for j in range(20)], \
		  [(str2Rep(''.join(random.choice(letras) for i in range(randint(1,30))), randint(1,3)), ''.join(random.choice(letras))) for j in range(20)], \
		  [(str2Rep(''.join(random.choice(letras) for i in range(randint(1,30))), randint(1,3)), ''.join(random.choice(letras)), randint(-1,0)) for j in range(20)], \
		  [(''.join(random.choice(letras) for i in range(randint(1,3))) , str2Rep(''.join(random.choice(letras) for i in range(randint(1,30))), randint(1,3))) for j in range(20)], \
		  [(str2Rep(''.join(random.choice(letras) for i in range(randint(1,30))), randint(1,3)), list(''.join(random.choice(letras) for i in range(randint(1,15))))) for j in range(20)], \
		  [(str2Rep(''.join(random.choice(letras) for i in range(randint(1,30))), randint(1,3)), list(''.join(random.choice(letras) for i in range(randint(1,15))))) for j in range(20)], \
		  [''.join(random.choice(letras) for i in range(randint(1,30))) for j in range(30)], \
		  [(str2Dic(''.join(random.choice(letras) for i in range(randint(1,30)))),''.join(random.choice(letras))) for j in range(30)], \
		  [(str2Dic(''.join(random.choice(letras) for i in range(randint(1,30)))),''.join(random.choice(letras)), randint(-1,0)) for j in range(30)], \
		  [(''.join(random.choice(letras) for i in range(randint(1,3))), str2Dic(''.join(random.choice(letras) for i in range(randint(1,30))))) for j in range(30)], \
		  [(str2Dic(''.join(random.choice(letras) for i in range(randint(1,30)))), list(''.join(random.choice(letras) for i in range(randint(1,3))))) for j in range(30)], \
		  [(str2Dic(''.join(random.choice(letras) for i in range(randint(1,30)))), list(''.join(random.choice(letras) for i in range(randint(1,3))))) for j in range(30)], \
		  [(deepcopy(agenda), ''.join(random.choice(letras) for i in range(randint(1,6))), ''.join(random.choice(algarismos) for i in range(randint(1,6)))) for l in range(30)], \
		  [(deepcopy(agenda), nomes[l], agenda[nomes[l]]) for l in range(10)] + [(deepcopy(agenda), nomes[1], agenda[nomes[1]]), (deepcopy(agenda), nomes[0], 'dsada')], \
		  [(deepcopy(agenda), nomes[0], agenda[nomes[0]][0], 'n1', '131'), (deepcopy(agenda), nomes[0], '', 'n1', ''), (deepcopy(agenda), nomes[1], agenda[nomes[1]][0], '', ''), (deepcopy(agenda), nomes[2], '', 'n1', '131'), (deepcopy(agenda), '', agenda[nomes[3]][0], '', '131'), (deepcopy(agenda), '', agenda[nomes[0]][0], 'n1', '131')], \
		  [deepcopy(agenda)], \
		  [(deepcopy(agenda), (nomes + ['']*10)[randint(0, len(nomes)+9)]) for l in range(30)]
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
			if type(testes[i][j]) != type((0,0)) or ehRepresentacao1(testes[i][j]):
				# A função possui somente 1 parâmetro
				execucaoGabarito = 'saidaGabarito = gabarito.' + exercicios[i] + '('
				if type(testes[i][j]) == type(''):
					execucaoGabarito = execucaoGabarito + "'" + testes[i][j] + "')"
				else:
					execucaoGabarito = execucaoGabarito + str(testes[i][j]) + ")"
				exec(execucaoGabarito)
				
				try:
					execucaoAluno = 'saidaAluno = aluno.' + exercicios[i] + '('
					if type(testes[i][j]) == type(''):
						execucaoAluno = execucaoAluno + "'" + testes[i][j] + "')"
					else:
						execucaoAluno = execucaoAluno + str(testes[i][j]) + ")"
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
					if type(testes[i][j][parametro]) == type(''):
						execucaoGabarito = execucaoGabarito + "'" + testes[i][j][parametro] + "',"
						execucaoAluno 	 = execucaoAluno    + "'" + testes[i][j][parametro] + "',"
					else:
						execucaoGabarito = execucaoGabarito + str(testes[i][j][parametro]) + ','
						execucaoAluno 	 = execucaoAluno    + str(testes[i][j][parametro]) + ','

				execucaoGabarito = execucaoGabarito[:-1] + ')' # Substitui a última vírgula por ')'
				execucaoAluno 	 = execucaoAluno[:-1] + ')' # Substitui a última vírgula por ')'
				exec(execucaoGabarito)

				try:
					signal.alarm(tempoAlarme) # Ativa o alarme
					exec(execucaoAluno)
					signal.alarm(0) # Cancela o alarme

					if exercicios[i] == 'exercicio_12_3_4' or exercicios[i] == 'exercicio_12_3_5'\
					or exercicios[i] == 'exercicio_12_3_6':
						assert(comparaStrings(str2Rep(saidaAluno, 3), str2Rep(saidaGabarito, 3),3))
					else:
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
if notaFinal >= 0.95:
	notaFinal = 1.0

if erros == '':
	# O aluno não obteve nota zero em nenhum exercício
	print('0', end='#')
else:
	print(erros[:-1], end='#')

# Imprime a nota final do aluno com 4 casas decimais.
# A nota está no intervalo [0,1]
print('%.2f'%notaFinal)
