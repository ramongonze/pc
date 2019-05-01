#!/usr/bin/env python
# coding: utf-8

# # Exercício_1

# In[ ]:


def Exercício_1_1(t,n):
    ## Calcula o fatorial progredindo até n
    n=1
    if n==t:
        resultado=1
    while t>=2:
        resultado=resultado*(n+1)
        n=n+1
        t+=1
    return resultado
print(Exercício_1_1(t,n))


# In[ ]:





# ## Exercício_2

# Digite o valor de k:
# 
# sinal ← -1
# 
# função harmônica_alternada(k,sinal):
# calcula o valor  da harmônica alternada
#  
#      se k=1:
#   
#          resultado é 1
#  
#      se k é ímpar:
#   
#         resultado=-sinal/k + -sinal/k-1
#  
#      se k é par:
#   
#         resultado=sinal/k + -sinal/k-1
#  
#      retorne resultado
# 
# printe: Harmônica_alternada 

# In[17]:


def exercício_2_2(k,sinal):
    ## calcula a série harmônica alternada
    if k==1:
        resultado=1
    elif k%2!=0:    
        resultado=-sinal/k + (-1*sinal/(k-1))
    else:
        resultado= sinal/k + (-sinal/(k-1))
    return resultado


# ## Exercício_3_1

# def neper_homR(termos,denom):
#  
#  if termos==1:
#   
#   res=denom
# 
#  else:
#   
#   res=denom + 1/neper(termos-1,denom+4)
# 
# O programa para se calcular a parte homegênea da função neper para 4 termos se enquadraria na parte do else:
# 
# 
# res=6+ 1/neper(3,10). Neste caso, como o número de termos ainda é superior a 1, se enquadra no else e o denom passa a ser 10:
# 
# 
# res=10+1/neper(2,14). Neste caso, como o número de termos ainda é superior a 1, se enquadra no else e o denom passa a ser 14:
# 
# 
# res=14+1/neper(1,18). Neste caso, como o número de termos é igual a 1, se enquadra no if:
# 
# 
# res=denom=18.
# 

# ## Exercício_3_2

# def neper_homI(termos,denom):
# 
#      import math
#  
#      res=math.inf
#  
#      while termos>0:
#   
#         denom=1/res
#   
#         termos=termos-1
#   
#         denom=denom+4
# 
# return resultado  
# 
# Quero calcular com 4 termos, então se enquadra no while:
# 
# termos=3 e denom=6. Ainda é maior que 0, ainda se enquadra no while:
# 
# termos=2 e denom=10. Ainda é maior que 0, ainda se enquadra no while:
# 
# termos=1 e denom=14. Ainda é maior que 0, ainda se enquadra no while:
# 
# termos=0 e denom=18

# ## Exercício_4_1

# In[23]:


def Exercício_4_1_1(n):
    ## Calcula uma série formada por raízes de 1 recursivamente
    if n==1:
        resultado=n**0.5
    if n>=2:
        resultado=(1+Exercício_4_1_1(n-1))**0.5
    return resultado
def Exercício_4_1_2(n):
    ## Calcula uma série formada por raízes de 1 iterativamente
    if n>=0:
        resultado=1
    while n>1:
        resultado=(resultado+1**0.5)**0.5
        n=n-1
    return resultado
def Exercício_4_1_3(n):
    ## Calcula uma série formada por raízes de 1 utilizando while True.
    if n<0:
        resultado=0
    else:
        resultado=1
        while true:
            resultado=(resultado+1**0.5)**0.5
            n=n-1
            if n<2:
                break
    return resultado


# ## Exercício_4_2

# In[38]:


def Exercício_4_2_1(n):
    ## Calcula uma série de sucessivas divisões por 1/1 recursivamente
    if n==1:
        resultado=1
    if n==2:
        resultado= 1+(1/1)
    if n>2:
        resultado=1+1/Exercício_4_2_1(n-1)
    return resultado
def Exercício_4_2_2(n):
    ## Calcula uma série de sucessivas divisões por 1/1 iterativamente
    if n==1:
        resultado=1
    elif n==2:
        resultado= 1+(1/1)
    while n>2:
        resultado=1+1/Exercício_4_2_2(n-1)
        n=n-1
    return resultado
def Exercício_4_2_3(n):
     ## Calcula uma série de sucessivas divisões por 1/1 utilizando while True
    if n==1:
        resultado=1
    elif n>=2:
        resultado= 1+(1/1)
        while True:
            resultado=1+1/Exercício_4_2_3(n-1)
            n=n-2
    return resultado


# ## 4_3

# In[40]:


def Exercício_4_3_1(k):
    ## Calcula o valor série harmônica fatorial recursivamente
    if k==1:
           resultado=1        
    elif k>0:
           resultado=1/k + Exercício_4_3_1(k-1)
    return resultado
def Exercício_4_3_2(k):
     ## Calcula o valor da série harmônica fatorial iterativamente
    if k==1:
        resultado=1
    while k>1:
        resultado=1/k + Exercício_4_3_1(k-1)
        n=n-1
    return resultado
def Exercício_4_3_3(k):
     ## Calcula o valor da série harmônica fatorial, utilizando While True
    if k==1:
        resultado=1
    if k>1:
        resultado=1
        while True:
            resultado=1/k + Exercício_4_3_1(k-1)
            if k<=1:
                break
    return resultado


# In[ ]:





# ## 4.4

# In[45]:


def Exercício_4_4_1(x,k):
    ## Calcula o valor da série x^k/k! recursivamente
    if k==0:
        resultado=1
    if k>=1:
        resultado=x**k/Exercício_4_4_1(x,k-1)
    return resultado 
