from os import path
import plot, msd, load

import matplotlib.pyplot as plt

import diffusion

test = 0, 2
bi = 0, 24
y = 24,32
o = 32,80

cell_size = 5.559, 5.559, 5.559

file = path.join("DataOut", "superc700_1.dat"), (480000, 3), 6000, o, cell_size
file1 = path.join("DataOut", "superc700_1.dat"), (480000, 3), 6000, o, cell_size

#plot.msd((msd.simple(file[0], file[1], file[2], file[3], file[4]), file[0]))
#plot.translation(file[0], file[1], file[2], file[3], file[4])
#plot.animated_translation(file[0], file[1], file[2], file[3])
#load.convert_dir_to_binary('supercell','DataOut')

fig = plt.figure()
ax = fig.gca()

dane1 = msd.simple(file[0], file[1], file[2], file[3], file[4])
dane2 = msd.fft(file1[0], file1[1], file1[2], file1[3], file1[4])

ax.plot(dane1[0], dane1[1])
ax.plot(dane2[0], dane2[1])

plt.show()

#diffusion.calculate(msd.fft(file[0], file[1], file[2], file[3]))
