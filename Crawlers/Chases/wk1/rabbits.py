import matplotlib.pyplot as plt
import numpy as np
import utils


def find_prey(position, max_dist, field):
    ds = int(max_dist/2)
    fov = field[int(position[0]-ds):int(position[0]+ds),
                int(position[1]-ds):int(position[1]+ds)]
    x, y = np.array(fov).nonzero()
    return x, y


def main():
    width = 250
    height = 250
    field = np.zeros((width, height, 3))
    n_rabbits = 100
    n_predators = 1
    start = []

    # Populate the field with rabbits
    for rabbit in range(n_rabbits):
        [x, y] = utils.spawn_random_point(np.zeros((width, height)))
        field[x, y, :] = [1, 1, 1]

    # Optionally, give predators a start:
    if n_predators == 1:
        start = [int(width / 2), int(height / 2)]
    field[start[0] - 2:start[0], start[1] - 2:start[1], :] = [1, 0, 0]
    # Coordinates of prey
    [xs, ys] = np.array(field[:, :, 0]).nonzero()
    prey = []
    for i in range(len(xs)):
        prey.append([xs[i], ys[i]])
    found_x, found_y = find_prey(start, 50, field[:, :, 1])
    print len(found_x)

    plt.imshow(field)
    plt.show()


if __name__ == '__main__':
    main()
