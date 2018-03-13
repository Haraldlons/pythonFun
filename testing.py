import numpy as np

l = [1,2,3,4,5,6]
print("L: " + str(l))

print("")
print("l[::2]:")
print(l[::2])

l = np.array(l)
l = np.arange(100)

print("")
print("l[::2]")
print(l[::2])

print("")
print("l.resize(2,3)------------------")
l.resize(10,10)
print(l)

print("")
print("l[::3]")
print(l[:2:])