def exercicio_1(n):
	r = 0

	cont = 'S'

	while(cont == 'S'):
		print(r)
		cont = input('Quer continuar? (S ou N): ')
		r = (r+1)%n
	print('Fim')

def exercicio_2_1(n):
	s = 0
	for i in range(n+1):
		s += i
	return s

def exercicio_2_2(n):
	return exercicio_2_1(n)

def exercicio_3_1(n):
	sP, sI = 0, 0

	for i in range(n+1):
		if i%2 == 0:
			sP += i
		else:
			sI += i

	return (sP, sI)

def exercicio_3_2(n):
	return exercicio_3_1(n)

def exercicio_4(n):
	divisores = []

	for i in range(1,n+1):
		if n%i == 0:
			divisores.append(i)

	return divisores

def exercicio_5(t):
	if len(t) == 0:
		return None, None

	return min(t), max(t)

def exercicio_6_1():
	s = 0

	for i in range(1,51):
		s += ((2*i-1)/i)

	return s

def exercicio_6_2():
	return exercicio_6_1()

def exercicio_7_1(n):
	s = 0

	for i in range(1,n):
		s += ((2*i-1)/i)

	return s

def exercicio_7_2(n):
	return exercicio_7_1(n)

def exercicio_8_1(a, b):
	L = []
	while a <= b:
		a += 1
		if a == 5:
			break
		L.append(a)
	return L

def exercicio_8_2(a, b):
	return exercicio_8_1(a, b)

def exercicio_8_3(a, b):
	L = [a]
	while a <= b:
		a += 1
		if a == 5:
			break
		L.append(a)
	L.append(a)
	return L
