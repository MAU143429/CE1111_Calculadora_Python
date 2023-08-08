import numpy, numbers, math
pi_t = 3.14159265358979323846

def dominio (a):
    sk=0
    #n=3
    while a<0 or a>(2*pi_t):
        if a < 0:
            a = a + (2*pi_t)
        elif a > (2*pi_t):
            a = a - (2*pi_t)
        else:
            return a
    return a

def sen_t (a,iterMax,tol):
    sk=0
    #n=3
    a = dominio(a)

    for n in range(0,iterMax):
        sig = (-1)**n
        den = a**((2*n)+1)
        fact = math.factorial((2*n)+1)
        skn = sk + sig * (den/fact)
        if abs(skn-sk) < tol:
            sk = skn
            break
        sk=skn

        
   
    return sk


def cos_t (a,iterMax,tol):
    sk=0
    #n=3
    a = dominio(a)

    for n in range(0,iterMax):
        sig = (-1)**n
        den = a**(2*n)
        fact = math.factorial(2*n)
        skn = sk + sig * (den/fact)
        if abs(skn-sk) < tol:
            sk = skn
            break
        sk = skn
   
    return sk

def atan_t (a,iterMax,tol):
    sk=0
    #n=3
    #a = dominio(a)

    if -1<a<1:
        for n in range(0,iterMax):
            sig = (-1)**n
            den = a**((2*n)+1)
            fact = (2*n)+1
            skn = sk + sig * (den/fact)
            if abs(skn-sk) < tol:
                sk = skn
                break
            sk = skn
        
    elif a > 1:
        for n in range(0,iterMax):
            sig = (-1)**n
            fact = ((2*n)+1)*(a**((2*n)+1))
            skn = sk + sig * (1/fact)
            if abs(skn-sk) < tol:
                sk = skn
                break
            sk = skn
        sk = (pi_t/2) - sk
    elif a < -1:
        for n in range(0,iterMax):
            sig = (-1)**n
            fact = ((2*n)+1)*(a**((2*n)+1))
            skn = sk + sig * (1/fact)
            if abs(skn-sk) < tol:
                sk = skn
                break
            sk = skn
        sk = -(pi_t/2) - sk
    
    return sk





        
ap = 120
iterMaxp = 2500
tolp = 1e-8

print(dominio(ap))
print(atan_t(ap,iterMaxp,tolp))
