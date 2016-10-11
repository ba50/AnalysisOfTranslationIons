import numpy as np

from numeric import msd_straight_forward, msd_fft
from load import load_data


def compute_straight_forward(file_to_load,
                             dimensions,
                             ion_steps, scope):
    data = load_data(file_to_load, dimensions, ion_steps, scope)

    msd_n = np.zeros((len(data), ion_steps))
    step = np.arange(ion_steps)

    for i, index in enumerate(data):
        msd_n[i] = msd_straight_forward(index.reshape(ion_steps, 3))

    msd = []
    for j in range(ion_steps):
        sum = 0
        for i in range(len(data)):
            sum += msd_n[i][j]
        msd.append(sum / len(data))

    return step, msd


def compute_fft(file_to_load, dimensions, ion_steps, scope):
    data = load_data(file_to_load, dimensions, ion_steps, scope)

    msd_n = np.zeros((len(data), ion_steps))
    step = np.arange(ion_steps)

    for i, index in enumerate(data):
        msd_n[i] = msd_fft(index.reshape(ion_steps, 3))

    msd = []
    for j in range(ion_steps):
        sum = 0
        for i in range(0, len(data)):
            sum += msd_n[i][j]
        msd.append(sum / len(data))

    return step, msd, file_to_load
