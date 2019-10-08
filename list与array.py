# list python中的list是python的内置数据类型，list中的数据类不必相同的，而array的中的类型必须全部相同。在list中的数据类型保存的是数据的存放的地址，简单的说就是指针，并非数据，这样保存一个list就太麻烦了，例如list1=[1,2,3,'a']需要4个指针和四个数据，增加了存储和消耗cpu。

#array 数组，查询的复杂度为O(1),增删的复杂度为O(n)  array类型数据存储方式是连续的，并且直接指代，而列表（list）的线反而显得杂乱无章，还需要通过寻址来存储，这就导致了numpy在计算的时候虽然类型单一，但没有太多循环的限制

#链表 ，查询的复杂度为O(),增删的复杂度为O(n1) 链表中的指针都是指向下一个元素，查询从头开始查，一层层指向（O（n）），删除直接该指针（0（1））.


#! conding:utf-8
__author__ = "hotpot"
__date__ = "2017/10/30 9:20"

class Linknode(object):
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

def list_2_linknode(array):
    tem_node = Linknode()
    node = Linknode()
    for i  in array:
        #记得是判定val是否有值，并且用一个node记住头节点，然后返回的是头节点
        if not tem_node.val:
            tem_node.val =i
            node = tem_node
        else:
            tem_node.next = Linknode(i)
            tem_node = tem_node.next
    return node

if __name__ == '__main__':
    array = [1,2,3,4,5]
    a = list_2_linknode(array)
    print(a.next.next.next.next.val)
