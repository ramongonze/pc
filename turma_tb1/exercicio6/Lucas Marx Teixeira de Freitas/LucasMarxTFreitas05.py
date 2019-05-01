#!/usr/bin/env python
# coding: utf-8

# Lucas Marx T. Freitas 2018015570 

# Exercicio 1

# #programa recursivo para calcular o fatorial (não modificado)
# def fatorial(n):
#     resultado = 0
#     if n >= 0:
#         if n == 0:
#             resultado = 1
#         else:
#             resultado = n*fatorial(n-1)
#         return resultado
# 
# #programa iterativo para calcular o fatorial (não modificado)
# def fatorial(n):
#     resultado = 0
#     if n >= 0:
#         resultado = 1
#         while (n > 1):
#             resultado = resultado * n
#             n = n - 1
#     return resultado
# 

# In[ ]:


#programa recursivo refeito 
def fatorial(n):
    result = 0
    if n >= 0:
        if n == 0:
            result = 1
    else:
        result = (n - (n - 1))*fatorial(n + 1)  #"A chamada recursiva irá aumentar o argumento do termo em vez de diminuir."
        while result == n:       #"O caso de base agora muda para testar se o termo é igual ao argumento n, o natural cujo fatorial se quer calcular."
            break 
    return result

#programa iterativo refeito
def fatorial(n):
    result = 0
    if n >= 0 or n >= 1:
        result = 1
        while (n > 1):
            result = result * (n - (n -1))
            n = n + 1
    return result


# Exercicio 2

# In[ ]:


#programa recursivo para calcular a função harmônica (modificado apenas para calcular a função harmônica com sinais alterados)
def harmonicaR(n):
    if n >= 1 or n <= -1:
        if n == 1:
            resultado = 1
        if n == -1:
            resultado = -1
        if n > 1:
            resultado = 1/n + harmonicaR(n-1)*(-1) # sendo um valor positivo, a primeira iteração será (-1) , a segunda, (1) e assim por diante.
        if n < -1:
            resultado = 1/n + harmonicaR(n-1)*(-1)*(-1)  # sendo um valor negativo, a primeira iteração será (1) , a segunda, (-1) e assim por diante.
        return resultado


# Exercicio 3

# In[ ]:


import math
math.e


# Exercicio 4

# In[8]:


#exercicio_4_1_1
import math

def neper_homI(term,denom): 
    result = math.inf 
    while (term = 1**1/2): 
        result = denom + 1**1/2 
        term = term + denom
    return result

#exercicio_4_1_2
def neper_homR(term,denom):
    if (term == 1**1/2):
        result = denom + neper_homR(termos + 1**1/2, denom) 
    return result
#############################################

exercicio_4_2_1

#exercicio_4_2_2
def neper_homR(term,denom): 
    result = 1
    if term = n 
        result = + 1/(n-1)
    return result

#############################################

exercicio_4_3_1

exercicio_4_3_2

#############################################

exercicio_4_4_1

exercicio_4_4_2

#############################################

exercicio_4_5_1

exercicio_4_5_2

#############################################

exercicio_4_6_1

exercicio_4_6_2

#############################################

#exercicio_4_7_1
import math 
def neper_homI(term,denom): 
    import math
    if term = 0
        result = 0
    if term = 1
        result = 1
    while (term > 1): 
        result = math.inf
        term = denom(term − 1) + denom(term − 2)
        denom = denom 
    return result

#exercicio_4_7_2
def neper_homR(term,denom): 
    if term = 0
        result = 0
    if term = 1
        result = 1
    else: 
        result = denom(term − 1) + denom(term − 2)
    return result

#############################################

exercicio_4_8_1

exercicio_4_8_2

#############################################

exercicio_4_9_1

exercicio_4_9_2

#############################################

exercicio_4_10_1

exercicio_4_10_2

#############################################

exercicio_4_11_1

exercicio_4_11_2

#############################################

exercicio_4_12_1

exercicio_4_12_2

