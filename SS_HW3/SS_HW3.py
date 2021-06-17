from scipy.io import wavfile
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
def plot_main_signal():
    name=input("file name: ")
    T,wave=scipy.io.wavfile.read(name)
    wave=wave[:500]
    t=np.arange(0,500/T,1/T)
    plt.plot(t,wave)
    plt.show()

def fourie():
    name = input("file name: ")
    T, wave = scipy.io.wavfile.read(name)
    #tanavob ba shekl hodadan 100 ast
    t=100
    omega=np.pi*2/t
    k=10
    ak=[]
    for i in range(k+1):
        b=0
        c=0
        for s in range (t-1):
            b+=wave[s]*np.cos(s*i*omega)
            c+=wave[s]*np.sin(s*i*omega)
        b*=1/t
        c*=1/t
        ak.append(complex(b,-c))
    for z in range(len(ak)):
        ak[z]=abs(ak[z])
    time=np.linspace(0,T,k+1)
    plt.stem(time,ak)
    plt.show()
if __name__ == '__main__':
    plot_main_signal()
    fourie()



