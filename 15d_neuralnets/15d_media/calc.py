import numpy as np

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

x = np.array([0.3, 0.6])
print(f"Input = {x}")
x = np.insert(x, 0, 1)
layer1 = np.array([[0.2, -2.1, 1.4], [-0.4, 1.1, 2.2]])
z1 = layer1 @ x
print(f"Hidden z = {z1}")
out1 = sigmoid(z1)
print(f"Hidden out = {out1}")
out1 = np.insert(out1, 0, 1)
layer2 = np.array([-0.1, 3.1, -1.2])
z2 = layer2 @ out1
print(f"Output z = {z2}")
out2 = sigmoid(z2)
print(f"Output output = {out2}")
