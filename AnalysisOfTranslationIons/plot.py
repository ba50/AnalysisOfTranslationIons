import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

from load import load_data


def translation(file_to_load, dimensions, ion_steps, scope):

   # Attaching 3D axis to the figure
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    data = load_data(file_to_load, dimensions, ion_steps, scope)
    for index in data:
        ax.plot(index[0], index[1], index[2])

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

    data = load_data(file_to_load, dimensions , ion_steps, scope)

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
    fig.canvas.set_window_title(data[2])

    # Setting the axes properties
    ax.set_xlabel('time')

    ax.set_ylabel('Y')

    ax.plot(data[0], data[1])
    plt.show()
