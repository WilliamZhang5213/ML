class Node(object):
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
head1 = None
for i in reversed([1,3,5,7]):
    head1 = Node(i,head1)
head2 = None
for j in reversed([2,4,6,8]):
    head2 = Node(j,head2)

# #合并链表后生成一个新链表，也就是说有一个新指针（newhead）
# newhead = Node('',next=None)
# begin = newhead  #newhead是一个节点，在下面的操作中newhead一直在指向其下一个，所以在一开始我们要记录其首节点，不然到最后如果返回newhead的话只是一个节点，其之前的值全部消失
# while head1 != None or head2 != None:
#     if head1 == None:
#         newhead.next = head2
#     if head2 == None:
#         newhead.next = head1
#         break
#     else:
#         if head1.data >= head2.data:
#             newhead.next = head1
#             # print(head1.data)
#             # newhead = Node(head1.data,newhead)
#             head1 = head1.next
#         else:
#             newhead.next = head2
#             # print(head2.data)
#             # newhead = Node(head2.data, newhead)
#             head2 = head2.next
#         newhead = newhead.next
#         # print(head1,head2)
# while begin != None:
#     print(begin.data)
#     begin = begin.next

#优化合并
# def merge(head1,head2):
#     if head1 == None:
#         return head2
#     elif head2 == None:
#         return head1
#     else:
#         if head1.data >= head2.data:
#             head = head2
#             head2 = head2.next
#         else:
#             head =head1
#             head1 = head1.next
#         tmp = head
#     while head1 and head2:
#         if head1.data >= head2.data:
#             tmp.next = head2
#             head2 = head2.next
#         else:
#             tmp.next = head1
#             head1 = head1.next
#         tmp =tmp.next    #tmp每次循环要next一次，不然tmp只会保存最后的信息
#     if head1 == None:
#         tmp.next = head2
#     else:
#         tmp.next = head1
#     return head
#
# head = merge(head1,head2)
# while head != None:
#     print(head.data)
#     head = head.next


#递归合并(递归的本质：自调)
def merge(head1,head2):
    if head1 == None:
        return head2
    elif head2 == None:
        return head1
    else:
        if head1.data <= head2.data:
            head = head1
            head.next = merge(head1.next,head2)
        else:
            head = head2
            head.next = merge(head1,head2.next)
    return head

head = merge(head1,head2)
while head != None:
    print(head.data)
    head = head.next