import matplotlib.pyplot as plt
import numpy as np

x, y, z = np.loadtxt('led-current.csv', delimiter=',', unpack=True)
plt.plot(x-y,z, label='LED Current')

plt.xlabel('Vgs (V)')
plt.ylabel('LED Current (ma)')
plt.title('MOSFET Current Source')
plt.suptitle('calculated Vgs')
plt.legend()
plt.show()
