import numpy as np

print(np.zeros((3, 5)))

print(np.eye(3))

a = np.array([20, 30, 40, 50])
print(a < 35)

print(np.sum(a))

Z = np.random.random((3, 3))
print(Z)

Z = np.random.random(10000)
m = Z.mean()
print(m)