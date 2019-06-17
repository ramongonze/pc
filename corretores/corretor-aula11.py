"""
	Corretor automático para os exercícios da aula 11.
	
	Entradas (linha de comando):
		- argv[1] = Caminho completo do arquivo do aluno (um arquivo .py).
		
		OBS.: - Deve ser passado somente o nome do arquivo, sem a extensão .py.
	    Exemplo:
	    	- Arquivo do aluno: "alunos/joao.py"

		Execução do script:
		$ python3 correor-aula11.py alunos/joao

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
num_questoes = 5 # Número de exercícios da aula
nota_final = 0.0
#####################################################

# Try-catch usado para verificar se há erro de sintaxe no arquivo do aluno
try:
	aluno = __import__(sys.argv[1])
except:
	print("Erro ao importar o arquivo do aluno.	")

################### Exercício 1 #####################
nota_parcial = 0.0
testes = ["01/01/2010",\
		  "09/12/2000",\
		  "29/10/1973",\
		  "10/02/1998"]

gabarito = ["Você nasceu em 01 de Janeiro de 2010.",\
		    "Você nasceu em 09 de Dezembro de 2000.",\
		    "Você nasceu em 29 de Outubro de 1973.",\
		    "Você nasceu em 10 de Fevereiro de 1998."]

for i in range(len(testes)):
	try:
		signal.alarm(tempo_alarme)
		saida = aluno.exercicio_11_1(testes[i])
		signal.alarm(0) # Cancela o alarme

		assert(gabarito[i] == saida)
		nota_parcial += (1/len(testes))
	except Exception:
		continue

nota_final += nota_parcial
#####################################################

################### Exercício 2 #####################
nota_parcial = 0.0
testes = ["ola mundo!",\
		  "branco bagre, bagre branco...",\
		  "exercicio !@  ",\
		  "aaaeioobxyy  .!,"]

gabarito = [(1, 4, [('d', 1), ('l', 1), ('m', 1), ('n', 1)], [('!', 1)]), \
		    (3, 8, [('b', 4), ('c', 2), ('g', 2), ('n', 2), ('r', 4)],
			[('.', 3), (',', 1)]), \
		    (3, 5, [('c', 2), ('r', 1), ('x', 1)], [('!', 1)]), \
		    (2, 7, [('b', 1), ('x', 1), ('y', 2)], [('.', 1), (',', 1), \
		    ('!', 1)])]

for i in range(len(testes)):
	try:
		signal.alarm(tempo_alarme)
		saida = aluno.exercicio_11_2(testes[i])
		signal.alarm(0) # Cancela o alarme

		assert(saida[0] == gabarito[i][0] and\
			   saida[1] == gabarito[i][1] and\
			   sorted(saida[2]) == sorted(gabarito[i][2]) and\
			   sorted(saida[3]) == sorted(gabarito[i][3]))

		nota_parcial += (1/len(testes))
	except Exception:
		continue

nota_final += nota_parcial
#####################################################

################### Exercício 3 #####################
testes = ["123.456.789-12",\
		  "147.895.685-98",\
		  "123.456789.12",\
		  "01234567890",\
		  "111.111.111-11",\
		  "328.265.015-93"]

gabarito = [False, False, None, None, False, True]

nota_parcial = 0.0
for i in range(len(testes)):
	try:
		signal.alarm(tempo_alarme)
		saida = aluno.exercicio_11_3(testes[i])
		signal.alarm(0) # Cancela o alarme

		assert(saida == gabarito[i])

		nota_parcial += (1/len(testes))
	except Exception:
		continue

nota_final += nota_parcial
#####################################################

################### Exercício 4 #####################
def gabarito_11_4(n):
	algarismos = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
	menor20 = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
	dezenas = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']

	if n <= 9:
		ans = algarismos[n]
	elif 10 <= n <= 19:
		ans = menor20[n-10]
	elif n == 100:
		ans = 'cem'
	else:
		nStr = str(n)
		ans = dezenas[int(nStr[0])-2]

		if n%10 != 0:
			ans = ans + " e " + algarismos[int(nStr[1])]

	return ans

testes = list(range(0,101))
nota_parcial = 0.0
for i in range(len(testes)):
	try:
		signal.alarm(tempo_alarme)
		saida = aluno.exercicio_11_4(i)
		signal.alarm(0) # Cancela o alarme
		
		assert(saida == gabarito_11_4(i))

		nota_parcial += (1/len(testes))
	except Exception:
		continue

nota_final += nota_parcial
#####################################################

################### Exercício 5 #####################
def gabarito_11_5_1():
	ans = ""

	for i in range(2,10):
		ans += ("%d x 1 = %d"%(i, i))
		for j in range(2,10):
			ans += ("\t" + "%d x %d = %d"%(i,j,i*j))
		ans += '\n'

	return ans

def gabarito_11_5_2():
	ans = ""
	for i in range(1,21):
		ans += ("{0:10}{1:10}{2:10}{3:10}\n".format(i,i**2,i**3,i**4))
	return ans

def gabarito_11_5_3(n):
	triangle = [[1], [1,1]]
	ans = ""

	for line in range(3,n+1):
		triangle.append([1] * line)

		for e in range(2,line):
			triangle[line-1][e-1] = triangle[line-2][e-2] + triangle[line-2][e-1]

	# Print triangulo
	for i in range(len(triangle)):
		ans += ("\t" * (n-i))
		for j in range(len(triangle[i])):
			if j == 0:
				ans += ("%d"%triangle[i][j])
			else:
				ans += ("\t\t%d"%triangle[i][j])
		ans += "\n"

	return ans

def strToList(s):
	temp = []
	for i in s:
		try:
			temp.append(int(i))
		except:
			continue

	return temp

nota_parcial = 0.0

########### 5.1 e 5.2 #############
for ex in [1,2]:
	for tipo in [1,2]:
		try:
			signal.alarm(tempo_alarme)
			exec('saida = strToList(list(aluno.exercicio_11_5_%d_%d()))'\
				%(ex, tipo))
			signal.alarm(0) # Cancela o alarme	
			exec('gabarito = strToList(list(gabarito_11_5_%d()))'%(ex))

			assert(saida == gabarito)
			nota_parcial += (1/3/2)
		except Exception:
			continue
###################################

############## 5.3 ################
testes = list(range(3,20))
for i in range(len(testes)):
	for tipo in [1,2]:
		try:
			signal.alarm(tempo_alarme)
			exec('saida = strToList(list(aluno.exercicio_11_5_3_%d(i)))'\
				%(tipo))
			signal.alarm(0) # Cancela o alarme	
			exec('gabarito = strToList(list(gabarito_11_5_3(i)))')

			assert(saida == gabarito)
			nota_parcial += (1/3/2/17)
		except Exception:
			continue

nota_final += nota_parcial
###################################

#####################################################

# Se a nota do aluno for >= 99, arredonda para 100, para o caso de o aluno
# ter acertado todas as questões e haver um erro de precisão no somatório
# das notas parciais
if nota_final >= 99.0:
	nota_final = 100.0

# Imprime a nota final do aluno com 2 casas decimais.
# A nota está no intervalo [0,100]
print("%.2f"%((nota_final/num_questoes)*100))
