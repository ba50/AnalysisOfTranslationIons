import numpy as np

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

import load


def translation(init_tuple):

    filename = init_tuple[0]
    ion_steps_scope = init_tuple[2]
    ions_scope = init_tuple[3]
    number_of_ions = ions_scope[1] - ions_scope[0]

   # Attaching 3D axis to the figure
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    paths = load.data(init_tuple)
    for ion in range(number_of_ions):
        ax.plot(paths[:, ion, 0], paths[:, ion, 1], paths[:, ion, 2])

   # Setting the axes properties
    ax.set_xlim3d([0.0, 6.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([0.0, 6.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([0.0, 6.0])
    ax.set_zlabel('Z')

    ax.set_title('Diffusion plot in: {}'.format(filename))

    plt.show()


def animated_translation(file_to_load, dimensions, ion_steps, scope, cell_size):

    def update_lines(num, data_lines, lines):
        for line, data_temp in zip(lines, data_lines):
            # NOTE: there is no .set_data() for 3 dim data...
            line.set_data(data_temp[0:2, :num])
            line.set_3d_properties(data_temp[2, :num])
        return lines

    # Attaching 3D axis to the figure
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    data = load.data(file_to_load, dimensions, ion_steps, scope, cell_size)

    ion_path = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]

    # Setting the axes properties
    ax.set_xlim3d([0.0, 1.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([0.0, 1.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([0.0, 1.0])
    ax.set_zlabel('Z')

    ax.set_title('Diffusion plot in: {}'.format(file_to_load))

    # Creating the Animation object
    line_ani = animation.FuncAnimation(fig, update_lines, ion_steps, fargs=(data, ion_path), interval=50, blit=False)

    plt.show()


def msd(data):
    fig = plt.figure()
    ax = fig.gca()
    fig.canvas.set_window_title(data[1])

    # Setting the axes properties
    ax.set_xlabel("time (ps)")

    ax.set_ylabel("MSD (A**2 s**-1)")

    ax.plot(data[0][0]*10**-2, data[0][1]) # Zamiana na fs * 10, a nastempnie na ps *10**-3
    plt.show()


def x_y(r):
    fig = plt.figure()
    ax = fig.gca()

    ax.plot(r[0], r[1])

    plt.show()
