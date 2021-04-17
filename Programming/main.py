import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style


def u(t):
    """Unit step function"""
    return 1 * (t >= 0)


def delta(t):
    """Unit step function"""
    return 1 * (t == 0)


def linear_step_func(x):
    y= np.piecewise(x, [
        x < -1,
       (x >= -1) & (x <= 1),
        x > 1],
            [-1,
             lambda x: x,
             lambda x: np.cos(x-1)]
       )
    return y


start = -10
end = 10
step = 0.01
x1 = np.linspace(start, end, int((end - start)/step))
y1 = pow(np.e, 0.5 * x1) * u(-1 * x1 + 4)
plt.plot(x1, y1, color="red")
plt.show()

start2 = -4
end2 = 4
x2 = np.linspace(start2, end2, int((end2 - start2)/step))
y2 = linear_step_func(x2)
plt.plot(x2, y2)
plt.show()

start3 = -5
end3 = 5
x3 = np.linspace(start3, end3, int((end3 - start3)/step))
sum = 0
for i in range(-20, 20 + 1):
    sum += np.e ** (-np.abs(2 * x3 + i))
y3 = sum
plt.plot(x3, y3)
plt.show()


start4 = -20
end4 = 20
x4 = np.linspace(start4, end4, int((end4 - start4)/1))
y4 = np.sin(2.3 * np.pi * x4) + np.cos(4.3 * np.pi * x4)
plt.stem(x4, y4)
plt.show()


start5 = -20
end5 = 20
x5 = np.linspace(start5, end5, int((end5 - start5)/1))
y5 = np.sin(4.3 * np.pi * x5) + np.cos(6.3 * np.pi * x5)
plt.stem(x5, y5)
plt.show()


start6 = -20
end6 = 20
x6 = np.linspace(start6, end6, int((end6 - start6)/1))
y6 = u(x6 - 3) - u(-1 * x6 + 3)
plt.stem(x6, y6)
plt.show()
plt.subplots(5)
