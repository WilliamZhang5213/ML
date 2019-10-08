'''
左视图：从左面去看这个树
大致方法：先找到树的深度,找到树每一层的节点list，每一节点取list[0]，合起来就是左视图（右视图为list[-1]）
'''


class Node:
    def __init__(self,number):
        self.number = number
        self.lchild = None
        self.rchild = None
class Tree:
    lis = []  #用来存放节点信息
    def __init__(self):
        self.root =None
    def add(self,number):
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
# 广度优先
def bfs(root):
    stack = [root]
    while stack:
        p = stack.pop()
        print(p.number)
        if p.lchild:
            stack.insert(0,p.lchild)
        if p.rchild:
            stack.insert(0,p.rchild)

def get_deep(root):
    if root.rchild == None and root.lchild == None:
        return 1
    if root.rchild:
        rlen = get_deep(root.rchild)
    else:rlen=0
    if root.lchild:
        llen = get_deep(root.lchild)
    else:llen = 0
    return 1+max(llen,rlen)
def find_len_node(root,n,target_node_list):
    if n == 1:
        target_node_list.append(root)
    if root.lchild:
        find_len_node(root.lchild,n-1,target_node_list)
    if root.rchild:
        find_len_node(root.rchild,n-1,target_node_list)
    return target_node_list

def look_at_left(root):
    deepth = get_deep(root)
    res = []
    for i in range(1,deepth+1):
        target_node_list = []
        res.append(find_len_node(root,i,target_node_list))
    for i in res:
        print(i[0].number) #左视图
        print(i[-1].number) #右视图


nums = [1,2,3,4,5,6,7,8]
a = Tree()
for i in nums:
    a.add(i)
look_at_left(a.root)





