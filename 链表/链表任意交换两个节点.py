class Node(object):
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

head = None
for i in range(8,0,-1):
    head = Node(i,head)
# while head != None:
#     print(head.data)
#     head = head.next

head1,head2 = head,head
a1,a2 = 3,7
b1,b2 = a1,a2
while a1 >0 or a2 >0:
    a1 -= 1
    a2 -= 1
    if a1 == 0:
        num1 = head1.data
    if a2 == 0:
        num2 = head1.data
    head1 = head1.next
while b1 > 0 or b2 > 0 :
    b1 -= 1
    b2 -= 1
    if b1 == 0:
        head2.data = num2
    if b2 == 0:
        head2.data = num1
    head2 = head2.next
while head != None:
    print(head.data)
    head = head.next