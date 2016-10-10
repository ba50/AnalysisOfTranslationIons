import plot, msd

test = range(0,2)
Bi = range(0,24)
Y = range(24,32)
O = range(32,80)

#plot.Msd(msd.ComputeFFT('DataOut\\vv800_1x.dat', (160000,3), 2000, Bi))
#plot.Translation('DataOut\\vv800_1x.dat', (160000,3), 2000, Bi)
plot.AnimatedTranslation('DataOut\\vv800_1x.dat', (160000,3), 2000, Bi)
