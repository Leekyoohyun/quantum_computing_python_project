from numpy import array
import pandas as pd

ket0 = array([1,0])
ket1 = array([0,1])
result = ket0/2+ket1/2
print(result)