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


#先序遍历
# def pre(a):
#     stack = [a]
#     while len(stack):
#         p = stack.pop()
#         print(p.number)
#         if p.rchild:
#             stack.append(p.rchild)
#         if p.lchild:
#             stack.append(p.lchild)
# pre(a.root)


#后序遍历
# def after(root):
#     stack = [root]
#     out = []
#     while len(stack):
#         p = stack.pop()
#         if p.lchild:
#             stack.append(p.lchild)
#         if p.rchild:
#             stack.append(p.rchild)
#         out.append(p)
#     for i in out[::-1]:
#         print (i.number)
# root = a.root
# after(root)


#
def mid(root):
    stack = []
    p =root
    while stack or p:
        while p:
            stack.append(p)
            p = p.lchild
        if stack:
            p = stack.pop()
            print (p.number)
            p=p.rchild

root = a.root
mid(root)

