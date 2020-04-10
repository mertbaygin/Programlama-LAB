from sympy import Symbol
x = Symbol('x')
y = Symbol('y')

p = x*(x+x)
# print(p) => 2*x**2

p = (x+2)*(x+3)
# print(p) (x+2)*(x+3)

from sympy import factor, expand,pprint
expr = x**2 - y**2
# factor(expr) (x-y)*(x+y)
factors = factor(expr)
expand = expand(factors)

expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3
factors = factor(expr)
# print(factors) => (x+y)**3

x = Symbol('x')
series = x
n=5
for i in range(2,n+1):
    series = series + (x**1)/i
pprint(series)


expr = x*x + x*y + x*y + y*y
res = expr.subs({x:1,y:2})
# print(res) => 9

r = expr.subs({x:1-y})
# print(r) y**2 + 2*y*(-y+1) + (-y+1)**2


x = Symbol('x')
series = x
n=5
x_value = 10
for i in range(2,n+1):
    series = series + (x**1)/i
pprint(series)
series_value = series.subs({x:x_value})
# print(series_value)
