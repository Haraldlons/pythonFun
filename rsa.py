import numpy as np
tall = 0
for i in range(2,1000):
	tall = np.mod(i*17,96)
	if tall == 1:
		print("tall: " + str(tall))
		print("i: " + str(i))
		break