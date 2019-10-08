class Node:
    def __init__(self, number):
        self.number = number
        self.lchild = None
        self.rchild = None


class Tree:
    lis = []
    def __init__(self):
        self.root = None
    def add(self, number):
        node = Node(number)
        if self.root == None:
            self.root = node
            Tree.lis.append(self.root)
        else:
            while True:
                point = Tree.lis[0]
                if point.lchild == None:
                    point.lchild = node
                    Tree.lis.append(point.lchild)
                    return
                elif point.rchild == None:
                    point.rchild = node
                    Tree.lis.append(point.rchild)
                    Tree.lis.pop(0)
                    return

#层次遍历-广度优先
def bfs(root):
    stack = [root]
    while stack:
        p = stack.pop()
        print(p.number)
        if p.lchild:
            stack.insert(0,p.lchild)
        if p.rchild:
            stack.insert(0,p.rchild)

def find_deep(root):
    if root.rchild == None and root.lchild == None:
        return 1
    if root.lchild:
        llength = find_deep(root.lchild)
    else:
        llength = 0
    if root.rchild:
        rlength = find_deep(root.rchild)
    else:
        rlength = 0
    return 1+max(llength,rlength)


nums = [1,2,3,4,5,6,7]
a = Tree()
for i in nums:
    a.add(i)
print(find_deep(a.root))

