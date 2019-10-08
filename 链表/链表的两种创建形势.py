#带有next属性
# class Node:
#     def __init__(self,data,next):
#         self.data = data
#         self.next = next
#
# head = None
# for i in range(5):
#     head = Node(i,head)
#     # head = head.next  #!!!此处不需要指向下一个
# while head !=None:
#     print(head.data)
#     head = head.next
#

#不带next属性
class Node:
    def __init__(self,data):  #不带有next
        self.data = data
        self.next = None  #直接给定了next的值

start = Node(0)
rel_start = start
for i in range(5):
    start.next = Node(i)
    start = start.next
end  = rel_start.next
while end != None:
    print(end.data)
    end = end.next





