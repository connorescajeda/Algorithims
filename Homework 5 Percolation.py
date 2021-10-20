import array as arr
import random


class Node:

    def __init__(self, coords):
        self.parent = None
        self.coords = coords
        self.rank = 1

    def find(self):
        if self.parent is None:
            return self
        else:
            return self.parent.find()

    def union(self, node):
        root1 = self.find()
        root2 = node.find()
        if root1.rank > root2.rank:
            root2.parent = root1
            root1.rank += root2.rank
        else:
            root1.parent = root2
            root2.rank += root1.rank


def make_grid(grid):
    top = []
    for i in range(len(grid)):
        top.append(f"{i}")
    print(f"Top {top}")
    i = 0
    for row in grid:
        print(f"{i} : {row}")
        i += 1


def neighbor_check(grid, x, y, coord):
    largest_rank = coord[(x, y)]
    if x - 1 >= 0:
        if grid[x - 1][y] == "O":
            if largest_rank < coord[(x-1, y)].rank:
                largest_rank = coord[(x - 1, y)]
    if x + 1 < len(grid):
        if grid[x + 1][y] == "O":
            if largest_rank < coord[(x + 1, y)].rank:
                largest_rank = coord[(x + 1, y)]
    if y - 1 >= 0:
        if grid[x][y - 1] == "O":
            if largest_rank < coord[(x, y - 1)].rank:
                largest_rank = coord[(x, y - 1)]
    if y + 1 < len(grid):
        if grid[x][y + 1] == "O":
            if largest_rank < coord[(x, y + 1)].rank:
                largest_rank = coord[(x, y + 1)]
    return largest_rank


def main():
    coord = {}
    rows, cols = (5, 5)
    grid = [["C"]*cols for i in range(rows)]
    print(len(grid))
    for i in range(20):
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        grid[x][y] = "O"
        tmp = Node((x, y))
        coord[(x, y)] = tmp
        neighbors = neighbor_check(grid, x, y, coord)
        make_grid(grid)
        print("-----------------------")


if __name__ == '__main__':
    main()
