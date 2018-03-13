import numpy as np


r = np.arange(36)
print("r = np.arange(36):")
print(r)
r = r.reshape(6,6)
print("")
print("r.reshape(6,6):")
print(r)

print("")
print("r[0:6,::-7]:")
print(r[0:6,::-7])

print("")
print("r[:,::7]")
print(r[:,::7])

print("")
print("r[::8]")
print(r[::8])

