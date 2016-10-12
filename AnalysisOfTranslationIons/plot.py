import numpy as np

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

import load

def translation(file_to_load, dimensions, ion_steps, scope):

   # Attaching 3D axis to the figure
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    data = load.data(file_to_load, dimensions, ion_steps, scope)
    for atom in range((scope[1] - scope[0])):
        ax.plot(data[:, atom, 0],data[:, atom, 1],data[:, atom, 2])

   # Setting the axes properties
    ax.set_xlim3d([0.0, 1.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([0.0, 1.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([0.0, 1.0])
    ax.set_zlabel('Z')

    ax.set_title('Diffusion plot in: {}'.format(file_to_load))

    plt.show()


def animated_translation(file_to_load, dimensions, ion_steps, scope):

    def update_lines(num, data_lines, lines):
        for line, data_temp in zip(lines, data_lines):
            # NOTE: there is no .set_data() for 3 dim data...
            line.set_data(data_temp[0:2, :num])
            line.set_3d_properties(data_temp[2, :num])
        return lines

    # Attaching 3D axis to the figure
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    data = load.data(file_to_load, dimensions , ion_steps, scope)

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


def n_msd_in_loop(msd):
    fig = plt.figure()
    ax = fig.gca()

    step = np.arange(len(msd))
    ax.plot(step, msd)

    plt.show()
