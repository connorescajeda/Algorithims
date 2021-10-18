import array as arr


class UnionSet:

    def __init__(self, parent):
        self.parent = parent

    def find(self):
        if self.parent is None:
            return self
        else:
            return self.parent.find()
    def union(self, node):
        root1 = self.find()
        root2 = node.find()
        root1.parent = root2

def main():
    rows, cols = (5, 5)
    grid = [["C"]*cols]*rows
    for row in grid:
        print(row)

if __name__ == '__main__':
    main()
