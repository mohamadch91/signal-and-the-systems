import numpy as np
import matplotlib.pyplot as plt
t_1 = np.arange(-10, 10, step=0.01)
x_t_1 = np.exp(0.5*t_1)*np.heaviside((-t_1+4),1)
t_2=np.linspace(-4,4,int((4-(-4)/0.01)))
x_t_2= np.piecewise(t_2, [
        t_2 < -1,
       (t_2 >= -1) & (t_2 <= 1),
        t_2 > 1],
            [-1,
             lambda t_2: t_2,
             lambda t_2: np.cos(t_2-1)]
       )
t_3=np.linspace(-5,5,int((5-(-5)/0.01)))
x_t_3=0
for k in range(-20,21):
    x_t_3+=np.exp(-np.abs(2*t_3+k))
n_1 = np.arange(-20, 20, step=1)
x_n_1 = np.sin(2.3*np.pi*n_1)+np.cos(4.3*np.pi*n_1)

plt.stem(n_1,x_n_1)
plt.plot(t_1,x_t_1)
plt.plot(t_2,x_t_2,color="red")
plt.plot(t_3,x_t_3,color="red")
plt.show()