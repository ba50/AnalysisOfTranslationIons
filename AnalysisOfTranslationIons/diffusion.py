import numpy as np
import plot
import numeric
import msd

import matplotlib.pyplot as plt
from os import path

def calculate(r):
    line = np.polyfit(r[0],r[1],1)
    print(line)
    print(line[1]/(6*r[1][-1]))


    o = 32,80

    file = path.join("DataOut", "superc800_2.dat"), (480000, 3), 6000, o

    fig = plt.figure()
    ax = fig.gca()

    dane1 = msd.fft(file[0], file[1], file[2], file[3])
    dane2 = numeric.make_line(line[1], line[0], (r[0][0],r[0][-1]),100)

    ax.plot(dane1[0], dane1[1])
    ax.plot(dane2[0], dane2[1])

    plt.show()




