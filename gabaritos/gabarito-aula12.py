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

def exercicio_12_3_4(simbolos, representacao):
	ans = []

	if type(representacao) == type((0,0)):
		for s in simbolos:
			if s in representacao[0]:
				ans.append((s,representacao[1][representacao[0].index(s)]))
	elif type(representacao[0]) == type('a'):
		for s in simbolos:
			if s in representacao:
				ans.append((s,representacao[representacao.index(s)+1]))
	else:
		for letra, count in representacao:
			if letra in simbolos:
				ans.append((s,count))

	return sorted(ans)

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
	ans = []

	if type(representacao) == type((0,0)):
		for s in simbolos:
			if s in representacao[0]:
				ans.append((s,representacao[1][representacao[0].index(s)]))
	elif type(representacao[0]) == type('a'):
		for s in simbolos:
			if s in representacao:
				ans.append((s,representacao[representacao.index(s)+1]))
	else:
		for letra, count in representacao:
			if letra in simbolos:
				ans.append((s,count))

	if ans == []:
		return None

	return sorted(ans)

def exercicio_12_4_1(string):
	vogais = 'aeiou'
	ans = [[],[]]
	d = {}
	for letra in string:
		if letra in d:
			d[letra] += 1
		else:
			d[letra] = 1
	for letra in d:
		if letra in vogais:
			ans[0].append((letra, string.count(letra)))
		else:
			ans[1].append((letra, string.count(letra)))
	ans[0] = sorted(ans[0])
	ans[1] = sorted(ans[1])
	return tuple(ans)

def exercicio_12_4_2(dicionario,letra):
	if letra not in dicionario:
		return None
	else:
		return dicionario[letra]	

def exercicio_12_4_3(dicionario,letra,codigo):
	if letra not in dicionario:
		return None

	if codigo == 0:
		dicionario[letra] = 0
	else codigo == -1:
		del dicionario[letra]
	else:
		return None

	return dicionario


def exercicio_12_4_4(string,dicionario):
	ans = {}
	for letra in string:
		if letra in dicionario:
			ans[letra] = dicionario[letra]

	return ans

def exercicio_12_4_5(dicionario,letras):
	for l in letras:
		if l not in dicionario:
			dicionario[l] = 0
		else:
			dicionario[l] += 1
	return dicionario

def exercicio_12_4_6(dicionario,letras):
	noLetter = False

	for l in letras:
		if l in dicionario:
			dicionario[l] += 1
			noLetter = True

	if not noLetter:
		return None
	else:
		return dicionario

def exercicio_12_5_1(agenda, nome, numero):
	if nome == '' or numero == '':
		return agenda

	agenda[nome].append(numero)

	return agenda

def exercicio_12_5_2(agenda, nome, numero):
	if nome == '' and numero == '':
		return None
	elif nome == '' and numero != '':
		count = 0
		for pessoa in agenda:
			if numero in agenda[pessoa]:
				agenda[pessoa].remove(numero)
				if agenda[pessoa] == []:
					del agenda[pessoa]
				count += 1
		
		if count == 0:
			return None

	elif nome != '' and numero == '':
		if nome in agenda:
			agenda[nome] = []
		else:
			return None
	else:
		if nome in agenda and numero in agenda[nome]:
			agenda[nome].remove(numero)
		else:
			return None

	return agenda

def exercicio_12_5_3(agenda, nome1, numero1, nome2, numero2):
	if nome1 != '' and numero1 != '' and nome2 != '' and numero2 != '':
		agenda[nome1].remove(numero1)
		agenda[nome1].append(numero2)
		agenda[nome2] = agenda[nome1]
		del agenda[nome1]

	elif nome1 != '' and numero1 == '' and nome2 != '' and numero2 == '':
		agenda[nome2] = agenda[nome1]
		del agenda[nome1]

	elif nome1 != '' and numero1 != '' and nome2 == '' and numero2 != '':
		agenda[nome1].remove(numero1)
		agenda[nome2].append(numero2)

	elif nome1 != '' and numero1 == '' and nome2 != '' and numero2 != '':
		del agenda[nome1]
		agenda[nome2] = [numero2]

	elif nome1 == '' and numero1 != '' and nome2 == '' and numero2 != '':
		for pessoa in agenda:
			if numero1 in agenda[pessoa]:
				agenda[pessoa].remove(numero1)
				agenda[pessoa].append(numero2)

	elif nome1 == '' and numero1 != '' and nome2 != '' and numero2 != '':
		agenda[nome2] = [numero1, numero2]

	else:
		return None

	return agenda

def exercicio_12_5_4(agenda):
	ans = ''

	for pessoa in agenda:
		ans = pessoa + ': '
		for telefone in agenda[pessoa]:
			ans = ans + telefone + '; '
		ans += '\n'
	
	return ans

def exercicio_12_5_5(agenda, nome):
	if nome not in agenda:
		return None

	ans = nome + ': '
	for telefone in agenda[nome]:
		ans = ans + telefone + '; '
	ans += '\n'

	return ans
