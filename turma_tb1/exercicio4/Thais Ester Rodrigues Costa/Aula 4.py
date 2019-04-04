#!/usr/bin/env python
# coding: utf-8

# Exercício 1

# In[4]:


a = int (input ("Primeiro valor:"))
b = int (input ("Segundo valor:"))
if a > b:
    print ("O primeiro valor é maior")
if a < b:
    print ("o segundo valor é maior")
if a ==b:            
    print ("a e b são iguais")


# Exercício 5

# In[5]:


a = int (input ("Digite o primeiro valor:"))
b = int (input ("Digite o segundo valor:"))
c = int (input ("Digite o terceiro valor:"))
if a > b:
    print ("O primeiro valor é maior")
else :
    print ("O segundo valor é menor ou igual ao primeiro")
if b > c:
    print ("O segundo valor é maior")
else: 
    print ("O terceiro valor é menor ou igual que o primeiro")
if c > a:
    print ("O terceiro valor é maior")
else:
    print (" O primeiro valor é menor ou igual ao primeiro")
    


# Exercício 6
# 

# In[7]:


num = int (input ("Digite um número"))
if num % 2!= 0:
    print ("O número é ímpar")
else:
    print ("O número não é ímpar")
    


# Execício 7

# In[12]:


def bissexto ():
    ano =  int (input ("Digite um ano:"))
if ano % 4 == 0:
    print ("O ano é bissexto")
else :
    print ("O ano não é bissexto")
if ano % 100 == 0:
    print ("O ano é bissexto")
else :
    print ("O ano não é bissexto")
if ano % 400 == 0:
    print ("O ano é bissexto")
else:
    print ("O ano não é bissexto")
        
    


# Exercício 3

# In[ ]:


salário = float(input("Digite o salário para calcular" " o imposto: "))
base_de_cálculo = salário 
imposto = 0 
if base_de_cálculo > 3000: 
    imposto = imposto + ((base_de_cálculo - 3000) * 0.35) 
    base_de_cálculo = 3000 if base_de_cálculo > 1000: 
        imposto = imposto + ((base_de_cálculo - 1000) * 0.20)
        print("O salário de R$%6.2f pagará R$%6.2f de " "impostos." % (salário,imposto))


# Exercício 4

# In[ ]:


categoria = int(input("Digite a categoria: ")) 
if categoria == 1:
    preço = 10
elif categoria == 2:
    preço = 18
elif categoria == 3:
    preço = 23
elif categoria == 4:
    preço == 26
elif categoria == 5:
    preço = 31 
else:
    print("Categoria inválida! Digite um valor entre 1 e 5!")
    preço = -1
    print("O preço do produto é R$%6.2f"  % preço)


# In[ ]:




