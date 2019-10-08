#python借助node类创建链表
class Node(object):
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

# 将数据导入链表
# 注意：将list导入链表之后方向改变，指针是由后向前，所以在按位置选取节点的时候要注意
head = None
for i in [8,3,2,5,8,1,10,8,5,8]:
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
# prob = head
# num = 5
# while num != 0:
#     prob = prob.next
#     num-=1
# newnode = Node('a',prob.next) #新建一个node，此节点的next定义为当前prob的next
# prob.next =newnode   #将当前的prob的next重新指向
# while head != None:
#     print(head.data)
#     head=head.next


# 删除
# 删除首节点
# head=head.next #直接跳过当前的首节点就好
#删除任一节点(根据val来删除，不完善，多个重复值咋办)
# prob = head
# while prob.next.data != 8:
#     prob = prob.next
# prob.next = prob.next.next
# while head != None:
#     print(head.data)
#     head=head.next
#删除任一节点(根据val来删除，已完善)
num = 0
num_lsit = []
prob1 = head
while prob1.next != None:    #这儿先不考虑首节点
    # num += 1
    if prob1.next.data == 8:
        prob1.next = prob1.next.next
    else:
        prob1=prob1.next
if head.data == 8:  #为什么这儿才考虑首节点？一开始考虑首节点，如果删除首节点会有新的首节点出现，不如先不考虑首节点，最后统一处理首节点
    head = head.next
while head != None:
    print(head.data)
    head=head.next