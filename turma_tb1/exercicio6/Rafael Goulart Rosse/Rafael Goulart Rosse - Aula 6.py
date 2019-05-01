#!/usr/bin/env python
# coding: utf-8

# # Aula 5 - Exercícios

# # Questão 1

# In[25]:


def exercício_1(n):
    condicao_de_parada = y
    resultado = 0
    if n >= 0:
        resultado = 1
    while (n>1 and n<=y):
        resultado = resultado * n
        n = n -1
    return resultado


# # Questão 2

# In[74]:


def exercício_2(n,sinal):
    "Esse programa corresponde ao somatório de n termos com uma razão de 1/k multiplicado por -1 elevado a k+1.    definimos o resultado para n sendo 1 e depois indicamos a fórmula."
    if n == 1:
        resultado = 1
    else:
        sinal = -1**n
        resultado = ((1/n) * sinal + exercício_2(n-1,sinal))
    return resultado


# # Questão 3

# In[21]:


def exercício_3_1(termos,denom):
    if (termos == 1):
        resultado = denom
    else:
        resultado = denom + 1/exercício_3_1(termos-1,denom+4)
    return resultado

termos = 4
denom = 1

def exercício_3_2(termos,denom):
    import math
    resultado = math.inf
    denom = 6 + (termos-1) * 4
    while (termos > 0):
        resultado = denom + 1/resultado
        termos = termos - 1
        denom = denom - 4
    return resultado

termos = 4
denom = 1

