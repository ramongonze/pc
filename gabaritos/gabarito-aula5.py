"""
    Gabarito dos exercícios da aula 5
    @author: José, Ramon
"""

def exercicio_1_1(n, i):
    if n == 0 or n == 1:
        return 1
    return n * exercicio_1_1(n-1, i)

def exercicio_1_2(n):
    return exercicio_1_1(n, 0)

def exercicio_2(n):
    if n == 1:
        return 1

    if n%2 == 0:
        return -1/n + exercicio_2(n-1)
    else:
        return 1/n + exercicio_2(n-1)

def exercicio_3_1_1(termos):
    """ Calcula a razão áurea e retorna None
        se n <= 0
    """
    res = None
    if termos > 0:
        if termos == 1:
            res = 1
        else:
            res = (1 + exercicio_3_1_1(termos-1))**.5
    return res

def exercicio_3_1_2(termos):
    return exercicio_3_1_1(termos)

def exercicio_3_2_1(termos):
    """ Calcula a razão áurea e retorna None
        se termos <= 0
    """
    res = None
    if termos == 1:
        res = 1
    elif termos > 1:
        res = 1 + 1/exercicio_3_2_1(termos-1)
    return res

def exercicio_3_2_2(termos):
    return exercicio_3_2_1(termos)

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

def exercicio_3_3_1(n):
    """ Calcula o no. de Euler por série.
        Retorna None se termos <= 0
    """
    res = None
    if n == 0:
        res = 1
    elif n == 1: # Evita uma chamada recursiva a mais
        res = 2
    elif n > 0:
        res = 1/fat(n) + exercicio_3_3_1(n-1)
    return res

def exercicio_3_3_2(n):
    return exercicio_3_3_1(n)

#print(exercicio_3_3(20))
def exercicio_3_4_1(k, x):
    """ Calcula e^x por série
        e retorna None se k <= 0
    """
    res = None
    if k == 0:
        res = 1
    elif k == 1: #evita uma chamada recursiva a mais
        res = x+1
    elif k > 1:
        res = x**k/fat(k) + exercicio_3_4_1(k-1, x)
    return res

def exercicio_3_4_2(k, x):
    return exercicio_3_4_1(k, x)

def exercicio_3_5_w(n, sinal):
    """ Calcula a série de potências para e^(-1)
        Retorna None se n <= 0
        Sinal é iniciado com (-1)^n
        1/e          = 0,36787944117144232159552377016146
        exercicio_3_5(1000) = 0.36787944117144245
    """
    res = None
    if n == 0:
        res = sinal
    elif n >= 1:
        res = sinal * 1/fat(n) + exercicio_3_5_w(n-1, -1*sinal)
    return res

def exercicio_3_5_1(n):
    """ wrapper para exercicio_3_5_w(n,sinal), como o sinal == (-1)^n
    """
    return exercicio_3_5_w(n,(-1)**n)

def exercicio_3_5_2(n):
    return exercicio_3_5_1(n)

def exercicio_3_6_w(termos,sinal):
    """ Calcula a parte homogênea da série para pi com tantos
        termos passados como argumento.
        Aqui, termos é o 2o. termo da série. Falta somar 3
        para obter pi. É a função que é envelopada (wrapped)
        por exercicio_3_6. Retorna None se termos <= 0
    """
    res =  None
    if termos == 0:
        res = 0
    elif termos > 0:
        d = 2*termos
        res = sinal*4/(d*(d+1)*(d+2)) + exercicio_3_6_w(termos-1,(-1)*sinal)
    return res
    
def exercicio_3_6_1(termos):
    """ Determina o sinal do termo mais profundo e chama a
        função exercicio_3_6_w para calcular os termos da série de
        pi
    """
    sinal = (-1)**termos
    return 3+exercicio_3_6_w(termos-1,sinal)

def exercicio_3_6_2(termos):
    return exercicio_3_6_1(termos)

def exercicio_3_7_1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return exercicio_3_7_1(n-1) + exercicio_3_7_2(n-2)

def exercicio_3_7_2(n):
    return exercicio_3_7_1(n)

