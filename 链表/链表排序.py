# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None
#
#
# '''
# 时间：O(n)  空间O(1)
# 思想：归并排序
# '''
# class Solution:
#     def sortList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if head is None or head.next is None:
#             return head
#         mid = self.get_mid(head)
#         l = head
#         r = mid.next
#         mid.next = None
#         return self.merge(self.sortList(l), self.sortList(r))
#
#     def merge(self, p, q):
#             tmp = ListNode(0)
#             h = tmp
#             while p and q:
#                 if p.val < q.val:
#                     h.next = p
#                     p = p.next
#                 else:
#                     h.next = q
#                     q = q.next
#                 h = h.next
#             if p:
#                 h.next = p
#             if q:
#                 h.next = q
#             return tmp.next
#
#     def get_mid(self, node):
#         if node is None:
#             return node
#         fast = slow = node
#         while fast.next and fast.next.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow


class Node(object):
    def __init__(self,val):
        self.val=val
        self.next = None

def link_sort(label):
    if label is None or label.next is None:
        return label
    mid =getmid(label)
    l = label
    r = mid.next
    mid.next = None
    l_part = link_sort(l)
    r_part = link_sort(r)
    return rebuild(l_part,r_part)

def rebuild(l,r):
    res=Node(0)
    tmp =res
    while l and r:
        if l.val<r.val:
            res.next =l
            l=l.next
        else:
            res.next = r
            r=r.next
        res = res.next
    if l:
        res.next = l
    if r:
        res.next = r
    return tmp.next

def getmid(node):
    if node == None:
        return node
    slow,fast=node,node
    while node.next and node.next.next:
        slow = slow.next
        fast = fast.next.next
        node = fast
    return slow

nums=[2,4,1,6,3,0,9,8]
a=Node(nums[0])
label = a
for i in nums[1:]:
    a.next = Node(i)
    a = a.next
res = link_sort(label)
while res:
    print(res.val)
    res=res.next