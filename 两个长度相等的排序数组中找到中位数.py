#给定两个有序数组arr1和arr2，已知两个数组的长度都为N，求两个数组中所有数的上中位数。要求时间复杂度O(logN)，空间复杂度O(1)
#中位数的含义：中间的数（上中位数：靠前的中位数（偶数情况））
arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]
#考虑情况
#1、两个数组都有一个元素，较小的数就为上中位数
#2、两个数组各有n个元素（n>1）：①如果arr1的上中位数与arr2的上中位数相等，随便返回一个就是结果；②不相等但n为基数，若arr1[mid1] > arr2[mid2]，数组arr1中mid1位置以后的数都不可能是整体的上中位数，数组arr2中mid2位置以前的数都不可能是整体的上中位数，只需要考虑arr1[left1…mid1]、arr2[mid2…right]（不保后，继续递归）；③不相等但n为偶数（n为偶数时考虑的是上中位数，所以两个剩下数组个数不一样），若arr1[mid1] > arr2[mid2]，数组arr1中mid1位置以后的数、数组arr2中mid2位置以前包括mid2位置都不可能有上中位数，只需要考虑arr1[left1…mid1]、arr2[mid2+1…right]（两个数组个数又相同了）

#类似于二分法
def getUpMedian(arr1, arr2):
    if arr1 == None or arr2 == None or len(arr1) != len(arr2):  #异常报错
        raise Exception("Your arr is invalid!")
    start1 = 0
    end1 = len(arr1) - 1
    start2 = 0
    end2 = len(arr2) - 1
    while start1 < end1:
        mid1 = (start1 + end1) // 2
        mid2 = (start2 + end2) // 2
        # offset = (end1 - start1 + 1) & 1 ^ 1   （原始的，不懂）
        # offset = (end1 - start1)%2
        offset = 1 if (end1 - start1 + 1)%2 == 0 else 0  #offset的意义在于区分奇数还是偶数
        # print(offset,end1 - start1+1)
        if arr1[mid1] == arr2[mid2]:
            return arr1[mid1]
        elif arr1[mid1] > arr2[mid2]:
            end1 = mid1
            start2 = mid2 + offset
        else:
            start1 = mid1 + offset
            end2 = mid2
    return min(arr1[start1], arr2[start2])