class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None
nums = [1,2,3,4,5]
head = Node(nums[0])
head1 = head
for i in nums[1:]:
    head.next = Node(i)
    head = head.next

# #单链表的反转
# pre = None
# while head1:
#     tmp = head1.next
#     head1.next = pre
#     pre = head1
#     head1 = tmp
# while pre:
#     print(pre.val)
#     pre=pre.next

#链表双双转换
# pre = Node(1)
# pre1 = pre
# pre.next = head1
# while pre.next and pre.next.next:
#     node1 = pre.next
#     node2 = node1.next
#     lat = node2.next
#
#     pre.next = node2
#     node2.next = node1
#     node1.next =lat
#
#     pre = node1
# res = pre1.next
# while res:
#     print(res.val)
#     res = res.next



#有序链表的合并
def merge(head1,head2):
    if head1 == None:   #head1而非head1.next
        return head2
    if head2 == None:
        return head1
    if head1.val > head2.val:
        head = head2
        head.next= merge(head1,head2.next)
    else:
        head = head1
        head.next = merge(head1.next,head2)
    return head
nums1 = [1,3,5]
head = Node(nums1[0])
head1 = head
for i in nums1[1:]:
    head.next = Node(i)
    head = head.next
nums2=[2,4,6]
head11 = Node(nums2[0])
head2 = head11
for i in nums2[1:]:
    head11.next = Node(i)
    head11 = head11.next
a = merge(head1,head2)
while a:
    print(a.val)
    a=a.next