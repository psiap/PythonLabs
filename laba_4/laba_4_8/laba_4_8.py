#7 7.	Выберите произвольную дифференцируемую и интегрируемую функцию одной переменной. 
#С помощью модуля symPy найдите и отобразите ее производную и интеграл в аналитическом и графическом виде. 
#Напишите код для решения произвольного нелинейного урванения и системы нелинейных уравнений.
#
# 

from sympy import *

class laba7(object):
    def __init__(self):
        pass

    def work1(self,a):
        x = Symbol('x')
        difura = diff(a, x)
        intura = integrate(a, x)
        print(difura)
        print(intura)

    def work2(self):
        x, y = symbols("x,y")
        print(nsolve((x**3+exp(y)-4,x+3*y),(x,y),(1,1)))
                      #'''Уравнение'''


#Функция
a = 'sin(x)*exp(x)'

g = laba7()

g.work1(a)
g.work2()