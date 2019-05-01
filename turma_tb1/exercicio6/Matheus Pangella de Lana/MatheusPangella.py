#!/usr/bin/env python
# coding: utf-8

# # Matheus Pangella de Lana 2017106857

# In[ ]:


def exercicio1_1(f,n):
    """Essa função calcula o fatorial de um numero natural n passado como argumento recusivamente"""
    if n<0:
        resultado=0
    elif n==0:
        resultado=1
    elif f == n:
        resultado = n
    elif f<n:
        resultado = f*exercicio1_1(f+1,n)
    return resultado

def exercicio1_2(f,n):
    """Essa função calcula o fatorial de um numero natural n passado como argumento iterativamente com o comando enquanto"""
    resultado = 0
    if n >= 0:
        resultado = 1
        while (f <= n):
            resultado = resultado * f
            f = f +1
    return resultado


# In[ ]:


def exercicio_2(n):
    if n == 1:
        resultado = 1
    elif (n%2==0):
        resultado = -1/n + exercicio_2(n-1)
    elif (n!=0):
        resultado = 1/n + exercicio_2(n-1)
    return resultado


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




