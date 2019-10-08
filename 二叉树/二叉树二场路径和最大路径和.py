'''
!!!最长路径和最大路径和都不一定经过根节点!!!
最大路径和：
最长路径：
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
nums = [2,-3,3,4,-5,-6]
# nums= [1,2,3]
a = Tree()
for i in nums:
    a.add(i)


'''
一个节点要么作为路径的一部分，要么就是作为路径的根节点
    作为路径的根节点时，路径长就是左孩子的最大高度+右孩子的最大高度+1
    所以用计算高度的方式来计算，更新self.ans
    return的时候return当前高度，也就是说自己作为路径的一部分时的情况，
    (return的为当前树的深度，ans一直在更新树的最长路径)
'''
# def getHeight(root):
#     global ans
#     # ans = 1
#     print("ans:",ans)
#     if root == None:
#         return 0
#     l = getHeight(root.lchild)
#     r = getHeight(root.rchild)
#     ans = max(ans, l + r + 1)
#     print(ans)
#     return max(l, r) + 1
#
# ans = 1
# print(getHeight(a.root),ans)

'''
如果节点的左子树和右子树为空，那么连续子数组的最大和为这个节点值。
如果左子树不为空，那么遍历左子树，求出以左子树为根的树中连续子数组的最大和。
如果右子树不为空，那么遍历右子树，求出以右子树为根的树中连续子数组的最大和。
接着对从左子树最大和、右子树最大和、节点值、左子树最大和 + 节点值、右子树最大和 + 节点值、左子树+右子树+节点值中取出最大的保存即可。
'''


def maxPath(root):
    global res
    if not root:
        return 0
    left = max(0, maxPath(root.lchild))
    right = max(0, maxPath(root.rchild))
    res = max(res, left + right + root.number,left,right)
    return max(left, right) + root.number

res = float('-inf')
print(maxPath(a.root),res)




# def getmaxpath(root):
#     global maxpath
#     print("ans:",maxpath)
#     if root == None:
#         return 0
#     l = getHeight(root.lchild)
#     r = getHeight(root.rchild)
#     maxpath = max(maxpath, l + r + 1)
#     print(maxpath)
#     return max(l, r) + root.number
#
# maxpath = float('-inf')
# print(getmaxpath(a.root),maxpath)





