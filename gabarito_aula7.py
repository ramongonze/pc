def ex_1():
	n = int(input("Módulo: "))
	cur = 0
	print(cur)

	while input("Quer continuar? (S ou N) ") == 'S':
		cur = (cur+1)%n
		print(cur)
	print("Fim")

def ex_2():
	SUM = 0
	n = int(input())
	for i in range(n+1):
		SUM += i
	print()