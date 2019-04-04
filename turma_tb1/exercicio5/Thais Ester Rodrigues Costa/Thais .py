#!/usr/bin/env python
# coding: utf-8

# Exercício 2

# In[ ]:


s = [ "ABCDEFGHI"]
print (s[-3::-1])


# In[ ]:


s = [ "ABCDEFGHI"]
print (s[-2:3:-1])


# Exercício 1

# In[26]:


A = "CRUZEIRO"
print (A[:-3])


# In[8]:


print(A[-3:-1]) # contando da direita para a esquerda, informa o segundo e o terceiro caracter 


# In[9]:


print (A[:2])# mostra os dois primeiros caracteres


# In[10]:


print (A[1:])# exclui o primeiro caracter 


# In[11]:


print (A[0:-4]) # mostra do primeiro ao quarto caracter 


# In[13]:


print (A[-1:])#mostra só o último caracter 


# In[14]:


print (A[::-1])# inverte a sequência 


# Exercício 3

# In[31]:


tempo_s = (int (input ("Digite o tempo em segundos:")))
a = tempo_s % 60
tempo_m = tempo_s %60
b = tempo_m %60
print ("o valor do tempo é:", a ,b)


# Exercício 3

# In[ ]:


s = (input("Digite um sequência:") )
A = s[::-1]
if A == s:
    print ("A sequência está no formato adequado!")
else:
    print ("A sequência não atende os parâmetros!")


# Exercício 5

# In[ ]:


from math import sqrt
a = float (input ("Digite um valor:"))
b = float (input ("Digite um valor:"))
c = float (input ("Digite um valor:"))
L = (sqrt ((a**2) + (b**2)))
D = (sqrt ((L**2) + (c**2)))
print ("O valor da diagonal é:", D)


# Exercício 4

# In[ ]:


from datetime import datetime
hora1 = datetime(9:34)
hora2 = datetime(21:41)
difhora = hora2 - hora1
'{0}:{2}'.format(*str(difdata).split())


# In[ ]:




