# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:00:10 2019

@author: José

Exercícios da aula 6
"""

def fat(n):
    """ Calcula o fatorial de n. Retorna None
        se n < 0.
    """
    res = None
    if n == 0 or n == 1:
        res = 1
    elif n > 1:
        res = n * fat(n-1)
    return res

def ex_4_1(termos):
    """ Calcula a razão áurea e retorna None
        se termos <= 0
    """
    res = None
    if termos > 0:
        if termos == 1:
            res = 1
        else:
            res = (1 + ex_4_1(termos-1))**.5
    return res

def ex_4_2(termos):
    """ Calcula a razão áurea e retorna None
        se termos <= 0
    """
    res = None
    if termos == 1:
        res = 1
    elif termos > 1:
        res = 1 + 1/ex_4_2(termos-1)
    return res

def ex_4_3(k):
    """ Calcula o no. de Euler por série.
        Retorna None se termos <= 0
    """
    res = None
    if k == 0:
        res = 1
    elif k == 1: #evita uma chamada recursiva a mais
        res = 2
    elif k > 0:
        res = 1/fat(k) + ex_4_3(k-1)
    return res

#print(ex_4_3(20))
def ex_4_4(x,k):
    """ Calcula e^x por série
        e retorna None se k <= 0
    """
    res = None
    if k == 0:
        res = 1
    elif k == 1: #evita uma chamada recursiva a mais
        res = x+1
    elif k > 1:
        res = x**k/fat(k) + ex_4_4(x,k-1)
    return res

#print(ex_4_4(2,20))
def ex_4_5_w(n,sinal):
    """ Calcula a série de potências para e^(-1)
        Retorna None se n <= 0
        Sinal é iniciado com (-1)^n
        1/e          = 0,36787944117144232159552377016146
        ex_4_5(1000) = 0.36787944117144245
    """
    res = None
    if n == 0:
        res = sinal
    elif n >= 1:
        res = sinal * 1/fat(n) + ex_4_5_w(n-1, -1*sinal)
    return res

def ex_4_5(n):
    """ wrapper para ex_4_5_w(n,sinal), como o sinal == (-1)^n
    """
    return ex_4_5_w(n,(-1)**n)

def ex_4_6_w(termos,sinal):
    """ Calcula a parte homogênea da série para pi com tantos
        termos passados como argumento.
        Aqui, termos é o 2o. termo da série. Falta somar 3
        para obter pi. É a função que é envelopada (wrapped)
        por ex_4_6. Retorna None se termos <= 0
    """
    res =  None
    if termos == 0:
        res = 0
    elif termos > 0:
        d = 2*termos
        res = sinal*4/(d*(d+1)*(d+2)) + ex_4_6_w(termos-1,(-1)*sinal)
    return res
    
def ex_4_6(termos):
    """ Determina o sinal do termo mais profundo e chama a
        função ex_4_6_w para calcular os termos da série de
        pi
    """
    sinal = (-1)**termos
    return 3+ex_4_6_w(termos-1,sinal)

#print(ex_4_6(2959))

def ex_4_8_w(termos):
    """ Calcula a parte homogênea da série para raiz quadrada
        de 3 com tantos termos passados como argumento.
        Aqui, termos é o 2o. termo da série. Falta somar 1
        para obter 1,732. É a função que é envelopada (wrapped)
        por ex_4_8. Retorna None se termos <= 0
    """
    res =  None
    if termos == 0:
        res = 0
    elif termos%2 == 1:
        #print(f't: {termos} res: {1/(1+f(t-1))})
        res = 1/(1 + ex_4_8_w(termos-1))
    else:
        res = 1/(2 + ex_4_8_w(termos-1))
    return res

def ex_4_8(termos):
    """ Soma 1 ao resultado da chamada da função que calcula 
        a parte homogênea da fração parcial que calcula a 
        raiz de 3, ex_4_8_w(termos-1)
    """
    return 1 + ex_4_8_w(termos-1)

#print(ex_4_8(100))

def ex_4_9_w(termos):
    """ Calcula a parte homogênea da série para raiz quadrada
        de 2 com tantos termos passados como argumento.
        Aqui, termos é o 2o. termo da série. Falta somar 1
        para obter 1,414. É a função que é envelopada (wrapped)
        por ex_4_9. Retorna None se termos <= 0
    """
    res =  None
    if termos == 0:
        res = 0
    elif termos > 0:

        res = 1/(2 + ex_4_9_w(termos-1))
    return res

def ex_4_9(termos):
    """ Soma 1 ao resultado da chamada da função que calcula 
        a parte homogênea da fração parcial que calcula a 
        raiz de 2, ex_4_8_w(termos-1)
    """
    return 1 + ex_4_9_w(termos-1)

#print(ex_4_9(100))
    
def ex_4_10(termos):
    """ Calcula o valor de 5,4321 por sua fração contínua,
        dado o númro de termos como argumento. Retona None
        se termos < 0
    """
    res =  None
    if termos == 0:
        res = 0
    elif termos == 1:
        res = 5
    elif termos == 2:
        res = 5 + 1/2
    elif termos == 3:
        res = 5 + 1/(2+1/3)
    elif termos == 4:
        res = 5 + 1/(2+1/(3+1/5))
    elif termos == 5:
        res = 5 + 1/(2+1/(3+1/(5+1/2)))
    elif termos > 5:
        res = 5 + 1/(2+1/(3+1/(5+1/(2+1/127))))
    return res

#print(ex_4_10(6))

def ex_4_11_w(x,num,termos):
    """ Calcula a tan(x), on de x é dado em pi radianos,
        por série.
        num é o numerador de cada termo e é dado por
        num = 2*termos-1
        Essa função é envelopada por ex_4_11 que inicia o numerador do
        primeiro termo com 1.
        Retorna None se termos <= 0.
    """
    res = None
    if termos == 1:
        res = x
    elif termos > 1:
        res = 1/(num/x - ex_4_11_w(x, num+2, termos-1))
    return res

def ex_4_11(x,termos):
    """ Wrapper da função ex_4_11: inicia o numerador com 1
        tan(pi/3) = sqrt(3)
        tan(2pi/3) = -sqrt(3)
        tan(3pi/4) = -1
        tan(3pi/8) = 1 + sqrt(2)
        tan(5pi/8) = -1 - sqrt(2)
        tan(6pi/7) = -0481574618807529
    """
    return ex_4_11_w(x,1,termos)

#print(ex_4_11(6*3.141592653589793/7,100))

def ex_4_12_w(termos,num):
    """ Calcula e por outra série. Retorna None se termos<0.
        num é o numerador do termo atual que é usado também
        como denominador.
    """
    res = None
    if termos == 1:
        res = 1
    elif termos > 1:
        res = num/(num + ex_4_12_w(termos-1,num+1))
    return res

def ex_4_12(termos):
    """ Wrapper da função ex_4_12_w(termos,num) que só soma
        2 ao resultado da chamada dessa função, inciando num
        com 2.
    """
    return 2+ex_4_12_w(termos,2)



for i in range(1,5):
    web.tel