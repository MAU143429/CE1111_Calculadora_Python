import math
import numpy as np

pi_t = 3.14159265358979323846
eps_t = 2.2204e-16
iterMax = 2500
tol = 1e-8


def div_t(a):

    if np.math.factorial(0) < a <= np.math.factorial(20):
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
            return skNew
        else:
            sk = skNew


def exp_t(a):

    sk = 0
    for n in range(iterMax):
        sk_n = sk + ((a**n)/(np.math.factorial(n)))
        if abs(sk_n-sk) < tol:
            sk = sk_n
            return sk
        else:
            sk = sk_n


def ln_t(a):

    sk_const = (2*(a-1)*div_t((a+1)))
    sk = 0
    for n in range(iterMax):
        sk_n = sk + ((1*div_t((2*n+1))) * (((a-1)*div_t((a+1))) ** (2*n)))
        if abs((sk_n * sk_const) - (sk * sk_const)) < tol:
            sk = sk_n
            return sk * sk_const
        else:
            sk = sk_n


def log_t(x, a):

    numerator = ln_t(x)
    denominator = ln_t(a)
    return numerator*div_t(denominator)


def power_t(x, y):
    sk = 1
    for n in range(y):
        sk *= x
    return sk


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


def sen_t(a):
    sk = 0
    a = dominio(a)

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


def cos_t(a):
    sk = 0
    a = dominio(a)

    for n in range(0, iterMax):
        sig = (-1)**n
        den = a**(2*n)
        fact = math.factorial(2*n)
        skn = sk + sig * (den * div_t(fact))
        if abs(skn-sk) < tol:
            sk = skn
            break
        sk = skn

    return sk


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


print(dominio(120))
print(atan_t(120))
print(div_t(52000))
print(exp_t(125))
print(ln_t(1000))
print(log_t(1000, 2))
print(power_t(125, 5))
