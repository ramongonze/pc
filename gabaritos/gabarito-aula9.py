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
# Teste feito no próprio corretor, pois há duas respostas corretas:
# "1 2 3 4 5\n6 7 8 9 10" e "1 2 3 4 5\n6 7 8 9 10\n"
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
	res = []
	for i in range(1,101):
		res.append(((i*cotacao, i), (i, i*cotacao)))

	return res
########################################