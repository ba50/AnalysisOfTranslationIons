from os import path
import plot, msd, load

test = range(0,2)
bi = range(0, 24)
y = range(24,32)
o = range(32,80)

file = path.join("DataOut", "superc800_3.dat"), (480000, 3), 6000, o

plot.msd(msd.compute_fft(file[0], file[1], file[2], file[3]))
#plot.translation(file[0], file[1], file[2], file[3])
#plot.animated_translation(file[0], file[1], file[2], file[3])
#load.convert_dir_to_binary('supercell','DataOut')
