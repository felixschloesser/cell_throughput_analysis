import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy


df_450 = pd.read_csv('450.csv', sep=',',header=None)
df_800 = pd.read_csv('800.csv', sep=',',header=None)
df_1800 = pd.read_csv('1800.csv', sep=',',header=None)
df_2600 = pd.read_csv('2600.csv', sep=',',header=None)

avrg_cell_throughput_450 = df_450.values[0]
avrg_cell_throughput_800 = df_800.values[0]
avrg_cell_throughput_1800 = df_1800.values[0]
avrg_cell_throughput_2600 = df_2600.values[0]

linspace = np.linspace(0,100,100)

fig=plt.figure()
ax1 = plt.subplot(411)
ax2 = plt.subplot(412)
ax3 = plt.subplot(413)
ax4 = plt.subplot(414)

ax1.hist(avrg_cell_throughput_450, bins=100, histtype='step', color='tab:blue', label='450MHz')
ax2.hist(avrg_cell_throughput_800, bins=100, histtype='step', color='tab:red', label='800MHz')
ax3.hist(avrg_cell_throughput_1800, bins=100, histtype='step', color='tab:green',label='1800 MHz')
ax4.hist(avrg_cell_throughput_2600, bins=100, histtype='step', color='tab:pink',label='1800 MHz')

ax1.set_ylim(top=10)
ax2.set_ylim(top=10)
ax3.set_ylim(top=10)
ax4.set_ylim(top=10)

ax1.get_shared_x_axes().join(ax1, ax2)

ax1.set_xticklabels([])
ax2.set_xticklabels([])
ax3.set_xticklabels([])

ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()

plt.xlabel('average throughput')


plt.show()