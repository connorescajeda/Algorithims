from checkgraph import checkgraph
import random

file = "graph-big-2"
def main():
    f = open(f"{file}.in")
    nodes = f.readline()
    edges = f.readline()
    f = f.read().splitlines()
    adjmap = {}
    for line in f:
        if len(line.split()) != 1:
            (one, two) = line.split()
            if one not in adjmap:
                adjmap[one] = []
            if two not in adjmap:
                adjmap[two] = []
            if two not in adjmap[one]:
                adjmap[one].append(two)
    topsort(adjmap)

def topsort(adjmap):

    t = []
    queue = []
    indegree = {}
    for vertex in adjmap:
        if vertex not in indegree:
            indegree[vertex] = 0
        for neighbor in adjmap[vertex]:
            if neighbor not in indegree:
                indegree[neighbor] = 0
            if neighbor in indegree:
                indegree[neighbor] += 1

    for vertex in indegree:
        if indegree[vertex] == 0:
            queue.append(vertex)

    while len(queue) != 0:
        tmpVertex = queue.pop(0)
        t.append(tmpVertex)
        for neighbor in adjmap[tmpVertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(t) == len(adjmap):
        stuff = "DAG\n"
        for vertex in t:
            stuff += f"{vertex}\n"
        output(f"{file}", stuff)

    else:
        for vertex in indegree:
            if indegree[vertex] > 0:
                parents, done, end = bfs(adjmap, vertex)
                if done:
                    order = []
                    current = end
                    while current != vertex:
                        order.append(current)
                        current = parents[current]
                    order.append(current)
                    break



        stuff = "cycle\n"
        for i in range(len(order), 0, -1):
            stuff += f"{order[i-1]}\n"
        output(f"{file}", stuff)




def bfs(adjmap, start):
    done = False
    tmpqueue = []
    parents = {}
    tmpqueue.append(start)
    parents[start] = None
    end = None
    while len(tmpqueue) > 0:
        current = tmpqueue.pop(0)
        for vertex in adjmap[current]:
            if vertex not in parents:
                parents[vertex] = current
                tmpqueue.append(vertex)
            elif vertex == start:
                done = True
                end = current
    return parents, done, end


def output(infile, text):
    f = open(f"{infile}.out", "x")
    f.write(text)







main()