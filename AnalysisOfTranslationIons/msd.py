import numpy as np

from numeric import CreateIonPath, MsdStraightForward, MsdFft
from load import LoadData


def ComputeStraightForward(file_to_load, dimansions, ion_steps, scope):

    data = LoadData(file_to_load,dimansions,ion_steps,scope)

    msd_n= np.zeros((len(data), ion_steps))
    step=np.arange(ion_steps)

    for i, index in enumerate(data):
        msd_n[i] = MsdStraightForward(index.reshape(ion_steps,3))

    msd=[]
    sum=0
    for j in range(0,ion_steps):
        for i in range(0, len(data)):
            sum += msd_n[i][j]
        msd.append(sum/len(data))
        sum=0

    return (step, msd)

def ComputeFFT(file_to_load, dimansions, ion_steps, scope):

    data = LoadData(file_to_load,dimansions,ion_steps,scope)

    msd_n= np.zeros((len(data), ion_steps))
    step=np.arange(ion_steps)

    for i, index in enumerate(data):
        msd_n[i] = MsdFft(index.reshape(ion_steps,3))

    msd=[]
    sum=0
    for j in range(0,ion_steps):
        for i in range(0, len(data)):
            sum += msd_n[i][j]
        msd.append(sum/len(data))
        sum=0

    return (step, msd)

