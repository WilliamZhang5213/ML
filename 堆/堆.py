'''
内存中的堆与栈：
栈：自动分配，自动释放的空间（代码中不特别声明的就是栈：int a= 10）
堆：需要程序员在代码中自己申请的内存，需要手动释放
'''

'''
数据结构中的栈与堆：
栈：先进后出
堆：完全二叉树，常用的有最大堆（顶点最大），最小堆（顶点最小）
！！！二叉堆虽然是一颗完全二叉树，但它的存储方式并不是链式存储，而是顺序存储。换句话说，二叉堆的所有节点都存储在数组当中
！！！堆是完全二叉树，但完全二叉树不一定是堆
！！！一组数据可能对应着多个大顶堆或小顶堆
'''

#构建堆-内置方法
#heapq.heappush() 导入堆   heapq.heappop()  把堆从小到大pop出来（堆排序）
# import heapq
# heap = []
# data = [1,3,5,7,9,2,4,6,8,0]
# for i in data:
#     heapq.heappush(heap,i)
# print(heap)
# result = []
# while heap:
#     result.append(heapq.heappop(heap))
# print(result)

#也是生成堆 heapq.heapify
import heapq
data = [1,3,5,7,9,2,4,6,8,0]
heapq.heapify(data)
print(data)

