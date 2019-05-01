#!/usr/bin/env python
# coding: utf-8

# ## Exercício 1

# In[1]:


def exercicio_1_1(p,n):
#Essa função calcula fatorial recursivamente
    if p<=n:
        resultado=p*exercicio_1_1(p+1,n)
    else:
        resultado=1
    if n<0:
        return 'Número não admitido para essa função' 
    return resultado

#n=int(input('Digite um valor do qual deseja calcular o fatorial: '))
#print(exercicio_1_1(1,n))

def exercicio_1_2(p,n):
#Essa função calcula fatorial iterativamente
    if n < 0:
        resultado=0
    elif n==0:
        resultado=1
    else:
        resultado=1
        while True:
            resultado=resultado*p
            p=p+1
            if n<p:
                break
    return resultado
#n = int(input("Entre com n: "))
#print("O fatorial de %d é %d" %(n,exercicio_1_2(1,n)))


# ## Exercício 2

# Atribui resultado inicial como 0, faz a soma do termo n reduzindo 1 em 1 até n==1, pois 0 no denominador não é definido.
# Adiciona uma outra variável 's' para representar o sinal, insere-se o sinal do primeiro termo, e multiplica por (-1) a cada
# operação.

# In[9]:


def exercicio_2(s,n):
#Essa função calcula o somatório da série alternada
    resultado = 0
    while n>0:
        resultado=1/n*s + resultado
        n=n-1
        s=s*(-1)
    return resultado

#n= int(input("Entre com n: "))
#s= int(input('Entre com o 1 ou -1 para o sinal do primeiro termo: '))
#print("A soma até o termo da posição %d é %f" %(n,exercicio_2(s,n)))


# ## Exercício 3

# ### Recursivo

# No programa recursivo, deve-se entrar com número de termos igual a 6, para que haja 4 termos na função homogênea.
# Sendo assim, o programa leria que termos >= 3 e daria e como, 1+2/(1+1/"chama a função neper_homogêneo(termos-1,denom+4"), até que termos seja igual a 1, que é o comando de parada.
# 
# Isto é a parte fixa: e=1+2/(1+/ ... com as chamadas da parte homogênea: ...  6+1/ (10+1/ (14+1/ 18))
# Sendo assim, e = 2.718281828735696

# ### Iterativo

# O programa iterativo faz o caminho contrário, ele começa a soma a partir do último termo. Para que os 4 termos da parte homogênea sejam calculados, é necessário que o número de termos seja igual a 6, asim como no exercício anterior. Então calculamos a parte homogênea. O cálculo vai continuar até que ele sai do while, o que acontece quando termos = 0. O resultado inicialmente é infinito e o denominador recebe 6+(termos-1)*4
# 
# Isto é a parte fixa: e=1+2/(1+/ ... acrescido do resultado da parte homogênea, que é contade de trás para frente, logo:
# Parte homogênea:
# 
# res= 6+(4-1)*4  + 1/infinito = 18
# termos= 4-1=3
# denom=18-4=14
# .
# .
# .
# res= 14 + 1/18
# termos=3-1=2
# denom=14-4=10
# .
# .
# .
# res= 10 + 1/ (14+1/18)
# termos=2-1=1
# denom=10-4=6
# .
# .
# .
# res= 6 + 1/(10+1/(14+1/18))
# termos=1-1=0
# denom=6-4=2
# 
# Termos agora é igual a zero, o que me leva para fora do while e retorna res = 6 + 1/(10+1/(14+1/18))
# Então e= 1+2/(1+/ 6 + 1/(10+1/(14+1/18)))
# 

# In[60]:


def neper(termos):
    if (termos == 1):
        e = 1
    elif (termos == 2):
        e = 1+2/1
    else: # termos >= 3
        e = 1+2/(1 + 1/neper_homI(4,denom))
    return e

def neper_homI(termos,denom):
    import math
    res = math.inf
    denom = 6+(termos-1)*4
    while (termos > 0):
        res = denom + 1/res
        termos = termos - 1
        denom = denom - 4
    return res
print (neper(6))


# In[ ]:




