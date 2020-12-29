import matplotlib.pyplot as plt
import numpy as np

def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

def smooth(data, points):
    ret = []
    for i in range(1, len(data)):
        temp = data[max(0, i - points): i]
        ret.append(sum(temp) / (len(temp)))
        
    return ret

def compare(d1, d2):
    difs = []
    for i in range(min(len(d1), len(d2))):
        difs.append(abs(d1[i] - d2[i]))
        
    return sum(difs) / len(difs)

def rotateToMax(d):
    # Find max value of array
    tmax = 0
    for j in range(len(d)):
        if d[j] > d[tmax]:
            tmax = j

    t2 = list(d[tmax:]) + list(d[:tmax])
    return t2

def loadData(n):
    data = []
    for i in range(n):
        with open('buffers/' + str(i) + '.wav', 'rb') as file:
            d1 = [bytes([b]) for b in file.read()[44:32000]]
            d2 = [i[0] + i[1] for i in list(chunks(d1, 2))]
            d3 = [int.from_bytes(i, byteorder='big', signed=True) for i in d2]
            data.append(d3) 
    return data

def getFreq(data):

    freq = []

    rels = []
    for i in range(1, len(data) - 1):

        if (data[i] > data[i - 1] and data[i] > data[i + 1]):
            rels.append(i)
        elif (data[i] < data[i - 1] and data[i] < data[i + 1]):
            rels.append(i)

    for i in range(len(rels)):
        freq.append(min(abs(rels[i] - rels[i - 1]), 100) / 100)

    return rels, freq

def clampData(data, val):
    return [i if abs(i) > val else 0 for i in data]

def normalize(data):
    return [i / data[0] for i in data]

def getAmp(data):
    return smooth([abs(i) for i in data], 50)
 
# Load Data
n = 4
data = clampData(normalize(rotateToMax(loadData(n)[0])), .05)
freqI, freq = getFreq(data)

# Plot amplitude and data
plt.plot(data)
amp = getAmp(data)[::5]
plt.plot([i * 5 for i in range(len(amp))], amp, color='r')

# Plot frequencies
plt.plot(freqI[1:], freq[1:])

plt.show()