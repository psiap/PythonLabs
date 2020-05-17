#6.	С помощью модуля numPy реализуйте следующие операции: 
#1) умножение произвольных матриц А (размерности 3х5) и В (5х2); 
#2) умножение матрицы (5х3) на трехмерный вектор; 
#3) решение произвольной системы линейных уравнений; 
#4) расчет определителя матрицы; 
#5) получение обратной и транспонированной матриц. 
#
#Также продемонстрируйте на примере матрицы 5х5 тот факт, 
#что определитель равен произведению собственных значений матрицы. 

import numpy as np
from numpy import *
class matrix(object):
    def __init__(self):
        pass
    #1) 
    def multiplication(self):
        return np.dot(np.ones((3,5)),np.ones((5,2)))

    #2) 
    def multiplication_vector(self):
        return np.dot(np.ones((5,3)),np.array([1, 2, 3]))

    #3)
    def linear_equation(self):
        #Матрица (левая часть системы) / Вектор (правая часть системы)
        return np.linalg.solve(np.array([[2., 5.], [1., -10.]]), np.array([1., 3.]))

    #4)
    def determinant_matrix(self):
        return np.linalg.det(np.arange(9).reshape(3,3))

    #5)
    def revers_matrix(self):
        return (np.linalg.inv(np.linalg.inv(np.matrix('1. -3.; 2. 5.').T))).T

    #6)
    def res_m(self):
        matrix = np.mat ([[-1, -6], [2, 6]])
        w, v = np.linalg.eig (matrix)
        return w, v


g = matrix()
print(g.res_m())