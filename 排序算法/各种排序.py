'''
冒泡排序：两两比较 O(N2)  双重遍历
选择排序：选择当前中最小的数而后去除，再找剩余数中最小的数 O(N2)
希尔排序(O(log(N**1.3)))（插入排序）：
step = len(a)
while step > 0:
    for i in range(step,len(a)):
        for j in range(i,step-1,-step):
            if a[j-step] > a[step]:
                a[j-step],a[step]=a[step],a[j-step]
    step = step//2
快速排序：分治 递归
'''

# 插入排序(从第二个值开始（索引为1），向之前的值（由后向前）进行比较，保证每个外围循环结束之后，之前的数组是有序的) O(N2)
# a = [13, 27, 49, 55, 4, 49, 38, 65, 97, 76]
# for i in range(1,len(a)):
#     for j in range(i,0,-1):
#         print(a[j],a[j-1])
#         if a[j] < a[j-1]:
#             num = a[j]
#             a[j] = a[j-1]
#             a[j-1] = num
#             print(a)
# print(a)
#希尔排序（步长=len(a)//2）
# a = [13, 27, 49, 55, 4, 49, 38, 65, 97, 76]
# bc = len(a)//2
# while bc > 0 :
#     print(a,bc)
#     for i in range(bc,len(a)):
#         for j in range(i,bc-1,-bc):  #类似于插入排序，与之前的比较
#             if a[j] < a[j-bc]:
#                 a[j],a[j-bc]=a[j-bc],a[j]
#     bc = bc//2
# print(a)


def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:   #一个元素或者空元素
        return lists
    key = lists[left]  #设置基准值
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]     #注意四个空格
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]    #注意四个空格
    lists[left] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists
# print quick_sort(L,0,5)

array = [1,4,7,3,8,34,67,234,81,2]
print(quick_sort(array,0,len(array)-1))