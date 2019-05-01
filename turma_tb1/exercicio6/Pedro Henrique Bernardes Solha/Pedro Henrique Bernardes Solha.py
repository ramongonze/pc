#!/usr/bin/env python
# coding: utf-8

# ### Exercício 1

# In[1]:


n = int(input("  "))
def fatorial(n):
    """Calcula o fatorial do natural n 
       usando "enquanto". Retorna 0 se n < 0.
    """
    resultado = 0
    if n >= 0:
        resultado = 1
    while (n > 1):
        resultado = resultado * n
        n = n - 1
    return resultado
    print(fatorial(n))


# In[ ]:




