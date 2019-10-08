import copy
class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

head = None
for i in range(5):
    head = Node(i,head)
a = copy.copy(head)
print(a.data)

pre = None
while head != None:
    tmp = head.next
    head.next =pre  #分裂出来，对于首节点而言指向的为空
    pre = head
    head = tmp

while a !=None:
    print(a.data)
    a = a.next