def Exercício_4_4_2(x,k):
    ## Calcula o valor da série x^k/k! iterativamente
    if k==0:
        resultado=1
    while k>=1:
        resultado=x**k/Exercício_4_4_1(x,k-1)
        k=k-1
        if k<1:
            break
    return resultado      
def Exercício_4_4_3(x,k):
    ## Calcula o valor da série x^k/k! utilizando while True
    if k==0:
        resultado=1
    if k>=1:
        resultado=1
        while True:
            resultado=x**k/Exercício_4_4_3(x,k-1)
            k=k-1
            if k<1:
                break
    return resultado        


# ## 4.5

# In[46]:


def Exercício_4_5_1(k):
    ## Calcula recursivamente o valor da série harmônica alternada
    if k==0:
        resultado=1
    else:
        resultado= 1/k + 1*(-1)**k/Exercício_4_5_1(k-1)
    return resultado
def Exercício_4_5_2(k):
    ## Calcula iterativamente o valor da série harmônica alternada
    if k==0:
        resultado=1
    while k>0:
        resultado= 1/k + 1*(-1)**k/Exercício_4_5_2(k-1)
        k=k-1
    return resultado
def Exercício_4_5_3(k):
    ## Calcula,utilizando while True, o valor da série harmônica alternada
    if k==0:
        resultado=1
    if k>0:
        resultado=1
        while True:
            resultado= 1/k + 1*(-1)**k/Exercício_4_5_3(k-1)
            k=k-1
            if k<=0:
                break
    return resultado


# ## 4.6

# In[49]:


def Exercício_4_6_1(n):
    ## Calcula uma aproximação para o valor de pi recursivamente
    if n==1:
        resultado=3
    if n==2:
        resultado=3 + ((-1)**n * 4)/((n)*(n+1)*(n+2))
    if n>2:
        resultado = Exercício_4_6_1(n-1) + ((-1)**n *4)/((2*n -2)*(2*n-1)*(2*n))
    return resultado
def Exercício_4_6_2(n):
    ## Calcula uma aproximação para o valor de pi iterativamente
    if n==1:
        resultado=3
    if n==2:
        resultado=3 + ((-1)**n * 4)/((n)*(n+1)*(n+2))
    while n>2:
        resultado = Exercício_4_6_2(n-1) + ((-1)**n *4)/((2*n -2)*(2*n-1)*(2*n))
        n=n-1
    return resultado
def Exercício_4_6_3(n):
    ## Calcula uma aproximação para o valor de pi, utilizando while True
    if n==1:
        resultado=3
    if n==2:
        resultado=3 + ((-1)**n * 4)/((n)*(n+1)*(n+2))
    if n>2:
        while True:
            resultado = Exercício_4_6_3(n-1) + ((-1)**n *4)/((2*n -2)*(2*n-1)*(2*n))
            n=n-1
            if n<2:
                break
    return resultado


# ## 4_7

# In[52]:


def Exercício_4_7_1(n):
    ## Calcula o valor da função F recursivamente
    if n==0:
        resultado=0
    if n==1:
        resultado=1
    if n>1:
        t=n-1
        resultado=Exercício_4_7_1(t)*Exercício_4_7_1(t-1)
    return resultado
def Exercício_4_7_2(n):
     ## Calcula o valor da função F iterativamente
    if n==0:
        resultado=0
    if n==1:
        resultado=1
    while n>1:
        t=n-1
        resultado=Exercício_4_7_2(t)*Exercício_4_7_2(t-1)
        n=n-1
    return resultado
def Exercício_4_7_3(n):
     ## Calcula o valor da função F utilizando while true
    if n==0:
        resultado=0
    if n==1:
        resultado=1
    if n>1:
        while True:
            t=n-1
            resultado=Exercício_4_7_3(t)*Exercício_4_7_3(t-1)
            n=n-1
            if n<=1:
                break
    return resultado


# ## 4_8

# In[8]:


def exercício_4_8_1(n):
    if n==1:
        resultado=1
    if n==2:
        resultado=1 + 1/1
    if n>=3:
        resultado=1 + 1/(1+(1/n-1))
    return resultado


# ## 4_9

# In[4]:


def exercício_4_1(n,denom):
    ## Função que calcula recursivamente uma aproximação para raiz de 2 a partir do número de termos
    if n==1:
        resultado=1
    else:
        resultado=1+exercício_4_1(n,denom)
    return resultado       


# ## 4_10

# In[14]:


def exercício_4_10_1(termos):
    ## Função que calcula o valor ou uma aproximação para 5,4321.
    if termos==1:
        resultado=5
    elif termos==2:
        resultado=5+1/2
    elif termos==3:
        5+1/(2+(1/3))
    elif termos==4:
        resultado=5+1/(2+(1/(3+1/5)))
    elif termos==5:
        resultado=5+1/(2+(1/(3+1/(5+(1/2)))))
    if termos==6:
        resultado=5+1/(2+(1/(3+1/(5+(1/2+(1/127))))))
    return resultado                   


# ## 4_11

# In[15]:


def exercício_4_11_1(termos,denom):
    ## Calcula recursivamente a tan(x) por meio de uma série 
    if termos==1:
        denom=1/x
        res=1/denom
    else:
        denom=1/x-exercício_4_11_1(termos,denom*3)
        res=1/denom
    return res


# ## 4_12

# In[16]:


def exercício_4_12_1(termos,denom):
    ## Calcula recursivamente o valor de e
    if termos==1:
        res=2
    if termos==2:
        denom=0
        res=2+(termos/2+denom)
    else:
        res=exercício_4_12_1(termos-1,denom)/(denom+1)
    return res    


# In[ ]:




