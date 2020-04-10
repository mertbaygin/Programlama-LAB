import sympy as sym
from sympy import Symbol
from sympy import pprint
import sympy.plotting as syp
%matplotlib inline
import matplotlib.pyplot as plt

sigma = Symbol('sigma')
x = Symbol('x')
mu = Symbol('mu')
sym.sqrt(2*sym.pi*sigma)

part_1 = 1/(sym.sqrt(2*sym.pi*sigma**2))
part_2 = sym.exp(-1*((x-mu)**2)/(2*sigma**2))

my_gauss_function = part_1 * part_2
# pprint(my_gauss_function)

# Fonksiyonun grafiği için
syp.plot(my_f.subs({mu:1,sigma:30}),(x,-10,10),title='gauss')


# fonksiyonun döngü ile yapımı
x_values = []
y_values = []
for value in range(-100,100):
    y =my_f.subs({mu:10,sigma:30,x:value})
    y_values.append(y)
    x_values.append(value)
    print(x,y)

plt.plot(x_values,y_values)