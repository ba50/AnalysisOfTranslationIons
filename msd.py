import numpy as np

import numeric
import load


def simple(init_tuple):
    data = load.data(init_tuple)

    ion_steps_scope = init_tuple[2]
    number_of_ion_steps = ion_steps_scope[1] - ion_steps_scope[0]

    ions_scope = init_tuple[3]
    number_of_ions = ions_scope[1] - ions_scope[0]

    step = np.arange(number_of_ion_steps)

    msd_n = [numeric.msd_simple(data[:, atom]) for atom in range(number_of_ions)]

    msd = []
    for j in range(ion_steps_scope[0], ion_steps_scope[1]):
        sum = 0.0
        for i in msd_n:
            sum += i[j]
        msd.append(sum/number_of_ions)

    return step, msd


def straight_forward(init_tuple):
    data = load.data(init_tuple)

    ion_steps_scope = init_tuple[2]
    number_of_ion_steps = ion_steps_scope[1] - ion_steps_scope[0]

    ions_scope = init_tuple[3]
    number_of_ions = ions_scope[1] - ions_scope[0]

    step = np.arange(number_of_ion_steps)

    msd_n = [numeric.msd_straight_forward(data[:, atom]) for atom in range(ions_scope[1]-ions_scope[0])]

    msd = []
    for j in range(number_of_ion_steps):
        sum = 0.0
        for i in msd_n:
            sum += i[j]
        msd.append(sum/number_of_ions)

    return step, msd

"""
def fft(file_to_load, dimensions, ion_steps, scope, cell_size):
    data = load.data(file_to_load, dimensions, ion_steps, scope, cell_size)

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
"""
