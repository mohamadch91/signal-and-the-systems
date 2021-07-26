import matplotlib.pyplot as plt
import  numpy as np
import numpy.fft
from scipy.io import wavfile
def similarity(song_spec, clip_spec, points_per_slice=6):
    song_flat = song_spec.flatten()
    clip_flat = clip_spec.flatten()
    
    sim_window_size = points_per_slice - 1
    score = 0
    for anchor in range(clip_flat.shape[0] - points_per_slice):
        anchor_y = anchor % points_per_slice
        sim_window = clip_flat[anchor: anchor+sim_window_size]
        for song_anchor in range(anchor_y, song_flat.shape[0] - points_per_slice - 1, points_per_slice):
            if clip_flat[anchor] == song_flat[song_anchor]:
                if np.count_nonzero((song_flat[song_anchor:song_anchor+sim_window_size] - sim_window) == 0) >= 4:
                    score += 1
    
    score /= song_flat.shape[0]
    return score

def sampling(rate,data):
    count_time=int(data.size/2048)

    signal_array=[]
    empty_array=[]
    for i in range(count_time):
        empty_array=[]
        for s in range(2048):
            empty_array.append(data[i*2048+s])

        signal_array.append(empty_array)
    empty_array=[]
    for ss in range(count_time*2048,data.size):
        empty_array.append(data[ss])
    signal_array.append(empty_array)
    return signal_array
def calculate_fouriye(signal_array,samplerate):
    fouriyes=[]
    for i in range (len(signal_array)):
                empty=[]
                x=numpy.fft.fft(signal_array[i])
                freq=np.fft.fftfreq(len(signal_array[i]),1/samplerate)
                for j in range(len(freq)):
                    if(freq[j]>100 and freq[j]<5000):
                        empty.append(x[j])
                fouriyes.append(empty)
    return fouriyes
def noiseprint(fouriye,samplerate):
    noisi = []
    for s in range(6):
            temp = []
            for i in range(len(fouriye)-1):
                x = fouriye[i]
                lentgh = len(x)
                count = int(lentgh / 6)
                empty=[]
                for m in range(count):
                    empty.append(x[s*count+m])
                freq=np.fft.fftfreq(len(empty),1/samplerate)
                max=numpy.max(freq)
                for counter in range(len(freq)):
                    if(max==freq[counter]):
                        noisi.append(empty[counter])

    z=np.reshape(noisi,(6,len(fouriye)-1))
    return z




if __name__ == '__main__':
    for i in range(1,4):
        score_array=[]
        filename='clip'+str(i)+'.wav'
        samplerate, data = wavfile.read(filename)
        signals=sampling(samplerate,data)
        fouriyes=calculate_fouriye(signals,samplerate)
        noise_matris=noiseprint(fouriyes,samplerate)
        print(noise_matris)
        # plt.plot(noise_matris,samplerate)
        # plt.show()
        # plt.imshow(noise_matris, origin='lower', aspect='auto', cmap='gray')
        s1,d1=wavfile.read('1_prelude.wav')
        ss1=sampling(s1,d1)
        f1=calculate_fouriye(ss1,s1)
        n_m1=noiseprint(f1,samplerate)
        temp=similarity(n_m1,noise_matris)
        score_array.append(temp)

        s2,d2=wavfile.read('2_love_is_blue.wav')
        ss2=sampling(s2,d2)
        f2=calculate_fouriye(ss2,s2)
        n_m2=noiseprint(f2,samplerate)
        temp = similarity(n_m2, noise_matris)
        score_array.append(temp)

        s3,d3=wavfile.read('3_chanson_du_toreador.wav')
        ss3=sampling(s3,d3)
        f3=calculate_fouriye(ss3,s3)
        n_m3=noiseprint(f3,samplerate)
        temp = similarity(n_m3, noise_matris)
        score_array.append(temp)


        s4,d4=wavfile.read('4_el_bimbo.wav')
        ss4=sampling(s4,d4)
        f4=calculate_fouriye(ss4,s4)
        n_m4=noiseprint(f4,samplerate)

        temp = similarity(n_m4, noise_matris)
        score_array.append(temp)

        max=numpy.max(score_array)
        for i in range(len(score_array)):
            if(max==score_array[i]):
                if(i==0):
                    print(filename+" similar to 1_prelude ")
                elif(i==1):
                    print(filename + " similar to 2_love_is_blue ")
                elif (i == 2):
                    print(filename + " similar to 3_chanson_du_toreador ")
                elif(i==3):
                    print(filename + " similar to 4_el_bimbo ")




