def exercicio_1(n):
	return [(i, i**2) for i in range(1,n+1)]

def exercicio_2(n):
	return [(i, i**2, i**3) for i in range(1,n+1)]

def exercicio_3(t):
	return [tuple(t[:int(len(t)/2)]), tuple(t[int(len(t)/2):])]

def exercicio_4(t):
	LP, LI = [], []
	for i in t:
		if i%2 == 0:
			LP.append(i)
		else:
			LI.append(i)
	return [tuple(LP), tuple(LI)]

def exercicio_5(L):
	return tuple(L)

def exercicio_6(L, n):
	for i in range(len(L)):
		lt = list(L[i])
		lt[-1] = n
		L[i] = tuple(lt)
	return L

def exercicio_7(cotacao):
	L = []
	for i in range(1,101):
		L.append((i, i*cotacao))
		L.append((i,i/cotacao))
	return L

def exercicio_8(cotacao):
	s = ''
	for i in range(1,101):
		s += f'US$ {i:6.2f} R$ {i*cotacao:6.2f}   R$ {i:6.2f} US$ {i/cotacao:6.2f}\n--------------------   --------------------\n'
	return s
