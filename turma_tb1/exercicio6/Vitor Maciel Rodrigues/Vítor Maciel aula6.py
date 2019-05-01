#!/usr/bin/env python
# coding: utf-8

# # Exercício 1

# Recursivo

# In[4]:


def fatorial(n): 
    if n == 0: 
        return 1  
    else: 
        return n*fatorial(n+1) 
fatorial (10)


# Iterativo

# In[20]:


def fatorial(n):
    """Calcula o fatorial do inteiro n, usando "repita...até". 
    Retorna 0 se n < 0. 
    """ 
    if n < 0: 
            resultado = 0 
    elif n == 0: 
            resultado = 1 
    else: 
            resultado = 1 
            while True: 
                resultado = resultado * n 
            n = n - 1 
            if n < 2: 
                break 
return resultado 
n = int(input("Entre com n: ")) 
print("O fatorial de %d é %d"%(n,fatorial(n)))


# # Exercício 2

# Recursivo

# In[ ]:


def harmonicaR(n): 
       if n == 1: 
           resultado = 1 
           else: 
               resultado = 1/n + harmonicaR(n-1) 
               return resultado


# In[ ]:


Iterativo


# In[ ]:


def harmonicaI(n): 
    resultado = 0 
    while n > 0: 
        resultado = \ 
        1/n + resultado 
        n = n - 1 
        return resultado


# # Exercício 3

# Recursivo

# In[ ]:


def neper_homR(termos,denom): 
    if (termos == 1): 
        res = denom 
        else: 
            res = denom + 1/neper_homR(termos-1,denom+4) 
            return res 


# Iterativo

# In[ ]:


def neper_homI(termos,denom): 
    import math 
    res = math.inf 
    while (termos > 0): 
        res = denom + 1/res 
        termos = termos-1 
        denom = denom+4 
        return res

