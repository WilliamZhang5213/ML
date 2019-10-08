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
# nums = [1,2,3,4,5,6]
nums = [1,-3,3,4,-5,-6]
a = Tree()
for i in nums:
    a.add(i)




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
    if root.lchild == None and root.rchild == None:
        return 1
    if root.lchild:
        llen = find_deep(root.lchild)
    else:
        llen = 0
    if root.rchild:
        rlen = find_deep(root.rchild)
    else:
        rlen = 0
    return max(llen,rlen)+1
def find_deep_2(root):
    if not root:
        return 0
    llen = find_deep_2(root.lchild)+1
    rlen = find_deep_2(root.rchild)+1
    return max(llen,rlen)

def find_target_node(root,n,target=[]):
    if n == 1:
        target.append(root)
    if root.lchild:
        find_target_node(root.lchild,n-1,target)
    if root.rchild:
        find_target_node(root.rchild,n-1,target)
    return target


# # 寻找最长路径
# def findMaxPathRecursive(root, maxs):
#     if root == None:
#         return 0
#     else:
#         # 求左子树以root.left为起始结点的最大路径和
#         sumLeft = findMaxPathRecursive(root.lchild, maxs)
#         # 求右子树以root.right为起始结点的最大路径和
#         sumRight = findMaxPathRecursive(root.rchild, maxs)
#         # 求以root为起始结点，叶子结点为结束结点的最大路径和
#         allmax = root.number + sumLeft + sumRight
#         leftMax = root.number + sumLeft
#         rightMax = root.number + sumRight
#         tmpMax = max(allmax, leftMax, rightMax)
#
#         if tmpMax > maxs:
#             maxs = tmpMax
#
#         subMax = sumLeft
#         if sumLeft < sumRight:
#             subMax = sumRight
#     return root.number + subMax
# def findMaxPath(root):
#     # maxs = IntRef()
#     maxs = -2 ** 31
#     findMaxPathRecursive(root, maxs)
#     return maxs

def getMax(root):
    if root == None:
        return 0
    left = max(0, getMax(root.lchild))
    right = max(0, getMax(root.rchild))
    return max(left, right) + root.number

curr_max = float('-inf')
print(getMax(a.root.lchild),getMax(a.root.rchild))
print(find_deep(a.root))
for i in find_target_node(a.root,2,target=[]):
    print(i.number)

