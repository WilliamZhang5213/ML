import copy
class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

head = None
for i in range(5):
    head = Node(i,head)
    # head = head.next  #!!!此处不需要指向下一个
# while head !=None:
#     print(head.data)
#     head = head.next
test1 = copy.copy(head)
rev_head = head
pre = None
while rev_head != None:
    tmp = rev_head.next
    rev_head.next = pre
    pre = rev_head
    rev_head = tmp
# print(pre.data)
# count  = 1
# new = head
# head = head.next
# # print(new.data)
# test = new
# while count <= 5:
#     count+=1
#     if count%2 == 1:
#         print("zh")
#         new.next = head
#         head = head.next
#     else:
#         print("fan")
#         new.next = pre
#         pre = pre.next
#     new=new.next
#     print(new.data)


while test1 != None:
    print(test1.data)
    test1 = test1.next