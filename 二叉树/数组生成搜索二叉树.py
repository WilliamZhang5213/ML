'''
先把数组变为有序数组
'''

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(nums):
    if not nums:
        return None
    length = len(nums)
    mid = length // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])
    return root
def cengci(root):
    stack =[root]
    while stack:
        p=stack.pop()
        print(p.val)
        if p.left:
            stack.insert(0,p.left)
        if p.right:
            stack.insert(0,p.right)
def pre(root):
    stack = [root]
    while stack:
        p = stack.pop()
        print(p.val)
        if p.right:
            stack.append(p.right)
        if p.left:
            stack.append(p.left)
def mid(root):  #搜索二叉树中序遍历的结果是有序的
    stack = []
    p = root
    while stack or p:
        while p:
            stack.append(p)
            p=p.left
        if stack:
            p = stack.pop()
            print(p.val)
            p=p.right
def after(root):
    stack = [root]
    output = []
    while stack:
        p = stack.pop()
        output.append(p)
        if p.left:
            stack.append(p.left)
        if p.right:
            stack.append(p.right)
    while output:
        print(output.pop().val)

def find_deep(root):
    if not root:
        return 0
    llen = find_deep(root.left)
    rlen = find_deep(root.right)
    return max(rlen,llen)+1
def find_long(root):
    global res
    if not root:
        return 0
    llen = find_deep(root.left)
    rlen = find_deep(root.right)
    res = max(res,llen+rlen+1)
    return max(rlen,llen)+1

def getMax(root):
    global max_res
    if root == None:
        return 0
    left = max(0, getMax(root.left))
    right = max(0, getMax(root.right))
    max_res = max(max_res, left + right + root.val)
    return max(left, right) + root.val

nums = [-1,2,3,4,5,6,7,8,9,10]
root = sortedArrayToBST(nums)
# after(root)
res = 0
max_res = float('-inf')
print(find_max(root))
print(max_res)
