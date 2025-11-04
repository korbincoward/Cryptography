from sympy.ntheory import discrete_log

p = 42443 #modulus
h = 42
g = 3
print(discrete_log(p, h, g))
