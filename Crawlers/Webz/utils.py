import networkx as nx
import os


def swap(fname, destroy):
    data = []
    [data.append(line.replace('\n', '')) for line in open(fname, 'r').readlines()]
    if destroy:
        os.remove(fname)
    return data


def readir(pathway, verbose):
    contents = {'files':[],'dirs':[]}
    for item in os.listdir(pathway):
        if os.path.isfile(pathway+'/' + item):
            contents['files'].append(item)
        if os.path.isdir((pathway+'/'+item)):
            contents['dirs'].append(item)
    if verbose:
        print str(len(contents['files'])) + ' Files Found'
        print str(len(contents['dirs'])) + ' Directories Found'
    return contents


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
