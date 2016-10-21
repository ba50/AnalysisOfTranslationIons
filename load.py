import numpy as np

import os
import glob

import numeric


# Wczytywanie danych z pliku i zapisywanie w formnie binarnej
# In: nazwa pliku do wczytania, kolumny, wiersze
# Out: plik do wczytania


def convert_file_to_binary(file_to_load, file_to_save, dimensions, skip_header=0, skip_footer=0):
    print("Loding file: {}".format(file_to_load))
    filename = file_to_save
    fp = np.memmap(filename, dtype='float32', mode='w+', shape=dimensions)
    data = np.genfromtxt(file_to_load, skip_header=skip_header, skip_footer=skip_footer)
    fp[:] = data[:]


def convert_dir_to_binary(dir_name_in, dir_name_out, dimensions):
    os.chdir(dir_name_in)
    file_load = glob.glob("*")

    os.chdir("..")
    for file in file_load:
        convert_file_to_binary(os.path.join(dir_name_in, file), os.path.join(dir_name_out, file + '.dat'), dimensions)


def data(init_tuple):

    filename = init_tuple[0]
    dimensions = init_tuple[1]
    ion_steps_scope = init_tuple[2]
    ions_scope = init_tuple[3]
    cell_size = init_tuple[4]

    translation = np.memmap(filename, dtype='float32', mode='r', shape=dimensions)
    return numeric.real_ion_path(translation, ion_steps_scope, ions_scope, cell_size)
