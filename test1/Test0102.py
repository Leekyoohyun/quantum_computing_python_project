# 맥북에 기본적으로 설치된 AppleGothic 폰트를 사용하여 다시 시도

import matplotlib.pyplot as plt
import networkx as nx

import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]

for t in np.arange(0,9,0.5):
    x.append(np.cos(t))
    y.append(np.sin(t))

plt.scatter(x,y)
plt.show()