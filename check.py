import numpy as np
import matplotlib.pyplot as plt

def check(l,x=0.3,n=1000):
  a = np.zeros(n)
  for i in range(n):
    x=l*x*(1-x)
  for i in range(n):
    a[i] = x
    x = l*x*(1-x)
  return a

X = np.linspace(3.2,3.8,100)

Y = [check(i) for i in X]
# Y = []
# for i in X:
#   Y.append(check(i))

plt.plot(X,Y,'k.',markersize=0.01,linewidth=None,markerfacecolor='red')
plt.savefig("bif1.png")