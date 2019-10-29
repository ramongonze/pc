def exercicio_12_1(string, n):
	letters = set(string)
	if n == 1:
		ans = [[], []]
		for l in letters:
			ans[0].append(l)
			ans[1].append(string.count(l))
		ans = tuple(ans)
	elif n == 2:
		ans = []
		for l in letters:
			ans += [l, string.count(l)]
	elif n == 3:
		ans = []
		for l in letters:
			ans.append((l, string.count(l)))
	else:
		ans = None

	return ans

def exercicio_12_2(representacao):
	vogais = 'aeiou'
	v, c = 0, 0

	if type(representacao) == type((0,0)):
		for i in range(len(representacao[0])):
			if representacao[0][i] in vogais:
				v += representacao[1][i]
			else:
				c += representacao[1][i]
	elif type(representacao[0]) == type('a'):
		for i in range(0, len(representacao), 2):
			if representacao[i] in vogais:
				v += representacao[i+1]
			else:
				c += representacao[i+1]
	else:
		for l, count in representacao:
			if l in vogais:
				v += count
			else:
				c += count
	return v, c

def exercicio_12_3_1(representacao):
	vogais = 'aeiou'
	ans = [[],[]]

	if type(representacao) == type((0,0)):
		for i in range(len(representacao[0])):
			if representacao[0][i] in vogais:
				ans[0].append((representacao[0][i], representacao[1][i]))
			else:
				ans[1].append((representacao[0][i], representacao[1][i]))
	elif type(representacao[0]) == type('a'):
		for i in range(0, len(representacao), 2):
			if representacao[i] in vogais:
				ans[0].append((representacao[i], representacao[i+1]))
			else:
				ans[1].append((representacao[i], representacao[i+1]))
	else:
		for l, count in representacao:
			if l in vogais:
				ans[0].append((l,count))
			else:
				ans[1].append((l,count))
	ans[0] = sorted(ans[0])
	ans[1] = sorted(ans[1])

	return tuple(ans)

def exercicio_12_3_2(representacao, letra):
	if type(representacao) == type((0,0)):
		if letra not in representacao[0]:
			return None
		else:
			return representacao[1][representacao[0].index(letra)]
	elif type(representacao[0]) == type('a'):
		if letra not in representacao:
			return None
		else:
			return representacao[representacao.index(letra)+1]
	else:
		for l, count in representacao:
			if letra == l:
				return count
		return None

def exercicio_12_3_3(representacao, letra, codigo):
	if codigo not in [0,-1]:
		return None

	if type(representacao) == type((0,0)):
		if letra not in representacao[0]:
			return None
		else:
			if codigo == 0:
				representacao[1][representacao[0].index(letra)] = 0
			else:
				del representacao[1][representacao[0].index(letra)]
				del representacao[0][representacao[0].index(letra)]
	elif type(representacao[0]) == type('a'):
		if letra not in representacao:
			return None
		else:
			del representacao[representacao.index(letra)+1]
			del representacao[representacao.index(letra)]
	else:
		for i in range(len(representacao)):
			if representacao[i][0] == letra:
				del representacao[i]
				return representacao
		return None
	return representacao

def exercicio_12_3_4(string, lista_de_contagens):


def exercicio_12_3_5(representacao, letras):
	if type(representacao) == type((0,0)):
		for l in letras:
			if l in representacao[0]:
				representacao[1][representacao[0].index(l)] += 1
			else:
				representacao[0].append(l)
				representacao[1].append(0)
	elif type(representacao[0]) == type('a'):
		for l in letras:
			if l in representacao:
				representacao[representacao.index(l)+1] += 1
			else:
				representacao.append(l)
				representacao.append(0)
	else:
		for l in letras:
			found = False
			for i in range(len(representacao)):
				if l == representacao[i][0]:
					found = True
					aux = list(representacao[i])
					aux[1] += 1
					representacao[i] = tuple(aux)
			if not found:
				representacao.append((l,0))
	return representacao

def exercicio_12_3_6(representacao, letras):
	