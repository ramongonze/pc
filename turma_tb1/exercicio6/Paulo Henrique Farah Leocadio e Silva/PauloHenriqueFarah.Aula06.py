#!/usr/bin/env python
# coding: utf-8

# ## EXERCÍCIO 1

# In[13]:


def exercicio1_1(n,i):
    if i<=n:
        resultado = i*exercicio1_1(n,i+1)
    else:
        resultado = 1
    return resultado


def exercicio1_2(p,h):#Aqui temos um cálculo de fatorial iterativamente
    if h <0:
        res = 0 
    elif h==0:
        res = 1
    else:
        res = 1
        while True:
            res = res*p
            p=p+1
            if h<p:
                break
        return res


# ## EXERCÍCIO 2

#     def exercicio_2(n): ---> O primeiro passo é definir a função.
#        resultado = 0  -----> Começar com um resultado incial, que neste caso será 0.
#        sinal = -1 ------> Como quero calcular a harmônica alternada, tenho de acrescentar que o sinal inicial seria de '-1'.
#        while n > 0:------> Iterativamnete, pode se calcular o somatório da série harmônica alternada.
#             resultado =( 1/n)*sinal + resultado -----> O resultado será este, levando em consideração que agora temos a existência de um sinal que influenciará no somatório.
#             n = n - 1 -----> Utilizamos isto para ir diminuindo o 'n'.
#             sinal = (-1)*sinal ------> Consideremos o sinal que irá variar a cada iteração.
#        return resultado -----> 'return' para retornar o resultado que se quer obter.
#     exercicio_2(3)

# In[12]:


def exercicio2(n):
    resultado = 0
    sinal = -1
    while n > 0:
        resultado =( 1/n)*sinal + resultado
        n = n - 1
        sinal = (-1)*sinal
    return resultado
exercicio2(3)


# ## EXERCÍCIO 3

#        def neper_homogeneo(termos,denom)
#       if (termos == 1)
#              res= denom 
#       else:
#             res= denom +1/neper_homogeneo(termos-1,denom+4)
#     def neper(termos):
#       if(termos == 1 ):
#         e = 1
#       elif (termos == 2 ):
#         e= 1+ 2/1
#       else: #termos >=3
#         e = 1 + 2/(1+1/neper_homogeneo(termos-2,6)
# 
#     
#       Aqui, o objetivo é calcular,à mão e recursivamente, os 4 primeiros números da parte homogênea(exceto os dois primerios que não são calculados pela parte homogênea) do número de Euler('e'). O  termo a ser calculado pela parte homogênea seria o sexto de um modo geral. Assim, quero 'def neper_homogeneo(4,denom)' e será dado por:
#       if (termos == 1)
#              res= denom 
#       else:
#             res= 6 +1/neper_homogeneo(4-1,6+4) ESTA PARTE É IGUAL A ( 6 + 1/10)
#       if (termos == 1)
#              res= denom 
#       else:
#             res= 10 +1/neper_homogeneo(3-1,10+4) ESTA PARTE, JUNTA DA OUTRA, É IGUAL A ( 6+1/(10+1/14))
#       if (termos == 1)
#              res= denom 
#       else:
#             res= 14 +1/neper_homogeneo(2-1,14+4) ESTA PARTE, JUNTA DAS DEMAIS, É IGUAL A ( 6+1/(10+1/(14+ 1/18)))
#             E COMO CHEGUEI A NÚMERO DE TERMOS == 1, O PROGRAMA ENCONTROU SUA PARADA E TERÍAMOS:
# 
#       if (termos == 1)
#              res= 18 ---> EXECUTARIA ESTA PARTE.
#       else:
#             res= 18 +1/neper_homogeneo(1-1,18+4)
# 
# 
# 

#     def neper_homI(termos,denom):
#        import math
#        res = math.inf
#        denom = 6 + (termos-1)*4
#      while (termos > 0):
#         res = denom + 1/res
#         termos = termos-1
#         denom = denom-4
#      return res
# 
# 
#        Aqui o objetivo é calcular,à mão e iterativamente, os 4 primeiros números da parte homogênea(exceto os dois primerios que não são calculados pela parte homogênea) do número de Euler('e'). Assim, quero 'def neper_homI(4,denom)' e será dado por:
#        while (termos > 0):
#         res = 6 + 1/res
#         termos = 4-1
#         denom = 6+4
#     return res --------> esta parte retornará 6 + 1/10
#        while (termos > 0):
#         res = 10 + 1/res
#         termos = 3-1
#         denom = 10+4
#     return res --------> esta parte, junta a outra, retornará 6 + 1/(10+ 1/14)
#        while (termos > 0):
#         res = 14 + 1/res
#         termos = 2-1
#         denom = 14+4
#     return res ---------> Agora, teremos 6 + 1/(10+ 1/(14 + 1/18))
#         while (termos > 0):
#         res = denom + 1/res
#         termos = 0
#         denom = denom+4
#     return res -------> 6 + 1/(10+ 1/(14 + 1/18))
# 
# 

# ## EXERCÍCIO 4

# In[10]:


def exercicio4_1_1(n):
    if (n==1):
        res = n**0.5
    if n>=2:
        res=(1 + exercicio_4_1(n-1))**0.5
    return res
exercicio_4_1(4)


# In[ ]:


def exercicio4_1_2(n):
    resultado = 1
    while n > 1:
        resultado = (1 + (resultado))**0.5
        n= n-1
    return resultado
exercicio_4_2(3)