def exercicio_3_8_w(termos):
    """ Calcula a parte homogênea da série para raiz quadrada
        de 3 com tantos termos passados como argumento.
        Aqui, termos é o 2o. termo da série. Falta somar 1
        para obter 1,732. É a função que é envelopada (wrapped)
        por exercicio_3_8. Retorna None se termos <= 0
    """
    res =  None
    if termos == 0:
        res = 0
    elif termos%2 == 1:
        res = 1/(1 + exercicio_3_8_w(termos-1))
    else:
        res = 1/(2 + exercicio_3_8_w(termos-1))
    return res

def exercicio_3_8_1(termos):
    """ Soma 1 ao resultado da chamada da função que calcula 
        a parte homogênea da fração parcial que calcula a 
        raiz de 3, exercicio_3_8_w(termos-1)
    """
    return 1 + exercicio_3_8_w(termos-1)

def exercicio_3_8_2(termos):
    return exercicio_3_8_1(termos)
    
def exercicio_3_8_i(termos):
    import math
    termos -= 1
    res = math.inf
    if termos%2 == 0:
        denom = 2
    else:
        denom = 1
    while termos > 0:
        res = denom + 1/res
        termos -= 1
        if termos%2 == 0:
            denom = 2
        else:
            denom = 1
    return 1 + 1/res

def exercicio_3_9_w(termos):
    """ Calcula a parte homogênea da série para raiz quadrada
        de 2 com tantos termos passados como argumento.
        Aqui, termos é o 2o. termo da série. Falta somar 1
        para obter 1,414. É a função que é envelopada (wrapped)
        por exercicio_3_9. Retorna None se termos <= 0
    """
    res =  None
    if termos == 0:
        res = 0
    elif termos > 0:

        res = 1/(2 + exercicio_3_9_w(termos-1))
    return res

def exercicio_3_9_1(termos):
    """ Soma 1 ao resultado da chamada da função que calcula 
        a parte homogênea da fração parcial que calcula a 
        raiz de 2, exercicio_3_8_w(termos-1)
    """
    return 1 + exercicio_3_9_w(termos-1)

def exercicio_3_9_2(termos):
    return exercicio_3_9_1(termos)
    
def exercicio_3_10_1(termos):
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

def exercicio_3_10_2(termos):
    return exercicio_3_10_1(termos)

def exercicio_3_11_w(x,num,termos):
    """ Calcula a tan(x), on de x é dado em pi radianos,
        por série.
        num é o numerador de cada termo e é dado por
        num = 2*termos-1
        Essa função é envelopada por exercicio_3_11 que inicia o numerador do
        primeiro termo com 1.
        Retorna None se termos <= 0.
    """
    res = None
    if termos == 1:
        res = 1/(num/x)
    elif termos > 1:
        res = 1/(num/x - exercicio_3_11_w(x, num+2, termos-1))
    return res

def exercicio_3_11_1(termos, x):
    """ Wrapper da função exercicio_3_11: inicia o numerador com 1
        tan(pi/3) = sqrt(3)
        tan(2pi/3) = -sqrt(3)
        tan(3pi/4) = -1
        tan(3pi/8) = 1 + sqrt(2)
        tan(5pi/8) = -1 - sqrt(2)
        tan(6pi/7) = -0481574618807529
    """
    return exercicio_3_11_w(x,1,termos)

def exercicio_3_11_2(termos, x):
    return exercicio_3_11_1(termos, x)

def exercicio_3_12_w(termos,num):
    """ Calcula e por outra série. Retorna None se termos<0.
        num é o numerador do termo atual que é usado também
        como denominador.
    """
    res = None
    if termos == 1:
        res = 1
    elif termos > 1:
        res = num/(num + exercicio_3_12_w(termos-1,num+1))
    return res

def exercicio_3_12_1(termos):
    """ Wrapper da função exercicio_3_12_w(termos,num) que só soma
        2 ao resultado da chamada dessa função, inciando num
        com 2.
    """
    return 2+exercicio_3_12_w(termos,2)

def exercicio_3_12_2(termos):
    return exercicio_3_12_1(termos)
