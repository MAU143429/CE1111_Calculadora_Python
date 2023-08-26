from funtrans import *


raiz = root_t((cos_t(3*div_t(7)))+ln_t(2),3)
sinh = sinh_t(sqrt_t(2))
atan = atan_t(exp_t(-1))
#test = (root_t(cos_t(3*div_t(7))+ln_t(2),3))*1*div_t(sinh_t(sqrt_t(2)))+atan_t(exp_t(-1))
test_official = (raiz*div_t(sinh))+atan
print(raiz)
print(sinh_t(sqrt_t(2)))
print(atan)

print(test_official)