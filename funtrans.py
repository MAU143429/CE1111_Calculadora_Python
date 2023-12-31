import numpy as np
import math

pi_t = 3.14159265358979323846
eps_t = 2.2204e-16
iterMax = 2500
tol = 1e-8


# La funcion div_t aproxima el valor de 1/a
# Sintaxis de la funcion: div_t(a)
# Parámetros de entrada:
#         a  numero real
# Parametros de salida:
#         0  = En caso de que no valores mayores a 200!
#         skNew = el valor de la aproximacion de 1/a
def div_t(a):

    if(a!=0):
        negFlag = False

        if a < 0:
            a = abs(a)
            negFlag = True

        if -1 < a <= np.math.factorial(20):
            x0 = eps_t**2
        elif np.math.factorial(20) < a <= np.math.factorial(40):
            x0 = eps_t**4
        elif np.math.factorial(40) < a <= np.math.factorial(60):
            x0 = eps_t**8
        elif np.math.factorial(60) < a <= np.math.factorial(80):
            x0 = eps_t**11
        elif np.math.factorial(80) < a < np.math.factorial(100):
            x0 = eps_t**15
        else:
            return 0

        skNew = x0*(2-a*x0)
        sk = x0

        for n in range(iterMax):
            skNew = sk*(2-a*sk)
            if (abs(skNew-sk) < (tol*abs(skNew))):
                sk = skNew
                if negFlag:
                    skNew *= -1
                return skNew
            else:
                sk = skNew
    else:
        return "x debe ser diff 0"
            

# La funcion exp_t aproxima el valor de e^a
# Sintaxis de la funcion: exp_t(a)
# Parámetros de entrada:
#         a  numero real
# Parametros de salida:
#         sk = el valor de la aproximacion de e^a
def exp_t(a):

    sk = 0
    for n in range(iterMax):
        sk_n = sk + ((a**n)/(np.math.factorial(n)))
        if abs(sk_n-sk) < tol:
            sk = sk_n
            return sk
        else:
            sk = sk_n

# La funcion ln_t aproxima el valor de ln(a)
# Sintaxis de la funcion: ln_t(a)
# Parámetros de entrada:
#         a  numero real positivo y diferente de 0
# Parametros de salida:
#         sk = el valor de la aproximacion de ln(a)
def ln_t(a):
    if (a!=0 and a>-1):
        sk_const = (2*(a-1)*div_t((a+1)))
        sk = 0
        for n in range(iterMax):
            sk_n = sk + ((1*div_t((2*n+1))) * (((a-1)*div_t((a+1))) ** (2*n)))
            if abs((sk_n * sk_const) - (sk * sk_const)) < tol:
                sk = sk_n
                return sk * sk_const
            else:
                sk = sk_n
        return sk * sk_const
    else:
        if (a==0):
            return "x debe ser diff de 0"
        else:
            return "x debe ser > -1"

# La funcion log_t aproxima el valor de log_x(a)
# Sintaxis de la funcion: log_t(a)
# Parámetros de entrada:
#         a  numero real positivo y diferente de 0
#         x  numero real positivo y diferente de 0
# Parametros de salida:
#         ln_t(x)/ln_t(a) = el resultado equivalente a log_x(a)
def log_t(x, a):
    if (x==1):
        return 0
    elif(a==0):
        return "a debe ser diff 0"
    elif(a==1):
        return "a debe ser diff 1"
    else:
        numerator = ln_t(x)
        denominator = ln_t(a)
        return numerator * div_t(denominator)

# La funcion power_t aproxima el valor de x**y
# Sintaxis de la funcion: power_t(a)
# Parámetros de entrada:
#         x  numero real 
#         y  numero real 
# Parametros de salida:
#         sk = la aproximacion de x**y 
def power_t(x, y):
    
    if(x==0 and y ==0):
        return "indeterminado"
    elif (x==0 or x==1):
        return x
    elif(y==0):
        return 1
    if(y % 1 == 0 and y > 0):
        sk = 1
        for n in range(int(y)):
            sk *= x
    else:
        sk = exp_t(y*ln_t(abs(x)))
    return sk


# La funcion dominio se encarga de ajustar el dominio de 0 a 2pi 
# Sintaxis de la funcion: dominio(a)
# Parámetros de entrada:
#         a valor de entrada inicial
# Parametros de salida:
#         a valor modificado para estar en el rango
def dominio(a):
    
    sk = 0
    while a < 0 or a > (2*pi_t):
        if a < 0:
            a = a + (2*pi_t)
        elif a > (2*pi_t):
            a = a - (2*pi_t)
        else:
            return a
    return a

def pimids_t(a):
    pidos = pi_t*0.5
    if(abs(abs(a)-pidos)<tol):
        return True
    else:
        return False


# La funcion sin_t aproxima el valor de sen(a)
# Sintaxis de la funcion: sin_t(a)
# Parámetros de entrada:
#         a  numero real
# Parametros de salida:
#         sk = el valor de la aproximacion de sin(a)
def sin_t(a):
    
    sk = 0
    a = dominio(a)
    if(abs(abs(a)-pi_t)<tol):
        return 0
    else:
        for n in range(0, iterMax):
            sig = (-1)**n
            den = a**((2*n)+1)
            fact = math.factorial((2*n)+1)
            skn = sk + sig * (den * div_t(fact))
            if abs(skn-sk) < tol:
                sk = skn
                break
            sk = skn

        return sk

# La funcion cos_t aproxima el valor de cos(a)
# Sintaxis de la funcion: cos_t(a)
# Parámetros de entrada:
#         a  numero real
# Parametros de salida:
#         sk = el valor de la aproximacion de cos(a)
def cos_t(a):
    
    sk = 0
    a = dominio(a)
    if(pimids_t(a)):
        return 0
    else:
        for n in range(0, iterMax):
            sig = (-1)**n
            den = a**(2*n)
            fact = math.factorial(2*n)
            skn = sk + sig * (den * div_t(fact))
            if abs(skn-sk) < tol:
                sk = skn
                break
            sk = skn
        print(n)
        return sk

# La funcion tan_t aproxima el valor de tan(a)
# Sintaxis de la funcion: tan_t(a)
# Parámetros de entrada:
#         a  numero real
# Parametros de salida:
#         sk = el valor de la aproximacion de tan(a)
def tan_t(a):
    
    cos = cos_t(a)
    if cos != 0:
        sk = sin_t(a)*div_t(cos_t(a))
    else:
        return "Fuera del dominio"
    return sk

# La funcion atan_t aproxima el valor de arctan(a)
# Sintaxis de la funcion: atan_t(a)
# Parámetros de entrada:
#         a  numero real
# Parametros de salida:
#         sk = el valor de la aproximacion de arctan(a)
def atan_t(a):
    
    sk = 0
    if -1 < a < 1:
        for n in range(0, iterMax):
            sig = (-1)**n
            den = a**((2*n)+1)
            fact = (2*n)+1
            skn = sk + sig * (den * div_t(fact))
            if abs(skn-sk) < tol:
                sk = skn
                break
            sk = skn

    elif a > 1:
        for n in range(0, iterMax):
            sig = (-1)**n
            fact = ((2*n)+1)*(a**((2*n)+1))
            skn = sk + sig * (1 * div_t(fact))
            if abs(skn-sk) < tol:
                sk = skn
                break
            sk = skn
        sk = (pi_t * div_t(2)) - sk
    elif a < -1:
        for n in range(0, iterMax):
            sig = (-1)**n
            fact = ((2*n)+1)*(a**((2*n)+1))
            skn = sk + sig * (1 * div_t(fact))
            if abs(skn-sk) < tol:
                sk = skn
                break
            sk = skn
        sk = -(pi_t * div_t(2)) - sk
    return sk

# La funcion sinh_t aproxima el valor de sinh(a)
# Sintaxis de la funcion: sinh_t(a)
# Parometros de entrada:
#         a = nomero real
# Parometros de salida:
#         sk = aproximacion del valor sinh_t(a)

def sinh_t(a):
    
    sk = 0
    for n in range(iterMax):
        sk_n = sk + ((a**(2*n+1))*div_t(np.math.factorial(2*n+1)))
        if abs(sk_n - sk) < tol:
            er = abs(sk_n - sk)
            sk = sk_n
            # print("El valor aproximado de sinh_t(a) es: ", sk)
            return sk
        sk = sk_n

# La funcion cosh_t aproxima el valor de cosh_t(a)
# Sintaxis de la funcion: cosh_t(a)
# Parometros de entrada:
#         a = nomero real
# Parometros de salida:
#         sk = aproximacion del valor cosh_t(a)


