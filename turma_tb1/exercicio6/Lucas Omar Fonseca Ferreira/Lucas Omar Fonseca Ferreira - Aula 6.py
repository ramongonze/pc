#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1

# def fatorial(n):
#    resultado = 0
#    cont = 1
#    if n >= 0:
#        if n == 0 or n == 1:
#            resultado = 1
#        else:
#            resultado = 2 * fatorial(cont+1)
#    return resultado
#print("%d" %fatorial(n))

# 1 Recursivo
n = int(input("Digite um número: "))
def fatorial (m, n):
    if m == n:
        resultado = m
    else:
        resultado = m*fatorial(m+1,n)
    return resultado
print("%d" %fatorial(1,n))


# In[7]:


# 1 Iterativo ao contrário
#n = int(input("Digite um valor: "))
#def fatorial(m,n):
#    resultado = 0
#   if n >= 0:
#       resultado = 1
#       while (n > m):
#           resultado *= n
#           m += 1
#   return resultado
#print("%d" %fatorial(1,n))
n = int(input("Digite um número para calcular seu fatorial: "))
def fatorial(n):
    m=0
    if n<0:
          resultado = 0
    else:
        resultado = 1
        while m < n:
            m+=1
            resultado *= m
    return resultado
print("%d" %fatorial(n))


# In[ ]:





# In[ ]:





# In[4]:


# 4.7
n = int(input("Entre com o número de termos da sequência: "))
def fibonacci(lim,m,n):
     if lim > 0:
        return 1
     elif n == 0:
        return 1
     else
        resultado = fibonacci(n-1) + fibonacci(n-2)
        
print("%d" %fibonacci(n))    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




