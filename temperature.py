import math
import numpy as np
import matplotlib.pyplot as plt
L = 0.3
h = 15
P = 0.03*4
A = 0.03**2
k = 200
m = math.sqrt((h*P)/(k*A))
tInf = 300
tempBase = 350
thetaB = tempBase-tInf
temperatures = []
divisions = np.linspace(0, 0.3, 60)

for i in divisions:
    p1 = math.cosh(m*(L-i)) + ((h/(m*k))*math.sinh(m*(L-i)))
    p2 = math.cosh(m*L) + ((h/(m*k))*math.sinh(m*L))
    temperatures.append(((p1/p2)*thetaB)+tInf)


print('Temperature in L/2: ' + str(temperatures[29]))
plt.plot(divisions, temperatures)
plt.xlabel('X')
plt.ylabel('Temperatures')
plt.show()