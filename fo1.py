import time
import timeit
t0 = time.clock()
def function_to_repeat():
  max = 0
  min = 10000
  tempTall = 0
  for N in range(1,100000):
    # print("=================")
    S_N = 0
    S_8_N = 0
    N_string = str(N)
    N_8 = 8 * N
    N_8_string = str(N_8)
    # S(N):
    for i in range(len(N_string)):
      S_N += int(N_string[i])
    #print("S("+ str(N) +") = " + str(S_N))
    
    # S(8*N):
    for i in range(len(N_8_string)):
      S_8_N += int(N_8_string[i])
    #print("S("+ str(N_8) +") = " + str(S_N))

    # S(8*N)/S(N)
    tempTall = float(S_8_N)/float(S_N)

    if(tempTall > max):
      max = tempTall
    if(tempTall < min):
      min = tempTall
    # print('N: ' + str(N) + ", S(" + str(N) + ") = " + str(S_N) + ",\t S(8*" + str(N) + ") = S(" + str(N_8) + ") = " + str(S_8_N) + ",\t tempTall = " + str(tempTall)) 

duration = timeit.timeit(function_to_repeat, number= 10)
print("Duration: " + str(duration))
t1 = time.clock()

print("This code segment took " + str(t1-t0) + " to execude!")
# print("Max number is: " + str(max))
# print("And min number is: " + str(min))