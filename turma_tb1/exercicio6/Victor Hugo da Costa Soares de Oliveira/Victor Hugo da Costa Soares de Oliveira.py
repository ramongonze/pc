#!/usr/bin/env python
# coding: utf-8

# Exercicio_1

# In[1]:


def fatorial (r,n):
    res=0
    if n==0:
        res=1
    if r<n:
        res=r*fatorial(r+1,n)
    else:
        res=n
    return res
r=1
n=int(input("Entre com n:"))
print(f"O fatorial de {r,n} é {fatorial (r,n)}")


# In[2]:


def fatorial(n):
#"""Calcula o fatorial...
# Retorna 0 se n<0."""
    if n<0:
        resultado=0
    elif n==0:
        resultado=1
    else:
        resultado=1
        while True:
            resultado=resultado*r
            r=r+1
            if r==n:
                break
    return resultado
r=1
n=int(input("Entre com n:"))
print("O fatorial de %d é %d" %(n,fatorial(n)))


# In[ ]:




