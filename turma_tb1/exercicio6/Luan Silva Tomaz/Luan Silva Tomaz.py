#!/usr/bin/env python
# coding: utf-8

# # Luan Silva Tomaz

# # Lista aula 06

# # Exercício 01
# 
# ## 1- Refaça os algoritmos e os programas recursivo e iterativo para calcular o fatorial do menor valor até o valor passado como argumento. 
# 
# ### Dicas: 
# ### 1.1 - A função terá mais um argumento para indicar o termo que se quer calcular. Qual valor esse argumento deve ter quando a função é chamada?
# 
# ### 1.2 - O caso de base agora muda para testar se o termo é igual ao argumento n, o natural cujo fatorial se quer calcular.
# 
# ### 1.3 -  A chamada recursiva irá aumentar o argumento do termo em vez de diminuir.

# ### Algoritmo 

# *receber valor
# 
# *validar valor recebido
# 
# *criar função
# 
#     enquanto o número de voltas for menor que o número que deseja calcular o fatorial
# 
#         somatorio do resultado vezes o numero de voltas
# 
#         retornar o resultado
# 
# *apresentar o resultado para o usuário

# ### Iteração

# In[26]:


#Validador
Validador_n = False
while Validador_n == False:
    n = int(input('Achar fatorial de: '))
    if n >= 0:
        Validador_n = True
    else:
        print('Favor digitar um número natural!')

#Função fatorial
def exercicio_1_1_1(n):
    resultado = 1
    contador = 1
    while contador < n + 1:
        resultado *= contador
        contador += 1
    return resultado    
print('{}! é igual a {}'.format(n,exercicio_1_1_1(n)))


# ### Recursão
# 

# In[29]:


#Validador de entrada
Validador_Num = False
while Validador_Num == False:
    try:
        Num = int(input('Achar o fatorial de: '))
        if Num >= 0:
            Validador_Num = True
    except ValueError:
        print('Favor digitar um número natural!')   
#Função
def exercicio_1_2_1(Num,contador):
    if Num == 0:
        resultado = 1
    else:
        resultado =  (contador) * exercicio_1_2_1(Num-1,contador+1)
        
    return resultado    
    
#print saída do resultado
print('{}! é igual a {}'.format(Num,exercicio_1_2_1(Num,1)))


# # Exercício 02
# 
# ## Faça o algoritmo e o programa para calcular a função harmônica com sinais alternados.
# 

# ### Algoritimo

# #### Validador
# *validador de entrada
#    
#     receber qual a posição do termo
#      
# #### Função
# 
# *O primeiro denominador é 1
# 
# *enquanto o denominador for menor que posição + 1
# 
#     somar no acumulador (1/denominador)*(sinal)
#     
#     denominador ganha mais um
#     
#     o sinal é multipicado por -1 para que ele alterne a cada volta
# 
# *retornar o valor acumulado
# 
# *imprimir o resultado do somatório

# ### Exemplo Função Harmonica

# In[30]:


#Validador de entrada
Validador_posição = False
while Validador_posição == False:
    try:
        posição = int(input('Favor digitar o número de termos: '))
        if posição >= 0:
            Validador_posição = True
    except ValueError:
        print('Favor digitar um número natural!')

#Função
def exercicio_2_1_1(posição):
    Cond_fim = 1
    somatório = 0
    sinal = 1
    while Cond_fim < posição + 1:
        somatório = somatório + (1/Cond_fim)*(sinal)
        Cond_fim = Cond_fim + 1
        sinal = sinal * (-1)
    return somatório
print('o resultado é {}'.format(exercicio_2_1_1(posição)))


# # Exercício 03
# 
# ## Execute à mão as funções iterativas e recursivas neper_homR e neper_homI para a parte homogênea que calcula a fração contínua para o número de Euler e para 4 termos (exceto os 2 primeiros que não são calculados por essas funções).
# 

# ### Neper_homl - Iterativa código

# In[31]:


#Validador de entrada
Validador_posição = False
while Validador_posição == False:
    try:
        termos = int(input('Favor digitar o número de termos: '))
        if termos >= 0:
            Validador_posição = True
    except ValueError:
        print('Favor digitar um número natural!')
        
#Função
def exercicio_3_1_1(termos,denom):
    import math
    res = math.inf
    denom = 1+(termos-1)*4
    while (termos > 0):
        res = denom + 1/res
        termos = termos - 1
        denom = denom - 4
    return res
print(exercicio_3_1_1(termos,1))


# ### neper_homI - Iterativa a mão
# 
# #### Recebe
# termos = 4
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 
# ##### validador
# termos maior ou igual a 0? Sim
# 
# Teste verificado:
# proxima linha depois do teste
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 
# #### Definir denominador
# 
# denom = 1+(4-1)*4
# 
# denom = 13
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 
# #### enquanto termos maior que 0:
# 
# res = 13 + 1/inf
# 
# res = 13
# 
# 
# termos = 4 - 1
# 
# termos = 3
# 
# 
# denom = 13 - 4
# 
# denom = 9
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 
# ##### termos maior que 0? Sim
# repete
# 
# 
# res = 9 + 1/13
# 
# res = 9,076923077,,,
# 
# 
# termos = 3 - 1
# 
# termos = 2
# 
# 
# denom = 9 - 4
# 
# denom = 5
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 
# ##### termos maior que 0? Sim
# 
# repete
# 
# 
# res = 5 + 1/9,076923077...
# 
# res = 5,110169491...
# 
# 
# termos = 2 - 1
# 
# termos = 1
# 
# 
# denom = 5 - 4
# 
# denom = 1
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 
# ##### termos maior que 0? Sim
# repete
# 
# res = 1 + 1/5,110169491...
# res = 1.195688225...
# 
# termos = 1 - 1
# termos = 0
# 
# denom = 1 - 4
# denom = -3
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 
# ##### Termos maior que 0? Não
# Quebrar looping
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 
# ##### Retornar o valor de res
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 
# #### Fim da função
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 
# #### imprimir o valor agregado a função
# 
# saída = 1.195688225...
# 

# ### neper_homR - Recursiva código

# In[33]:


#Validador de entrada
Validador_posição = False
while Validador_posição == False:
    try:
        termos = int(input('Favor digitar o número de termos: '))
        if termos >= 0:
            Validador_posição = True
    except ValueError:
        print('Favor digitar um número natural!')

#Função
def exercicio_3_2_1(termos,denom):
    if (termos == 1):
        res = denom
    else:
        res = denom + 1/neper_homR(termos-1,denom+4)
    return res
print(exercicio_3_2_1(termos,1))


# ### neper_homR - Recursiva a mão

# Termos = 4
# denom = 1
# 
# ##### Termos igual a 1? Não
# 
# ##### Res
# 
# re1 = denom
# 
# 
# $$ re1 = 1$$
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 
# ##### Denom
# 
# denom = denom + 4 
# 
# denom = 5
# 
# ##### Termos
# 
# termos = termos - 1
# 
# termos = 3
# 
# ##### Res
# 
# res2 = 1 + 1/(denom)
# 
# res2 = 1 + 1/(5)
# 
# 
# $$ re2 = 1+{1\over5}$$
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 
# ##### Denom
# 
# denom = denom + 4
# 
# denom = 9
# 
# ##### Termos
# 
# termos = termos - 1
# 
# termos = 2
# 
# ##### Res
# 
# res3 = 1 + 1/(5 + 1/(denom)) 
# 
# res3 = 1 + 1/(5 + 1/(9))
# 
# 
# $$ re3 = 1+{1\over5+{1\over9}}$$
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 
# ##### Denom
# 
# denom = denom + 4
# 
# denom = 13
# 
# ##### Termos
# 
# termos = termos - 1
# 
# termos = 1
# 
# ##### Res
# 
# res4 = 1 + 1/(5 + 1/(9 + 1/(denom)))
# 
# res4 = 1 + 1/(5 + 1/(9 + 1/(13)))
# 
# 
# $$ re4 = 1+{1\over5+{1\over9+{1\over13}}} $$
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 
# #### Termos igual a 1? Sim
# 
# quebrar looping
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 
# ##### Retornar o valor de res
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 
# #### Fim da função
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 
# #### imprimir o valor agregado a função
# 
# saída = 1.1956882255389718
# 

# # Exercício 04
# 
# ## Faça programas Python recursivos e iterativos com enquanto e repita...até para as seguintes frações contínuas e séries:

# ## 4.1
# $$φ = \sqrt{1 + \sqrt{1 + \sqrt{1 + \sqrt{1 + ...}}}}$$
# 
# 

# 

# In[ ]:


from math import sqrt
x = 0

while True:
    n = sqrt(1 + x)
    x = n

print(n)


# ## 4.2
# 
# $$ 1+{1\over1+{1\over1+...}} $$

# ### 4.2.1 - Iterativa

# In[12]:


#Validador de entrada
Validador_Num = False
while Validador_Num == False:
    try:
        termos = int(input('Digite a quantidade de termos: '))
        if termos >= 0:
            Validador_Num = True
            denom = 1
    except ValueError:
        print('Favor digitar um número natural!')

#função
def exercicio_4_2_1(termos,denom):
    import math
    res = math.inf
    while (termos > 0):
        res = denom + 1/res
        termos -= 1
    return res
print(exercicio_4_2_1(termos,denom))


# ### 4.2.1 - Recursão

# In[34]:


#Validador de entrada
Validador_Num = False
while Validador_Num == False:
    try:
        termos = int(input('Digite a quantidade de termos: '))
        if termos >= 0:
            Validador_Num = True
            denom = 1
    except ValueError:
        print('Favor digitar um número natural!')
'''
#função
def neper_homI(termos,denom):
    import math
    res = math.inf
    while (termos > 0):
        res = denom + 1/res
        termos -= 1
    return res
print(neper_homI(termos,denom))
'''
#Função
def exercicio_4_2_2(termos,denom):
    if (termos == 1):
        res = denom
    else:
        res = denom + 1/neper_homR(termos-1,denom)
    return res
print(exercicio_4_2_2(termos,1))


# ## 4.3
# 
# $$\sum_{k=0}^{\infty}{1\over k!}$$

# ### 4.3.1 - Iteração

# In[53]:


#Validador de entrada
Validador_Num = False
while Validador_Num == False:
    try:
        Num = int(input('Digite o valor de n: '))
        if Num >= 0:
            Validador_Num = True
    except ValueError:
        print('Favor digitar um número natural!')

#função fatorial

def exercicio_4_3_1(n):
    if n == 0:
        resultado = 1
    else:
        resultado = n * exercicio_4_3_1(n-1)
    return resultado

#Função da somatória
def exercicio_4_3_1(Num):
    k = 1
    somatório = 0
    while k < Num + 1:
        somatório = somatório + (1/(fatorial(k)))
        k = k + 1
    return somatório
print('o resultado é {}'.format(exercicio_4_3_1(Num)))


# ### 4.3.2 - Recursão

# In[37]:


Num = int(input('Digite o valor de n: '))

#função fatorial
def exercicio_4_3_2(n):
    resultado = 1
    while n > 0:
        resultado = resultado * n
        n = n - 1
    return resultado

#Função da somatória
def exercicio_4_3_2(Num):
    k = 1
    somatório = 0
    while k < Num + 1:
        somatório = somatório + (1/(fatorial(k)))
        k = k + 1
    return somatório
print('o resultado é {}'.format(exercicio_4_3_2(Num)))


# ## 4.4
# 
# $$\sum_{k=0}^{\infty}{x^k\over k!}$$

# ### 4.4.1 - Iteração

# In[54]:


#Validador de entrada
Validador_Num = False
while Validador_Num == False:
    try:
        Num = int(input('Digite o valor de n: '))
        x = float(input('Digite o valor de x: '))
        if Num >= 0:
            Validador_Num = True
            break
    except ValueError:
        print('Favor digitar um número natural!')

#função fatorial
def fatorial(n):
    if n == 0:
        resultado = 1
    else:
        resultado= n*fatorial(n-1)
    return resultado

#Função da somatória
def harmonica(Num):
    k = 0
    somatório = 0
    while k < Num + 1:
        somatório = somatório + ((x**k)/(fatorial(k)))
        k = k + 1
    return somatório
print('o resultado é {}'.format(harmonica(Num)))


# ### 4.4.2 - Recursão

# In[ ]:





# ## 4.5
# 
# $$p_n = \sum_{k=0}^{n}{(-1)^k\over k!}$$

# ### Iterativa

# In[ ]:


#Validador de entrada
Validador_Num = False
while Validador_Num == False:
    try:
        Num = int(input('Digite o valor de n: '))
        if Num >= 0:
            Validador_Num = True
    except ValueError:
        print('Favor digitar um número natural!')

#função fatorial        
def fatorial(n):
    resultado = 1
    while n > 0:
        resultado = resultado * n
        n = n - 1
    return resultado

#Função da somatória
def harmonica(Num):
    k = 0
    somatório = 0
    while k < Num + 1:
        somatório = somatório + (((-1)**k)/(fatorial(k)))
        k = k + 1
    return somatório
print('o resultado é {}'.format(harmonica(Num)))


# ### Recursiva

# In[ ]:


#Validador de entrada
Validador_Num = False
while Validador_Num == False:
    try:
        Num = int(input('Digite o valor de n: '))
        if Num >= 0:
            Validador_Num = True
    except ValueError:
        print('Favor digitar um número natural!')

#função fatorial
def fatorial(n):
    if n == 0:
        resultado = 1
    else:
        resultado= n*fatorial(n-1)
    return resultado

#Função da somatória
def harmonica(Num):
    k = 0
    somatório = 0
    while k < Num + 1:
        somatório = somatório + (((-1)**k)/(fatorial(k)))
        k = k + 1
    return somatório
print('o resultado é {}'.format(harmonica(Num)))


# ## 4.6
# 
# $$\pi = 3 + {4\over \mbox{2x3x4}} - {4\over \mbox{4x5x6}} + {4\over \mbox{6x7x8}} - {4\over \mbox{8x9x10}} + ...$$

# ### 4.6.1 - Iterativa

# In[ ]:


#Validador de entrada
Validador_Num = False
while Validador_Num == False:
    try:
        Num = int(input('obs: quanto maior o valor de n, mais exato será o resultado! \n'
        'obs: quanto maior o n, mais demorado será a resposta, então use com moderação\n'
                       'Digite o valor de n: \n'))
        if Num >= 0:
            Validador_Num = True
    except ValueError:
        print('Favor digitar um número natural!')

#Função
def harmonica(Num):
    k = 2
    somatório = 3
    sinal = 1
    while k < Num:
        somatório = somatório + (4/((k)*(k+1)*(k+2)))*(sinal)
        k = k + 2
        sinal = sinal * (-1)
    return somatório
print('pi é aproximadamente {}'.format(harmonica(Num)))


# ### 4.6.2 - Recursão

# ## 4.7
# 
# $$F(n) = \left \{ \begin{matrix} 0, & \mbox{n = 0} \\ 1, & \mbox{n = 1} \\ F(n-1)+F(n-2), & \mbox n>1 \end{matrix} \right.$$

# ### 4.7.1 - Iteração

# In[21]:


