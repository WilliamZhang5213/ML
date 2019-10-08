#python借助node类创建链表
class Node(object):
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

# 将数据导入链表
# 注意：将list导入链表之后方向改变，指针是由后向前，所以在按位置选取节点的时候要注意
head = None
for i in [3,2,5,8,1,10,5]:
    # print(i)
    head = Node(i,head)

# 遍历
# while head != None:
#     print(head.data)
#     print(head.next)
#     head=head.next

# 遍历 (变的一直是prob，而head没变（这两个都是指针）)
# prob = head
# while prob != None:
#     print(prob.data)
#     prob = prob.next
# print(prob,head.data)

#搜索（指定值）
# prob = head
# while prob.data != 3:
#     print(prob.data)
#     prob=prob.next
#搜索（指定位置）
# num = 1
# prob = head
# while num > 0:
#     prob=prob.next
#     num-=1
# print(prob.data)

#替换数据
#eg：将第三个节点的value变为50
# num = 2
# prob = head
# while num >0:
#     prob = prob.next
#     num-=1
# prob.data = 50
# while head != None:
#     print(head.data)
#     head =head.next


#插入数据
#头部插入
# head = Node('a',head)
# while head != None:
#     print(head.data)
#     head =head.next
#尾部插入(当next指向为None的时候，next指向一个新节点)
# newnode = Node('a',None)
# prob = head
# while head.next != None:
#     # print(head.data)
#     head =head.next
# head.next =newnode #next指向一个新节点
# while prob != None:
#     print(prob.data)
#     prob=prob.next
#中间位置插入
prob = head
num = 0
while num < 0:
    prob = prob.next
    num-=1
newnode = Node('a',prob.next.next)
prob.next =newnode
while head != None:
    print(head.data)
    head=head.next