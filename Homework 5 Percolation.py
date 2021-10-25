import array as arr
import random


class Node:

    def __init__(self, coords):
        self.parent = self
        self.coords = coords
        self.rank = 1

    def __repr__(self):
        return f"{self.coords}"

    def find(self, node):
        if self.parent == node:
            return node
        return self.parent.find(self.parent)

    def union(self, node):
        root1 = self.find(self)
        root2 = node.find(node)
        if root1.rank > root2.rank:
            root2.parent = root1
            root1.rank += root2.rank
        else:
            root1.parent = root2
            root2.rank += root1.rank


def make_grid(grid):
    i = 0
    str = ""
    for row in grid:
        str += f"{i} : {row}\n"
        i += 1
    return str


def create_adj(adj_map, x, y, coord, direction):
    node = coord[(x, y)]
    variation = 1
    if node not in adj_map:
        adj_map[node] = []
    if direction == "north" or direction == "west":
        variation = -1
    if direction == "north" or direction == "south":
        variable = x + variation
        adj_map[node].append(coord[variable, y])
        if node not in adj_map[coord[variable, y]]:
            adj_map[coord[variable, y]].append(node)
    else:
        variable = y + variation
        adj_map[node].append(coord[x, variable])
        if node not in adj_map[coord[x, variable]]:
            adj_map[coord[x, variable]].append(node)
    return adj_map


def neighbor_check(grid, x, y, coord, adj_map):
    node = coord[(x, y)]
    adj_map[node] = []
    if x - 1 >= 0:
        if grid[x - 1][y] == "O":
            node.union(coord[(x-1, y)])
            adj_map = create_adj(adj_map, x,y, coord, "north")
    if x + 1 < len(grid):
        if grid[x + 1][y] == "O":
            node.union(coord[(x + 1, y)])
            adj_map = create_adj(adj_map, x, y, coord, "south")
    if y - 1 >= 0:
        if grid[x][y - 1] == "O":
            node.union(coord[(x, y - 1)])
            adj_map = create_adj(adj_map, x, y, coord, "west")
    if y + 1 < len(grid):
        if grid[x][y + 1] == "O":
            node.union(coord[(x, y + 1)])
            adj_map = create_adj(adj_map, x,y, coord, "east")
    return coord, adj_map


def percolation_check(start, end):
    perc_check = {}
    for point in start:
        if start[point].find(point) not in perc_check:
            perc_check[start[point].find(point)] = start[point]
    for point in end:
        if end[point].find(point) in perc_check:
            return True, end[point], perc_check[end[point].find(point)]
    return False, 0, 0


def bfs(adj_map, start, end, grid):
    done = False
    tmpqueue = []
    parents = {}
    tmpqueue.append(start)
    parents[start] = None
    while len(tmpqueue) > 0:
        current = tmpqueue.pop(0)
        for nodes in adj_map[current]:
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
            x, y = current.coords
            grid[x][y] = "X"
            order.append(current)
            current = parents[current]
        order.append(current)
        grid[x][y] = "X"
    return order


def output(path, text):
    f = open(f"Percolation_output1", "x")
    f.write(path)
    f.write(text)


def main():
    coord = {}
    adj_map = {}
    start = {}
    end = {}
    percolated = False
    rows, cols = (500, 500)
    grid = [["C"]*cols for i in range(rows)]
    i = 0
    while not percolated:
        x = random.randint(0, rows - 1)
        y = random.randint(0, rows - 1)
        while (x, y) in coord:
            x = random.randint(0, rows - 1)
            y = random.randint(0, rows - 1)
        grid[x][y] = "O"
        tmp = Node((x, y))
        coord[(x, y)] = tmp
        coord, adj_map = neighbor_check(grid, x, y, coord, adj_map)
        if x == 0:
            if tmp.find(tmp) not in start:
                start[(x, y)] = tmp
        if x == (rows - 1):
            end[(x, y)] = tmp
        if i > (rows * cols * .592):
            percolated, start_point, end_point = percolation_check(start, end)
        i += 1

    order = bfs(adj_map, start_point, end_point, grid)
    length = len(order)
    path = make_grid(grid)
    text = f"Percolation achieved with {i} cells opened ({i / (rows*cols)}%)\n Shortest path length = {length}"
    output(path, text)



if __name__ == '__main__':
    main()
