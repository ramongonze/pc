def exercicio_1(L):
	return sum(L)

def exercicio_2(L):
	return sum(L)/len(L)

def exercicio_3(L):
	if len(L) == 0:
		return None, None

	return min(L), max(L)

def exercicio_4(L):
	ans = 0
	for i in L:
		if len(i) >= 2 and i[0] == i[-1]:
			ans += 1
	return ans

def exercicio_5(L):
	return L

def exercicio_6(L1,L2):
	L1S = set(L1)
	L2S = set(L2)
	if len(L1S.intersection(L2S)) > 0:
		return True
	return False

def exercicio_7(linhas):
	triangle = ''
	for i in range(linhas):
		spaces = (2*linhas-1-(2*i+1))/2
		
		for j in range(int(spaces)):
			triangle += ' '		
		for j in range(2*i+1):
			triangle += '*'

		triangle += '\n'
	return triangle

def exercicio_8(linhas):
	triangle = ''
	for i in range(linhas-1,-1,-1):
		spaces = (2*linhas-1-(2*i+1))/2
		
		for j in range(int(spaces)):
			triangle += ' '		
		for j in range(2*i+1):
			triangle += '*'
		
		triangle += '\n'
	return triangle
