'''
冒泡排序：两两比较 O(N2)
选择排序：选择当前中最小的数而后去除，再找剩余数中最小的数 O(N2)
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
#         else:
#             break  #当某个值大于它前一个值时，由于之前的都是已经排好序的了，所以break
# print(a)
#希尔排序（步长=len(a)//2）
a = [13, 27, 49, 55, 4, 49, 38, 65, 97, 76]
bc = len(a)//2
while bc > 0 :
    print(a,bc)
    for i in range(bc,len(a)):
        for j in range(i,bc-1,-bc):  #类似于插入排序，与之前的比较
            if a[j] < a[j-bc]:
                a[j],a[j-bc]=a[j-bc],a[j]
    bc = bc//2
    # if bc == 0:
    #     break
    # bc = bc if bc > 0 else 1
    # print(bc)
print(a)


# def shell_sort(l):
#     n = len(l)
#     # 初始间隔
#     gap = n//2
#
#     while gap > 0:
#         for i in range(gap, n):
#             for j in range(i, gap-1, -gap):
#                 if l[j] < l[j-gap]:
#                     l[j], l[j-gap] = l[j-gap], l[j]
#                 else:
#                     break
#         gap //= 2
#
#
# if __name__ == '__main__':
#     l = [13, 27, 49, 55, 4, 49, 38, 65, 97, 76]
#     print(l)
#     shell_sort(l)
#     print(l)

# 快排（分治）
# def quick_sort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less_than_pivot = [x for x in array if x <= pivot]
#         more_than_pivot = [x for x in array if x > pivot]
#         return quick_sort(less_than_pivot) + [pivot] + quick_sort(more_than_pivot)

def QuickSortRecur(array, start, end):
    if start >= end:
        return
    low, high, pivotKey = start, end, array[start]
    while low < high:
        while low < high and array[high] >= pivotKey:
            high -= 1
        array[low], array[high] = array[high], array[low]
        while low < high and array[low] <= pivotKey:
            low += 1
        array[low], array[high] = array[high], array[low]

    QuickSortRecur(array, start, low - 1)
    QuickSortRecur(array, high + 1, end)