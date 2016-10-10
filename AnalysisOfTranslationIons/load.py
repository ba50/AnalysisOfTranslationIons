import numpy as np
import os, glob

from numeric import CreateIonPath

# Wczytywanie danych z pliku i zapisywanie w formnie binarnej
# In: nazwa pliku do wczytania, kolumny, wiersze
# Out: plik do wczytania

def ConvertFileToBinary(file_to_load, file_to_save, skip_header=8, skip_footer=0):
    filename = os.path.join(os.path.abspath(".\\"), file_to_save)
    fp = np.memmap(filename, dtype='float32', mode ='w+', shape = (160000, 3))
    data = np.genfromtxt(file_to_load, skip_header = skip_header, skip_footer= skip_footer)
    fp[:] = data[:]

def ConvertDirToBinary(dir_name_in, dir_name_out):

    file_load=[]
    os.chdir(dir_name_in)
    for file in glob.glob('*'):
        file_load.append(file)

    os.chdir('..')
    for file in file_load:
        ConvertFileToBinary(dir_name_in + file, dir_name_out + file + '.dat')

def LoadData(file_to_load, dimansions, ion_steps, scope):
    filename = os.path.join(os.path.abspath(".\\"), file_to_load)
    translation = np.memmap(filename, dtype='float32', mode='r', shape = dimansions)
    return CreateIonPath(translation, ion_steps, scope)