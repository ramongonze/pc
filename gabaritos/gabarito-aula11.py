# Exercício 1
def exercicio_11_1(data):
	meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', \
	'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

	l = data.split('/')
	ans = "Você nasceu em %02d de %s de %s."%(int(l[0]), meses[int(l[1])-1], l[2])

	return ans
########################################

# Exercício 2
def exercicio_11_2(s):
	ans = [0,0,0,0]
	ans[0] = s.count(" ")
	
	sum_ = 0
	for v in "aeiou":
		sum_ += s.count(v)
	ans[1] = sum_

	l = []
	for c in "bcdfghjklmnpqrstvwxyz":
		if s.count(c) > 0:
			l.append((c, s.count(c)))
	ans[2] = l	
	
	l = []
	for c in ".,;?!":
		if s.count(c) > 0:
			l.append((c, s.count(c)))
	ans[3] = l	

	return tuple(ans)

########################################

# Exercício 3
def exercicio_11_3(cpf):
	tokens = cpf.split('.')
	if len(tokens) != 3:
		return None

	end_ = tokens[-1].split('-')
	if len(end_) != 2:
		return None

	cpf = tokens[0] + tokens[1] + end_[0]
	try:
		digitos9 = [int(x) for x in cpf]
		digVerificador1 = int(end_[1][0])
		digVerificador2 = int(end_[1][1])
	except:
		return False

	L = [10,9,8,7,6,5,4,3,2]
	sum_ = 0
	for i in range(len(L)):
		sum_ += (digitos9[i]*L[i])

	if (sum_*10) % 11 != digVerificador1:
		return False

	L = [11] + L
	digitos9 = digitos9 + [digVerificador1]

	sum_ = 0
	for i in range(len(L)):
		sum_ += (digitos9[i]*L[i])

	if (sum_*10) % 11 != digVerificador2:
		return False

	# Verifica se todos os dígitos são iguais
	if digitos9.count(digitos9[0]) == len(digitos9) and digitos9[0] == digVerificador2:
		return False

	return True
########################################

# Exercício 4
def exercicio_11_4(n):
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
########################################

# Exercício 5.1
def exercicio_11_5_1_1():
	ans = ""

	for i in range(2,10):
		ans += ("%d x 1 = %d"%(i, i))
		for j in range(2,10):
			ans += ("\t" + "%d x %d = %d"%(i,j,i*j))
		ans += '\n'

	return ans

def exercicio_11_5_1_2():
	ans = ""

	for i in range(2,10):
		ans += ("%d x 1 = %d"%(i, i))
		for j in range(2,10):
			ans += ("\t" + "%d x %d = %d"%(i,j,i*j))
		ans += '\n'

	return ans
########################################

# Exercício 5.2
def exercicio_11_5_2_1():
	ans = ""
	for i in range(1,21):
		ans += ("{0:10}{1:10}{2:10}{3:10}\n".format(i,i**2,i**3,i**4))
	return ans

def exercicio_11_5_2_2():
	ans = ""
	for i in range(1,21):
		ans += ("{0:10}{1:10}{2:10}{3:10}".format(i,i**2,i**3,i**4))
	return ans
########################################

# Exercício 5.3
def exercicio_11_5_3_1(n):
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

def exercicio_11_5_3_2(n):
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
########################################