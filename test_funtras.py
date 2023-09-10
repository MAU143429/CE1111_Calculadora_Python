from funtrans import *


# Calcula la raíz cúbica de la expresión (cos(3/7) + ln(2)) y la almacena en la variable 'raiz'
raiz = root_t((cos_t(3 * div_t(7))) + ln_t(2), 3)

# Calcula el seno hiperbólico de la raíz cuadrada de 2 y lo almacena en la variable 'sinh'
sinh = sinh_t(sqrt_t(2))

# Calcula la arcotangente de la exponencial de -1 y lo almacena en la variable 'atan'
atan = atan_t(exp_t(-1))

# Realiza una operación que multiplica 'raiz' por 'sinh' y luego le suma 'atan', almacenando el resultado en 'test_official'
test_official = (raiz * div_t(sinh)) + atan

# Imprime el valor de 'test_official'
print(test_official)