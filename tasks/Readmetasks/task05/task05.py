import cmath

a = int(input("a-ni daxil et"))
b = int(input(" b-ni"))
c = int(input(" c-ni"))
 
d = (b**2) - (4*a*c)

s1 = (-b-cmath.sqrt(d))/(2*a)
s2 = (-b+cmath.sqrt(d))/(2*a)
print('heller {0} ve {1}'.format(s1,s2))