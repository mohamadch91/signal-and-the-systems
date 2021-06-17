import numpy as np

import matplotlib.pyplot as plt
def conv(x_n,h_n):
     ans=np.zeros((len(x_n)+len(h_n)))
     temp_1=np.concatenate((x_n,np.zeros(len(h_n))))
     temp_2 = np.concatenate((h_n, np.zeros(len(x_n))))

     for i in range(len(ans)):
          for j in range (i):
               ans[i]+=temp_1[j]*temp_2[i-j]
     return ans

if __name__ == '__main__':
     n=np.arange(-25,25,step=1)
     h_n=np.heaviside((n-10),1)-np.heaviside((n+10),1)
     x_n=(np.heaviside((n-5),1)-np.heaviside((n+5),1))
     for z in range(len(x_n)):
          x_n[z]=x_n[z]*(0.25**(z-25))
     ans_1=conv(x_n,h_n)
     ans_1_correct=np.convolve(x_n,h_n);
     plt.stem(ans_1)
     plt.show()
     plt.stem(ans_1_correct)
     plt.show()
     t=np.arange(-15,15,step=0.01)
     h_t=np.heaviside((t+3),1)-np.heaviside((t-3),1)
     x_t=(0.5)*np.exp(2*t)*np.heaviside((-t),1)
     ans_2=conv(x_t,h_t)
     plt.plot(ans_2)
     plt.show()
     plt.plot(np.convolve(x_t,h_t))
     plt.show()
