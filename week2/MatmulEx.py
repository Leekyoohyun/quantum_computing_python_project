from numpy import matmul
from numpy import *

ket0 = array([1,0])
ket1 = array([0,1])

M1 = array([[1, 1], [0, 0]])
M2 = array([[1, 1], [1, 0]])

print(matmul(M1, ket1))
print(matmul(M1,M2))
print(matmul(M2,M1))