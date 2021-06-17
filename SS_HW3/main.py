from scipy.io import wavfile
import scipy.io
import numpy as np
import matplotlib.pyplot as plt


def plot_waves(filename):
    rate, data = scipy.io.wavfile.read(filename, mmap=False)
    length = data.shape[0] / rate
    dataSmaller = data[:500]
    duration = dataSmaller.shape[0] / rate
    time = np.arange(0, duration, 1 / rate)
    plt.plot(time, dataSmaller)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title(filename)
    plt.show()
    return rate, data, length, filename


def fourier_series(length, rate, arr, filename, K):
    T = 100
    if filename == "bonus.wav":
        T = 10113
    w = 2 * np.pi/T
    sum_value_b = 0
    sum_value_c = 0
    a_k = []
    b_k = []
    c_k = []
    for k in range(K):
        for t in range(0, int(T-1)):
            sum_value_b = sum_value_b + arr[t] * np.cos(k*t*w)
            sum_value_c = sum_value_c + arr[t] * np.sin(k*t*w)
        integral_value_b = (1 / T) * sum_value_b
        integral_value_c = (1 / T) * sum_value_c
        b_k.append(integral_value_b)
        c_k.append(integral_value_c)
        a_k.append(abs(complex(b_k[k], -1*c_k[k])))
        sum_value_b = 0
        sum_value_c = 0
    fre = np.linspace(0, 44100, K)
    plt.stem(fre, a_k)
    plt.xlabel('Frequency [f]')
    plt.ylabel('Amplitude')
    plt.title(filename)
    plt.show()
    if filename == "bonus.wav":
        a_k.sort(reverse=True)
        print("Bonus Wave frequences:",a_k[0], a_k[1], a_k[2], a_k[3], a_k[4])


rate1, data1, length1, filename1 = plot_waves("wave1.wav")
rate2, data2, length2, filename2 = plot_waves("wave2.wav")
rate3, data3, length3, filename3 = plot_waves("wave3.wav")
rate4, data4, length4, filename4 = plot_waves("wave4.wav")
rate_bonus, data_bonus, length_bonus, filename_bonus = plot_waves("bonus.wav")
fourier_series(length1, rate1, data1, filename1, 11)
fourier_series(length2, rate2, data2, filename2, 11)
fourier_series(length3, rate3, data3, filename3, 11)
fourier_series(length4, rate4, data4, filename4, 11)
fourier_series(length_bonus, rate_bonus, data_bonus, filename_bonus, 100)






