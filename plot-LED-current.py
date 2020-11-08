import matplotlib.pyplot as plt
import numpy as np

x, y, z = np.loadtxt('led-current.csv', delimiter=',', unpack=True)
plt.plot(x,z, label='LED Current')

plt.xlabel('Vin (V)')
plt.ylabel('LED Current (ma)')
plt.title('MOSFET Current Source')
plt.legend()
plt.show()
