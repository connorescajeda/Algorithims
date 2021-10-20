import array as arr
import random

class Node:
    parents = {}
    coord = {}

    def __init__(self, parent, coords):
        self.parent = parent
        self.coords = coords

    def find(self):
        if self.parent is None:
            return self
        else:
            return self.parent.find()

    def union(self, node):
        root1 = self.find()
        root2 = node.find()
        root1.parent = root2





def makegrid(grid):
    top = []
    for i in range(len(grid)):
        top.append(f"{i}")
    print(f"Top {top}")
    i = 0
    for row in grid:
        print(f"{i} : {row}")
        i += 1


def neighbor_check(grid, x, y):
    neighbor = {}
    if x - 1 >= 0:
        if grid[x - 1][y] == "O":
            neighbor["north"] = True
    if x + 1 < len(grid):
        if grid[x + 1][y] == "O":
            neighbor["south"] = True
    if y - 1 >= 0:
        if grid[x][y - 1] == "O":
            neighbor["west"] = True
    if y + 1 < len(grid):
        if grid[x][y + 1] == "O":
            neighbor["east"] = True
    return neighbor



def main():
    coord = {}
    rows, cols = (5, 5)
    grid = [["C"]*cols for i in range(rows)]
    print(len(grid))
    for i in range (20):
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        grid[x][y] = "O"
        neighbors = neighbor_check(grid, x, y)
        if neighbors == {}:
            Node(None, (x, y))
        makegrid(grid)
        print("-----------------------")



if __name__ == '__main__':
    main()
