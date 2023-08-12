import numpy
import numbers
import math
pi_t = 3.14159265358979323846


def dominio(a):
    sk = 0
    # n=3
    while a < 0 or a > (2*pi_t):
        if a < 0:
            a = a + (2*pi_t)
        elif a > (2*pi_t):
            a = a - (2*pi_t)
        else:
            return a
    return a


def sen_t(a, iterMax, tol):
    sk = 0
    # n=3
    a = dominio(a)

    for n in range(0, iterMax):
        sig = (-1)**n
        den = a**((2*n)+1)
        fact = math.factorial((2*n)+1)
        skn = sk + sig * (den/fact)
        if abs(skn-sk) < tol:
            sk = skn
            break
        sk = skn

    return sk


def cos_t(a, iterMax, tol):
    sk = 0
    # n=3
    a = dominio(a)

    for n in range(0, iterMax):
        sig = (-1)**n
        den = a**(2*n)
        fact = math.factorial(2*n)
        skn = sk + sig * (den/fact)
        if abs(skn-sk) < tol:
            sk = skn
            break
        sk = skn

    return sk


def atan_t(a, iterMax, tol):
    sk = 0
    # n=3
    # a = dominio(a)

    if -1 < a < 1:
        for n in range(0, iterMax):
            sig = (-1)**n
            den = a**((2*n)+1)
            fact = (2*n)+1
            skn = sk + sig * (den/fact)
            if abs(skn-sk) < tol:
                sk = skn
                break
            sk = skn

    elif a > 1:
        for n in range(0, iterMax):
            sig = (-1)**n
            fact = ((2*n)+1)*(a**((2*n)+1))
            skn = sk + sig * (1/fact)
            if abs(skn-sk) < tol:
                sk = skn
                break
            sk = skn
        sk = (pi_t/2) - sk
    elif a < -1:
        for n in range(0, iterMax):
            sig = (-1)**n
            fact = ((2*n)+1)*(a**((2*n)+1))
            skn = sk + sig * (1/fact)
            if abs(skn-sk) < tol:
                sk = skn
                break
            sk = skn
        sk = -(pi_t/2) - sk

    return sk

# La funcion sinh_t aproxima el valor de sinh(a)
# Sintaxis de la funcion: sinh_t(a,iterMax,tol)
# Parometros de entrada:
#         a = nomero real
#         iterMax = nomero entero positivo, que representa la cantidad de iteraciones moximas del motodo
#         tol =  nomero real positivo, que es el criterio de parada del error, donde |S_(k+1)-S_(k)|<tol
# Parometros de salida:
#         sk = aproximacion del valor sinh_t(a)
#         er = error dado por la formula |S_(k+1)-S_(k)|
#         n = cantidad de iteraciones realizadas


def sinh_t(a, iterMax, tol):
    sk = 0
    for n in range(iterMax):
        sk_n = sk + ((a**(2*n+1))/np.math.factorial(2*n+1))
        if abs(sk_n - sk) < tol:
            er = abs(sk_n - sk)
            sk = sk_n
            # print("El valor aproximado de cosh_t(a) es: ",sk)
            # print("El error es: ",er)
            # print("La cantidad de iteraciones realizadas es: ",n)
            return sk
        sk = sk_n

# La funcion cosh_t aproxima el valor de cosh_t(a)
# Sintaxis de la funcion: cosh_t(a,iterMax,tol)
# Parometros de entrada:
#         a = nomero real
#         iterMax = nomero entero positivo, que representa la cantidad de iteraciones moximas del motodo
#         tol =  nomero real positivo, que es el criterio de parada del error, donde |S_(k+1)-S_(k)|<tol
# Parometros de salida:
#         sk = aproximacion del valor cosh_t(a)
#         er = error dado por la formula |S_(k+1)-S_(k)|
#         n = cantidad de iteraciones realizadas


def cosh_t(a, iterMax, tol):
    sk = 0
    for n in range(iterMax):
        sk_n = sk + ((a**(2*n))/np.math.factorial(2*n))
        if abs(sk_n - sk) < tol:
            er = abs(sk_n - sk)
            sk = sk_n
            # print("El valor aproximado de cosh_t(a) es: ",sk)
            # print("El error es: ",er)
            # print("La cantidad de iteraciones realizadas es: ",n)
            return sk
        sk = sk_n


# La funcion tanh_t aproxima el valor de tanh_t(a)
# Sintaxis de la funcion: tanh_t(a,iterMax,tol)
# Parometros de entrada:
#         a = nomero real
#         iterMax = nomero entero positivo, que representa la cantidad de iteraciones moximas del motodo
#         tol =  nomero real positivo, que es el criterio de parada del error, donde |S_(k+1)-S_(k)|<tol
# Parometros de salida:
#         sk = aproximacion del valor tanh_t(a)
def tanh_t(a, iterMax, tol):
    sk = sinh_t(a, iterMax, tol)/cosh_t(a, iterMax, tol)
    print("El valor aproximado de tanh_t(a) es: ", sk)
    return sk

# La funcion sec_t aproxima el valor de sec_t(a)
# Sintaxis de la funcion: sec_t(a,iterMax,tol)
# Parometros de entrada:
#         a = nomero real
#         iterMax = nomero entero positivo, que representa la cantidad de iteraciones moximas del motodo
#         tol =  nomero real positivo, que es el criterio de parada del error, donde |S_(k+1)-S_(k)|<tol
# Parometros de salida:
#         sk = aproximacion del valor sec_t(a)


def sec_t(a, iterMax, tol):
    sk = 1/cos_t(a, iterMax, tol)
    print("El valor aproximado de sec_t(a) es: ", sk)
    return sk


# La funcion csc_t aproxima el valor de csc_t(a)
# Sintaxis de la funcion: csc_t(a,iterMax,tol)
# Parometros de entrada:
#         a = nomero real
#         iterMax = nomero entero positivo, que representa la cantidad de iteraciones moximas del motodo
#         tol =  nomero real positivo, que es el criterio de parada del error, donde |S_(k+1)-S_(k)|<tol
# Parometros de salida:
#         sk = aproximacion del valor csc_t(a)
def csc_t(a, iterMax, tol):
    sk = 1/sen_t(a, iterMax, tol)
    print("El valor aproximado de csc_t(a) es: ", sk)
    return sk


ap = 120
iterMaxp = 2500
tolp = 1e-8

print(dominio(ap))
print(atan_t(ap, iterMaxp, tolp))
