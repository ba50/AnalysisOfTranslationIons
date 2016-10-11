import plot, msd, load
from os import path

test = range(0,2)
bi = range(0, 24)
Y = range(24,32)
O = range(32,80)

#plot.Msd(msd.ComputeFFT('DataOut\\vv800_1x.dat', (160000,3), 2000, Bi))
plot.Translation('DataOut\\vv800_1x.dat', (160000,3), 2000, bi)
#plot.AnimatedTranslation(path.join("DataOut", "vv800_1x.dat"), (160000,3), 2000, bi)
#load.ConvertDirToBinary('DataIn','DataOut')
