from os import path
import plot, msd, load

import matplotlib.pyplot as plt

import diffusion

test = 32, 33
bi = 0, 24
y = 24,32
o = 32,80

file = path.join("DataOut", "vv800_1x.dat"), (160000, 3), 6, test

#plot.msd((msd.fft(file[0], file[1], file[2], file[3]), file[0]))
plot.translation(file[0], file[1], file[2], file[3])
#plot.animated_translation(file[0], file[1], file[2], file[3])
#load.convert_dir_to_binary('supercell','DataOut')

#fig = plt.figure()
#ax = fig.gca()

#dane1 = msd.fft(file[0], file[1], file[2], file[3])
#dane2 = msd.fft(file1[0], file1[1], file1[2], file1[3])

#ax.plot(dane1[0], dane1[1])
#ax.plot(dane2[0], dane2[1])

#plt.show()

#diffusion.calculate(msd.fft(file[0], file[1], file[2], file[3]))
