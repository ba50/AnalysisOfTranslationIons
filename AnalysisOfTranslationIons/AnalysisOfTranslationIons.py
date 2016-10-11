from os import path
import plot, msd, load

test = 0, 1
bi = 0, 24
y = 24,32
o = 32,80

file = path.join("DataOut", "vv800_1x.dat"), (160000, 3), 2000, bi

plot.msd((msd.straight_forward(file[0], file[1], file[2], file[3]), file[0]))
#plot.translation(file[0], file[1], file[2], file[3])
#plot.animated_translation(file[0], file[1], file[2], file[3])
#load.convert_dir_to_binary('supercell','DataOut')
