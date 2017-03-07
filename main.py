from os import path
import plot, msd, load

import matplotlib.pyplot as plt

import diffusion

test = 735, 745
bi = 0, 24
y = 24, 32
o = 32, 80

# wielokrotnosc 80
# zakres <0, 75>
multiple = 0, 1
ion_steps_scope = multiple[0] * 745, multiple[1] * 745

#cell_size = 5.559, 5.559, 5.559
cell_size = 1, 1, 1

file = path.join("data_out", "simulation.dat"), (151200, 3), ion_steps_scope, test, cell_size
#file1 = path.join("data_out", "superc1000_1.dat"), (480000, 3), ion_steps_scope, o, cell_size

#plot.msd((msd.simple(file[0], file[1], file[2], file[3], file[4]), file[0]))
plot.translation(file)
#plot.animated_translation(file[0], file[1], file[2], file[3])
#load.convert_dir_to_binary('kmc','data_out', (151200, 3))

#fig = plt.figure()
#ax = fig.gca()

#dane1 = msd.simple(file)
#dane2 = msd.simple(file1)

#ax.plot(dane1[0], dane1[1])
#ax.plot(dane2[0], dane2[1])

#plt.show()

#diffusion.calculate(msd.fft(file[0], file[1], file[2], file[3]))