#Validador de entrada
Validador_Num = False
while Validador_Num == False:
    try:
        Num = int(input('obs: Favor digitar um número positivo!\n'
                        'Qual posição você deseja? '))
        if Num > 0:
            Validador_Num = True
    except ValueError:
        print('Favor digitar um número positivo!')

#função
def fibonacci(Num):
    k = Num
    a = 0 
    b = 1
    if k == 1:
        resultado = 0
    elif k == 2:
        resultado = 1
    else:
        k = k - 2
        while k > 0:   
            c = a + b
            a = b 
            b = c
            k = k - 1
            resultado = c
    return resultado
print(fibonacci(Num))


# ### 4.7.2 - Recursão

# In[20]:


#Validador de entrada
Validador_Num = False
while Validador_Num == False:
    try:
        Num = int(input('obs: Favor digitar um número natural\n'
                        'Qual posição você deseja? '))
        if Num >= 0:
            Validador_Num = True
            break
    except ValueError:
        print('Favor digitar um número positivo!')

#função
def fibonacci(Num):
    if Num == 0:
        res = 0
    elif Num == 1:
        res = 1
    elif Num > 1:
        res = (Num-1) + (Num-2)
    return res
print(fibonacci(Num))   


# ## 4.8
# 
# $$ \sqrt{3} = 1+{1\over 1+{1\over 2+{1\over 1+{ 1\over{2+...}}}}} $$

# ta errado

# In[ ]:


#Validador de entrada
Validador_Num = False
while Validador_Num == False:
    try:
        termos = int(input('Digite a quantidade de termos: '))
        if termos >= 0:
            Validador_Num = True
            denom = 2
    except ValueError:
        print('Favor digitar um número natural!')

#Função
def função(termos,denom):
    import math
    contador = 0
    res = math.inf
    resultado = 0
    while (termos > 0):
        res = denom + 1/res
        termos = termos-1
        contador = contador + 1
        if contador % 2 == 0:
            denom = denom + 1
        else:
            denom = denom - 1
        if 1 < res < 2:
            resultado = res
    res = res - 1
    return resultado
print(função(termos,denom))


# ## 4.9
# 
# $$\sqrt{2} = 1 + {1\over 2+{1\over 2+{1\over 2+{1\over 2+{1\over 2+...}}}}}$$

# ### 4.9.1 - Iterativa

# In[ ]:


#Validador de entrada
Validador_Num = False
while Validador_Num == False:
    try:
        termos = int(input('Digite a quantidade de termos: '))
        if termos >= 0:
            Validador_Num = True
            denom = 2
    except ValueError:
        print('Favor digitar um número natural!')

#Função
def função(termos,denom):
    import math
    res = math.inf
    while (termos > 0):
        res = denom + 1/res
        termos = termos-1
    res = res - 1
    return res
print(função(termos,denom))


# ## 4.10
# 
# $$5,4321 = 5+{1\over 2+{1\over 3+{1\over 5+{1\over 2 + {1\over 127}}}}}$$

# 

# In[ ]:





# ## 4.11
# 
# $${tan(x)} = {1\over {1\over x} - {1\over {3\over x} - {1\over {5\over x} - ...}}}$$

# 

# In[ ]:





# ## 4.12
# 
# $$e = 2+{2\over 2+{3\over 3+{4\over 4+{5\over 5+...}}}} $$

# 

# 

# In[51]:


#Validador de entrada
Validador_Num = False
while Validador_Num == False:
    try:
        termos = int(input('Digite a quantidade de termos: '))
        if termos >= 0:
            Validador_Num = True
            denom = 2
    except ValueError:
        print('Favor digitar um número natural!')

#função
def exercicio_4_2_1(termos,denom):
    import math
    res = math.inf
    while (termos > 0):
        res = denom + (denom+1)/res
        termos -= 1
    return res
print(exercicio_4_2_1(termos,denom))


# In[ ]:




