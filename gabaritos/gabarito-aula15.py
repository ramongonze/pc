# Questão 1
def exercicio_8_6(L1, L2):
	L1S = set(L1)
	L2S = set(L2)
	if len(L1S.intersection(L2S)) > 0:
		return True
	return False

# Questão 2
def exercicio_14_3_9(ini, fim):
	D = dict()
	for i in range(ini, fim+1):
		for div in range(9,0,-1):
			if i%div == 0:
				D[i] = div
				break
	return D

# Questão 3
def exercicio_14_0(ini, fim):
	d = {x:y for x in range(ini, fim)
             for y in [max([a for a in range(1,10) if x % a == 0])]
              if y == 1 or y == x and y != 4 and y != 6 and y != 8 and y != 9}
	return [k for k,_ in d.items()]

# Questão 4
def exercicio_12_0(nome_do_arquivo):
	f = open(nome_do_arquivo)
	frequencias = dict()
	media = 0
	for linha in f:
		frase = linha.split(' ')
		for palavra in frase:
			palavra = palavra.replace('\n', '')
			if palavra not in frequencias:
				frequencias[palavra] = 1
			else:
				frequencias[palavra] += 1
	f.close()
	
	mais_frequentes = sorted([(y,x) for x,y in frequencias.items()], reverse=True)

	# Calcula a média de tamanho das 10 palavras mais frequentes
	# Se houver menos que 10 palavras no arquivo, olha a media de todas as palavras
	media_tamanho = 0
	if len(mais_frequentes) >= 10:
		for _, palavra in mais_frequentes[:10]:
			media_tamanho += len(palavra)
		media_tamanho /= 10
		mais_frequentes = [p for _,p in mais_frequentes[:10]]
	else:
		for _, palavra in mais_frequentes:
			media_tamanho += len(palavra)
		media_tamanho /= len(mais_frequentes)
		mais_frequentes = [p for _,p in mais_frequentes]

	# Linha do texto onde ocorre as 10 palavras mais frequentes
	f = open(nome_do_arquivo)
	linhas = []
	count = 1
	contabilizada = []
	for linha in f:
		frase = linha.split(' ')
		for palavra in frase:
			palavra = palavra.replace('\n', '')
			if palavra in mais_frequentes and palavra not in contabilizada:
				linhas.append(count)
				contabilizada.append(palavra)
		count += 1
	f.close()

	return frequencias, media_tamanho, linhas

# Questão 5
def exercicio_5_1_1(n, i):
    if n == 0 or n == 1:
        return 1
    return n * exercicio_5_1_1(n-1, i)

# Questão 6 recursiva
def exercicio_7_6_1(n):
	s = 0

	for i in range(1,n+1):
		s += ((2*i-1)/i)

	return s

# Questão 6 iterativa
def exercicio_7_6_2(n):
	return exercicio_7_6_1(n)

# Questão 7
def exercicio_6_3(string):
	return string == string[::-1]

# Questão 8
def exercicio_9_1(n):
	return [(i, i**2, i**3) for i in range(1,n+1)]

# Questão 9
def exercicio_4_6(n1,n2,n3):
	L = sorted([n1,n2,n3], reverse=True)
	for i in L:
		if i%2 == 1:
			return i
	return None
