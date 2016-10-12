import numpy as np

import numeric
import load
import plot


def simple(file_to_load, dimensions, ion_steps, scope):
    data = load.data(file_to_load, dimensions, ion_steps, scope)

    msd_n = np.zeros((len(data), ion_steps))
    step = np.arange(ion_steps)

    msd_n = [numeric.msd_simple(data[:, atom]) for atom in range(scope[1]-scope[0])]

    msd = []
    for j in range(ion_steps):
        sum = 0.0
        for i in msd_n:
            sum += i[j]
        msd.append(sum/(scope[1]-scope[0]))

    return step, msd


def straight_forward(file_to_load,
                             dimensions,
                             ion_steps,
                             scope):
    data = load.data(file_to_load, dimensions, ion_steps, scope)

    msd_n = np.zeros((len(data), ion_steps))
    step = np.arange(ion_steps)

    msd_n = [numeric.msd_straight_forward(data[:, atom]) for atom in range(scope[1]-scope[0])]

    msd = []
    for j in range(ion_steps):
        sum = 0.0
        for i in msd_n:
            sum += i[j]
        msd.append(sum/(scope[1]-scope[0]))

    return step, msd


def fft(file_to_load, dimensions, ion_steps, scope):
    data = load.data(file_to_load, dimensions, ion_steps, scope)

    msd_n = np.zeros((len(data), ion_steps))
    step = np.arange(ion_steps, dtype='float32')

    msd_n = [numeric.msd_fft(data[:, atom]) for atom in range((scope[1]-scope[0]))]

    msd = []
    for j in range(ion_steps):
        sum = 0.0
        for i in msd_n:
            sum += i[j]
        msd.append(sum/(scope[1]-scope[0]))

    return step, msd

