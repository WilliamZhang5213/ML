'''
①先序遍历与中序遍历还原树；
②后序遍历
'''

class Node(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def rebuild(pre, center):
    if not pre:
        return
    cur = Node(pre[0])
    index = center.index(pre[0])
    cur.left = rebuild(pre[1:index + 1], center[:index])
    cur.right = rebuild(pre[index + 1:], center[index + 1:])
    return cur