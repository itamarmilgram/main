N = int(input("number of positions: "))
starting_arr = []
for i in range(N):
    starting_arr.append(0)
n_inf = 0
n_non_inf = 0

class Node:
    def __init__(self, value=None, parent=None, child=[]):
        self.value = value
        self.parent = parent
        self.children = list()
        kids = child
        if self.value and self.value in kids:
            kids.remove(self.value)
        for num in kids:
            kid = kids.copy()
            kid.remove(num)
            self.children.append(Node(num, child=kid))

    def print_perm(self):
        def func(value, children, val=''):
            if children:
                for child in children:
                    func(child.value, child.children, val=val + str(value) if value else '')
            else:
                print(val + str(value))
        func(self.value, self.children)

class Tree:
    def __init__(self, N):
        self.head = Node(child=list(range(1, N + 1)))

    def print_perm(self):
        return self.head.print_perm()

root = Tree(N)
print(root.print_perm())
