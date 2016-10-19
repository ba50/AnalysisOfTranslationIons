import numpy as np


def boxed_ion_path(translation, ion_steps_scope, ions_scope):
    numer_of_ions = ions_scope[1] - ions_scope[0]
    paths = np.empty((ion_steps, numer_of_ions, 3))
    for ion in range(numer_of_ions):
        step = ion_steps_scope[0]
        seed = ion + ions_scope[0]
        for ion_step in range(ion_steps_scope[0], ion_steps_scope[1]):
            paths[ion_step, ion, :]  = translation[seed+step]
            step += 80

    return paths

def real_ion_path(translation, ion_steps_scope, ions_scope, cell_size=(0,0,0)):

    numer_of_ions = scope[1]-scope[0]
    paths = boxed_ion_path(translation, ion_steps_scope, ions_scope)
    for ion in range(numer_of_ions):
        for ion_step in range(ion_steps_scope[0], ion_steps_scope[1]-1):
            next_ion_step = ion_step+1

            if paths[next_ion_step, ion, 0]-paths[ion_step, ion, 0] < 0.5:
                paths[next_ion_step, ion, 0]+=1
            if paths[next_ion_step, ion, 0]-paths[ion_step, ion, 0] > -0.5:
                paths[next_ion_step, ion, 0]-=1

            if paths[next_ion_step, ion, 1]-paths[ion_step, ion, 1] < 0.5:
                paths[next_ion_step, ion, 1]+=1
            if paths[next_ion_step, ion, 1]-paths[ion_step, ion, 1] > -0.5:
                paths[next_ion_step, ion, 1]-=1


            if paths[next_ion_step, ion, 2]-paths[ion_step, ion, 2] < 0.5:
                paths[next_ion_step, ion, 2]+=1
            if paths[next_ion_step, ion, 2]-paths[ion_step, ion, 2] > -0.5:
                paths[next_ion_step, ion, 2]-=1

    if not cell_size[0] == 0:
        paths*=cell_size
        paths/=2.0


    return paths


def msd_simple(r):

    msd=[]
 #   print(r[0, 0])
    for i in range(len(r)):
 #       print(r[i,0]-r[0,0])
        msd.append(np.square(r[i,0]-r[0,0])+
                   np.square(r[i,1]-r[0,1])+
                   np.square(r[i,2]-r[0,2]))

    return msd


def msd_straight_forward(r):
    shifts = np.arange(len(r))
    msds = np.zeros(shifts.size)

    for i, shift in enumerate(shifts):
        diffs = r[:-shift if shift else None] - r[shift:]
#        print(r[:-shift if shift else None] )
#        print("\n")
 #       print(r[shift:])

        sqdist = np.square(diffs).sum(axis=1)
#        print("\n")
#        print(sqdist)
        msds[i] = sqdist[0]#.mean()
#        print("------------------------------")

    return msds


def msd_fft(r):
  def autocorrFFT(x):
      N=len(x)
      F = np.fft.fft(x, n=2*N)  #2*N because of zero-padding
      PSD = F * F.conjugate()
      res = np.fft.ifft(PSD)
      res= (res[:N]).real   #now we have the autocorrelation in convention B
      n=N*np.ones(N)-np.arange(0,N) #divide res(m) by (N-m)
      return res/n #this is the autocorrelation in convention A

  N=len(r)
  D=np.square(r).sum(axis=1)
  D=np.append(D,0)
  S2=sum([autocorrFFT(r[:, i]) for i in range(r.shape[1])])
  Q=2*D.sum()
  S1=np.zeros(N)
  for m in range(N):
      Q=Q-D[m-1]-D[N-m]
      S1[m]=Q/(N-m)
  return S1-2*S2


def make_line(a, b, scope, num):
    x = np.linspace(scope[0], scope[1], num=num)
    y = a*x+b
    return x, y
