#!/usr/bin/env python
# coding: utf-8

# Exercício 1

# In[5]:


n = int(input("Digite um natural "))
n == False
while n == False:
    try:
        if n >= 0:
            n = True
    except ValueError:
            print("Digite um natural ")
def fatorial(n,c):    
    if n == 0:
        res = 1
    else:
        res = (c) * fatorial(n-1,c+1)
    return res
print("O fatorial de %d é %d"%(n,fatorial(n,1)))


# Exercício 2

# def funcao(a): Definir a função 
#     res = 0 -> Primeiro resultado
#     sinal_para_alternada = -1 -> Sinal necessário para a série alternada
#     Enquanto n > 0:
#         res = (1/n)*sinal_para_alternada + res
#         a = a - 1
#         sinal_para_alternada = (-1)*sinal_para_alternada
#     retorna res
# funcao(a)

# In[ ]:


def funcao(a):
    res = 0 
    sinal_para_alternada = -1 
    while n > 0:
        res = (1/n)*sinal_para_alternada + res
        a = a - 1
        sinal_para_alternada = (-1)*sinal_para_alternada
    return res
funcao(3)


# Exercício 3

# In[1]:


def neper_homR(termos,denom):
    if (termos == 4):
        res = denom
    else:
        res = denom + 1/neper_homR(termos-1,denom+4)
    return res


# In[3]:


def neper_homI(termos,denom):
    import math
    res = math.inf
    while (termos > 0):
        res = denom + 1/res
        termos = termos-1
        denom = denom+4
return res


# In[ ]:




