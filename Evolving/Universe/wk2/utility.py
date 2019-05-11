from matplotlib.animation import FFMpegWriter
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

colors = {'r': [1,0,0],
          'g': [0,1,0],
          'b': [0,0,1],
          'c': [0,1,1],
          'm': [1,0,1],
          'y': [1,1,0],
          'k': [0,0,0],
          'w': [1,1,1]}


def spawn_random_point(state):
    # Initialize a random position
    x = np.random.randint(0, state.shape[0], 1, dtype=int)
    y = np.random.randint(0, state.shape[1], 1, dtype=int)
    return [x, y]


def bfs(graph_data, start):
    g = nx.from_dict_of_lists(graph_data)
    path = list()
    queue = [start]
    queued = list()
    while queue:
        vertex = queue.pop()
        for node in graph_data[vertex]:
            if node not in queued:
                queued.append(node)
                queue.append(node)
                path.append([vertex, node])
    return path


def dfs(graph, start):
    stack = [start]
    parents = {start:start}
    path = list()
    while stack:
        vertex = stack.pop(-1)
        for node in graph[vertex]:
            if node not in parents:
                parents[node] = vertex
                stack.append(node)
        path.append([parents[vertex], vertex])
    return path[1:]


def spawn_random_walk(position, n_steps):
    choice_pool = np.random.randint(1, 10, n_steps)
    random_walk = list()
    for step in choice_pool:
        directions = {1: [position[0]-1, position[1]-1],
                      2: [position[0], position[1]-1],
                      3: [position[0]+1, position[1]-1],
                      4: [position[0]-1, position[1]],
                      5: position,
                      6: [position[0]+1, position[1]],
                      7: [position[0]-1, position[1]+1],
                      8: [position[0], position[1]+1],
                      9: [position[0]+1, position[1]+1]}
        position = directions[step]
        random_walk.append(directions[step])
    return random_walk


def ind2sub(index,dims):
    """
    Given an index and array dimensions,
    convert an index to [x,y] subscript pair.
    :param index:
    :param dims:
    :return tuple - subscripts :
    """
    ii = 0
    for y in range(dims[1]):
        for x in range(dims[0]):
            if index==ii:
                return [x,y]
            ii +=1
    return [x,y]

def add_random_points_color(state,n_pts,value):
    for t in range(n_pts):
        pt = spawn_random_point(np.zeros((state.shape[0], state.shape[1])))
        state[pt[0], pt[1], :] = colors[value]
    return state


def add_random_points(state, n_pts):
    for point in range(n_pts):
        [x, y] = spawn_random_point(state)
        state[x, y] = 1
    return state


def animate_walk(steps,state,frame_rate,save,name):
    f = plt.figure()
    film = []
    for step in steps:
        if state[step[0], step[1]] == 1:
            state[step[0], step[1]] = 0
        else:
            state[step[0], step[1]] = 1
        film.append([plt.imshow(state, 'gray_r')])
    a = animation.ArtistAnimation(f,film,interval=frame_rate,blit=True,repeat_delay=900)
    if save:
        w = FFMpegWriter(fps=frame_rate, bitrate=1800)
        a.save(name, writer=w)
    plt.show()


def build_map(width, height, n_points):
    state = np.zeros((width, height))
    for pt in range(n_points):
        [x,y] = spawn_random_point(state)
        state[x,y] = 1
    return state


def build_map_color(width, height, n_points):
    state = np.zeros((width, height, 3))
    for pt in range(n_points):
        [x,y] = spawn_random_point(np.zeros((width, height)))
        state[x,y,:] = [1,0,0]
    return state
# EOF
