def exercicio_1(data):
	meses = [1, 'janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', \
	'setembro', 'outubro', 'novembro', 'dezembro']

	tokens = data.split('/')
	return tokens[0] + ' de ' + meses[int(tokens[1])] + ' de ' + tokens[2]

def exercicio_2(frase):
	vogais = 'aeiouAEIOU'
	consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
	pontuacao = '?!.,;:'
	ans = []
	ans.append([(' ', frase.count(' '))])
	for p in [vogais, consoantes, pontuacao]:
		l = []
		for c in p:
			n = frase.count(c)
			if n > 0:
				l.append((c, n))
		ans.append(l)
	return tuple(ans)

def exercicio_3(cpf):
	tokens = cpf.split('.')

	if len(tokens) != 3:
		return None

	t2 = tokens[-1].split('-')

	if len(t2) != 2:
		return None

	cpf = tokens[0] + tokens[1] + t2[0] + t2[1]

	if len(cpf) != 11:
		return None

	# Verifica se todos os algaristmos são iguais
	if cpf.count(cpf[0]) == len(cpf):
		return False

	# 1 digito verificador
	valido = True
	s = 0
	for i in range(9):
		s += (int(cpf[i]) * (10-i))
	r = s%11
	j = int(cpf[-2])

	if (r == 0 or r == 1) and j != 0:
		return False
	elif r in range(2,11) and j != 11-r:
		return False

	# 2 digito verificador
	s = 0
	for i in range(9):
		s += (int(cpf[i]) * (11-i))
	s += (2*j)
	r = s%11
	k = int(cpf[-1])

	if (r == 0 or r == 1) and k != 0:
		return 	False
	elif r in range(2,11) and k != 11-r:
		return False

	return True

def exercicio_4(n):
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

def exercicio_5_1():
	ans = ''
	for i in range(2,10):
		for j in range(1,10):
			ans += ('%d x %d = %d\t'%(i,j,i*j))
		ans = ans[:-1] + '\n'
	return ans

def exercicio_5_2():
	ans = ''
	for i in range(1,21):
		ans += ('{0:>7}{1:>7}{2:>7}{3:>7}\n'.format(i,i**2,i**3,i**4))
	return ans

def exercicio_5_3(n):
	t = [[1]]
	for i in range(2,n+1):
		l = [1]
		for j in range(1,i-1):
			l += [t[i-2][j-1] + t[i-2][j]]
		l += [1]
		t += [l]
	triangulo = ('\t' * (n-1)) + '1\n'
	for i in range(2,n+1):
		triangulo = triangulo + ('\t' * (n-i)) + '1'
		for j in range(1,len(t[i-1])):
			triangulo = triangulo + '\t\t' + str(t[i-1][j])
		triangulo += '\n'
	return triangulo[:-1]