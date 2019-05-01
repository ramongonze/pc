#!/usr/bin/env python
# coding: utf-8

# Programação de computadores
# Exercícios aula 06
# Aluna: Raíssa Nepomuceno Freitas
# Matrícula: 2017104013

# In[ ]:


#Exercício 1 - Recursiva

def fatorial(n,k):
        if k == 0:
            return 1
        if n == k:
            return k
        else:
            return n*fatorial(n+1,k)
n=1
k=0
fatorial(n,k)


# In[ ]:


#Exercício 1 - Iterativa
def fatorial(n,k):
    resultado = 0
    if n >=0:
        resultado = 1
        while (n>=k):
            resultado = resultado*k
            k = k+1
        return resultado
n=5
k=1
fatorial(n,k)


# In[ ]:


#Exercício 2
def harmonica(n):
    if n == 1:
        resultado = 1
    else:
        resultado = (((-1)**(n+1)*(1/n)) + (harmonica(n-1)))
    return resultado

n=5
harmonica(n)


# In[ ]:


#Exercício 4.1
def fi(n):
    if n == 1:
        resultado = 1
    else: 
        resultado = (1+fi(n-1))**(1/2)
    return resultado
fi(3)


# In[ ]:


def k(n):
    resultado =0
    while n>=1 :
        resultado = (resultado +  1 ) **(1/2)
        n = n-1
    return resultado 
k(3)


# In[ ]:


#Exercício 4.2
def fi(n):
    if n == 1:
        resultado = 1
    else: 
        resultado = 1+(1/(1+fi(n-1)))
    return resultado
fi(3)


# In[ ]:


#Exercício 4.3
def fatorial(n):
    if(n==1):
        resultado = 1
    else:
            resultado = 1/(n*(fatorial(n-1)))
    return resultado
    
n=3
fatorial(n)


# In[ ]:


def fatorial (n):
    resultado = 0
    while n > 0:
        resultado =  1 +  1/n + resultado
        n = n - 1
        return resultado
fatorial(3)


# In[ ]:


#Exercício 3.4
def fatorial(n):
    if(n==1):
        resultado = 1
    else:
        resultado = ((x**n)/n*(fatorial(n-1)))
    return resultado

n= 3
x= 1
fatorial(n)


# In[ ]:


# Exercício 4.5 
def fatorial1(n) :
    if n == 1 :
         resultado = 1 
    else :
         resultado = 1 + ((-1)**n)/(fatorial1(n-1)) 
    return  resultado 
fatorial1(30)


# In[ ]:


# Exercício 4.6 
def pi(termos) :
   if  termos == 1 :
       resultado = 3
   else :
       resultado = 3 + pi2(1,1,termos)
   return resultado 
       
def pi2(iteração,sinal,termos) :
   if iteração == termos - 1 : 
       k=2*iteração 
       resultado = (sinal*4)/((k)*(k+1)*(k+2))
   else :
       k=2*iteração 
       resultado = (sinal*4)/((k)*(k+1)*(k+2)) + pi2(iteração + 1,(-1)*sinal,termos)
   return resultado 

pi(100)


# In[ ]:


# Exercício 4.7
def fatorial (n): 
    if n == 0 :
         resultado = 0
    elif  n == 1 :
        resultado = 1 
    elif  n > 1 :
         resultado = fatorial(n-1) + fatorial (n-2)
    return  resultado 
fatorial(4) 

