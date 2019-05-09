# Exercício 1
def exercicio_1(n):
	res = []
	for i in range(1, n+1):
		res.append((i, i*i))
	return res
########################################

# Exercício 2
def exercicio_2(n):
	res = []
	for i in range(1, n+1):
		res.append((i, i*i, i*i*i))
	return res
########################################

# Exercício 3
def exercicio_3(t):
	ans = ""
	for i in range(int(len(t)/2)):
		ans = ans + str(t[i]) + " "
	ans = ans[:-1] + '\n' # Troca o útlimo espaço por \n
	
	for i in range(int((len(t)/2)), len(t)):
		ans = ans + str(t[i]) + " "
	ans = ans[:-1] + '\n' # Troca o útlimo espaço por \n
	
	return ans

########################################

# Exercício 4
def exercicio_4(t):
	t_par = []
	t_impar = []
	for i in t:
		if i%2 == 0:
			t_par.append(i)
		else:
			t_impar.append(i)

	t_par = sorted(t_par)
	t_impar = sorted(t_impar)

	return tuple(t_par), tuple(t_impar)
########################################

# Exercício 5
def exercicio_5_1(l):
	return tuple(l)

def exercicio_5_2(l):
	return tuple(l)
########################################

# Exercício 6
def exercicio_6(l, n):
	for i in range(len(l)):
		lista = list(l[i])
		lista[-1] = n
		l[i] = tuple(lista)

	return l
########################################

# Exercício 7
def exercicio_7(cotacao):
	s = ''
	
	for i in range(1,101):
		s += f'US$ {i:6.2f} R$ {i*cotacao:6.2f}   R$ {i:6.2f} US$ {i/cotacao:6.2f}\n--------------------   --------------------\n'
	
	return s
########################################