class Node(object):
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

head = None
for i in [2,3,4,1,5,6]:
    head = Node(i,head)
# while head != None:
#     print(head.val)
#     head = head.next

#反转链表  （分裂 重组）
pre = None
while head != None:
    tmp = head.next
    head.next =pre  #分裂出来，对于首节点而言指向的为空
    pre = head
    head = tmp #重组  最终pre为反转后形成的新链表

while pre != None:
    print(pre.val)
    pre=pre.next