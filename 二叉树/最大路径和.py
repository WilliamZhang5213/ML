class Node(object):
    def __init__(self,val):
        self.val = val
        self.l =None
        self.r = None
class Tree(object):
    _lis = []
    def __init__(self):
        self.root = None
    def add(self,x):
        node = Node(x)
        if self.root == None:
            self.root = node
            Tree._lis.append(node)
        else:
            tmp = Tree._lis[0]
            if tmp.l == None:
                tmp.l = node
                Tree._lis.append(node)
            elif tmp.r == None:
                tmp.r = node
                Tree._lis.append(node)
                Tree._lis.pop(0)
            else:
                return
def getmax(root):
    global res
    if not root:
        return 0
    lmax = getmax(root.l)
    rmax = getmax(root.r)
    res = max(res,lmax+rmax+root.val)
    return max(lmax,rmax)+root.val
nums = [2,-3,3,4,-5,-6]
a = Tree()
for i in nums:
    a.add(i)
root = a.root
res = float('-inf')
print(getmax(root),res)


