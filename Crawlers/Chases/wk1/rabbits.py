import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import utils


def find_prey(position, max_dist, field):
    ds = int(max_dist/2)
    fov = field[int(position[0]-ds):int(position[0]+ds),
                int(position[1]-ds):int(position[1]+ds)]
    x, y = np.array(fov).nonzero()
    return x, y


def chase(start, field, verbose):
    # Coordinates of prey
    [xs, ys] = np.array(field[:, :, 0]).nonzero()
    prey = []
    for i in range(len(xs)):
        prey.append([xs[i], ys[i]])
    found_x, found_y = find_prey(start, 50, field[:, :, 1])
    print len(found_x)

    dist = {}
    # Identify Prey, and find the closest/most dense population
    for j in range(len(found_x)):
        prey = [found_x[j] + start[0], found_y[j] + start[1]]
        if prey[0] != start[0] and prey[1] != start[1]:
            dx = start[0] - prey[0]
            dy = start[1] - prey[1]
            r = np.sqrt((dx ** 2) + (dy ** 2))
            dist[r] = [dx, dy]
            print "Prey @ [" + str(prey[0]) + ',' + str(prey[1]) + ']\tDist: ' + str(r)

    heading = dist[np.array(dist.keys()).min()]
    if verbose:
        print '\033[1m\033[31mChasing To Heading' + str(heading) + '\033[0m'
    return heading


def main():
    width = 250
    height = 250
    field = np.zeros((width, height, 3))
    n_rabbits = 100
    n_predators = 1
    start = []
    rabbits = []

    # Populate the field with rabbits
    for rabbit in range(n_rabbits):
        [x, y] = utils.spawn_random_point(np.zeros((width, height)))
        field[x, y, :] = [1, 1, 1]
        rabbits.append([x, y])
    # Optionally, give predators a start:
    if n_predators == 1:
        start = [int(width / 2), int(height / 2)]
    field[start[0] - 2:start[0], start[1] - 2:start[1], :] = [1, 0, 0]
    # If not assign predator random start
    if len(start) <= 1:
        start = utils.spawn_random_point(field)

    f = plt.figure()
    # Determine direction to head, and define
    # how many steps before checking fov
    simulation = []
    [pxs, pys] = np.array(field[:, :, 1]).nonzero()
    steps = 0
    while n_rabbits > (n_rabbits/2) and steps < 10:
        for position in rabbits:
            directions = {1: [position[0] - 1, position[1] - 1],
                          2: [position[0], position[1] - 1],
                          3: [position[0] + 1, position[1] - 1],
                          4: [position[0] - 1, position[1]],
                          5: position,
                          6: [position[0] + 1, position[1]],
                          7: [position[0] - 1, position[1] + 1],
                          8: [position[0], position[1] + 1],
                          9: [position[0] + 1, position[1] + 1]}

        steps += 1
        simulation.append([plt.imshow(field)])
    a = animation.ArtistAnimation(f,simulation,interval=190,blit=True,repeat_delay=900)
    plt.show()


if __name__ == '__main__':
    main()
