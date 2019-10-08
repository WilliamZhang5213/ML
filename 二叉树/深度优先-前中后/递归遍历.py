#生成树
class Node(object):
    def __init__(self, number):
        self.number = number
        self.lchild = None
        self.rchild = None
class Tree(object):
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
nums = [1,2,3,4,5,6,7]
a = Tree()
for i in nums:
    a.add(i)


# #先序遍历
# def pre(a):
#     if a == None:
#         return
#     print(a.number)
#     pre(a.lchild)
#     pre(a.rchild)
# pre(a.root)


#中序遍历
def mid(a):
    if a == None:
        return
    mid(a.lchild)
    print(a.number)
    mid(a.rchild)
mid(a.root)