def cosh_t(a):
    
    sk = 0
    for n in range(iterMax):
        sk_n = sk + ((a**(2*n))*div_t(np.math.factorial(2*n)))
        if abs(sk_n - sk) < tol:
            er = abs(sk_n - sk)
            sk = sk_n
            # print("El valor aproximado de cosh_t(a) es: ", sk)
            return sk
        sk = sk_n


# La funcion tanh_t aproxima el valor de tanh_t(a)
# Sintaxis de la funcion: tanh_t(a)
# Parometros de entrada:
#         a = nomero real
# Parometros de salida:
#         sk = aproximacion del valor tanh_t(a)
def tanh_t(a):


    sk = sinh_t(a)*div_t(cosh_t(a))
    # print("El valor aproximado de tanh_t(a) es: ", sk)
    return sk


# La funcion sec_t aproxima el valor de sec_t(a)
# Sintaxis de la funcion: sec_t(a,iterMax,tol)
# Parometros de entrada:
#         a = nomero real
# Parometros de salida:
#         sk = aproximacion del valor sec_t(a)
def sec_t(a):
    
    coseno = cos_t(a)
    if(coseno != 0):
        sk = div_t(coseno)
        # print("El valor aproximado de sec_t(a) es: ", sk)
        return sk
    else: return "fuera del dominio"


# La funcion csc_t aproxima el valor de csc_t(a)
# Sintaxis de la funcion: csc_t(a,iterMax,tol)
# Parámetros de entrada:
#         a = nomero real
# Parametros de salida:
#         sk = aproximacion del valor csc_t(a)
def csc_t(a):
    seno = sin_t(a)
    if(seno!=0):

        sk = div_t(seno)
        return sk
    else: return "fuera del dominio"

# La funcion root_t aproxima el valor de root(a,n)
# Sintaxis de la funcion: root_t(x,y)
# Parámetros de entrada:
#         x numero real positivo 
#         y raiz nesima que se desea usar
# Parametros de salida:
#         sk = el valor de la aproximacion de root(a)
def root_t(x, y):
    if(y%2==0):
        if(x<0):
            return "x debe ser >= 0"
    if y % 1 == 0 and y > 0:
        y = int(y)
        sk = x*div_t(2)
        for i in range(iterMax):
            sk_n = sk - (sk**y - x)*(1*div_t(y*power_t(sk, y-1)))
            if abs(sk_n - sk) < tol:
                er = abs(sk_n - sk)
                sk = sk_n

                return sk
            sk = sk_n
    else:
        result = power_t(x,div_t(y))
        return result

# La funcion sqrt_t aproxima el valor de raizcuadrada(a)
# Sintaxis de la funcion: sqrt_t(a)
# Parámetros de entrada:
#         a numero real positivo
# Parametros de salida:
#         sk = el valor de la aproximacion de sqrt_t(a)
def sqrt_t(a):

    return root_t(a, 2)

# La funcion asin_t aproxima el valor de arcsen(a)
# Sintaxis de la funcion: asin_t(a)
# Parometros de entrada:
#         a = nomero real
# Parometros de salida:
#         sk = aproximacion del valor arcsen(a)
def asin_t(x):
    
    sk = 0
    if -1 <= x <= 1:
        for n in range(0, iterMax):
            sk_n = sk + (((math.factorial(2*n)))*(1*(div_t((4**n)
                         * (math.factorial(n)**2)*((2*n)+1))))*(x**((2*n)+1)))
            if abs(sk_n - sk) < tol:
                er = abs(sk_n - sk)
                sk = sk_n
                return sk
            sk = sk_n
        return sk
    else:
        return "fuera del dominio"

# La funcion asin_t aproxima el valor de arccos(a)
# Sintaxis de la funcion: acos_t(a)
# Parometros de entrada:
#         a = nomero real
# Parometros de salida:
#         sk = aproximacion del valor arccos(a)
def acos_t(x):
    if -1 <= x <= 1:

        return (pi_t*div_t(2)) - asin_t(x)
    else:
        return "fuera del dominio"

# La funcion cos_t aproxima el valor de cos_t(a)
# Sintaxis de la funcion: cos_t(a,iterMax,tol)
# Parámetros de entrada:
#         a = nomero real
# Parametros de salida:
#         sk = aproximacion del valor cot_t(a)
def cot_t(a):
    tangente = tan_t(a)
    if tangente != 0:
        sk = 1*div_t(tangente)
        return sk
    else: return "fuera del dominio"
