import matplotlib.pyplot as plt

yaxis = [134.2,117.3, 109.1, 101.1, 99.1, 95.7, 88.6, 86.7, 63.8, 56.2]
xaxis = [0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.18, 0.2, 0.5, 1]

plt.plot(xaxis, yaxis, '--')
plt.savefig('data.png')
