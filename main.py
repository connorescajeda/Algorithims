def main():
    f = open("graphs/graph-F21.txt")
    edges = f.readline()
    f = f.read().splitlines()
    s = {}
    for line in f:
        if len(line.split()) != 1:
            (one, two) = line.split()
            if one not in s:
                s[one] = []
            if two not in s:
                s[two] = []
            if one not in s[two]:
                s[two].append(one)
            if two not in s[one]:
                s[one].append(two)
    order = bfs(s)
    for i in range(len(order), 0, -1):
        print(order[i-1])






def bfs(s):
    done = False
    end = "END"
    start = "Connor"
    tmpqueue = []
    parents = {}
    tmpqueue.append("Connor")
    parents['Connor'] = None
    while len(tmpqueue) > 0:
        current = tmpqueue.pop(0)
        for nodes in s[current]:
            if nodes not in parents:
                parents[nodes] = current
                tmpqueue.append(nodes)
                if nodes == end:
                    done = True
                    break
    if done:
        current = end
        order = []
        while current != start:
            order.append(current)
            current = parents[current]
        order.append(current)
    return order







main();