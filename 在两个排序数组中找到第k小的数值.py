'''
题目描述
给定两个有序数组arr1和arr2，再给定一个整数k，返回所有的数中第k小的数。要求时间复杂度O(log(min{M,N}))，额外空间复杂度O(1)。
1、两个数组只是有序但并没有说长度相等；
2、假如要返回两个数组的中位数，相应的可以转化为k值（第k小正好是中位数）
'''
'''
解题思路(基础：在两个等长的有序数组中寻找中位数):转化为求中位数
假设两个数组，长度较短的数组为shortArr，长度记为lenS；长度较长的数组为longArr，长度记为lenL。那么对于整数k，有以下三种情况
1、k < lenS。那么在shortArr中选前k个数，在longArr中也选前k个数，这两段数组中的中位数就是整体的第k个最小。

2、k > lenL。对于longArr中的前k-lenS-1个数，都不能满足要求，因为即使它们比shortArr中所有的数都大，也无法达到第k个。longArr中的第k-lenS个数，如果它比shortArr中的所有数都大，那么它就是第k小数，否则，它也不是。对于shortArr中的前k-lenL-1个数，都不能满足要求，因为即使它们比longArr中所有的数都大，也无法达到第k个。shortArr中的第k-lenL个数，如果它比longArr中的所有数都大，那么它就是第k小数，否则，它也不是。如果shortArr[k-lenL-1]和longArr[k-lenS-1]都不是第k小的数，那么shortArr[k-lenL…lenS-1]和longArr[k-LenS…lenL-1]这两段数组 的中位数就是整体的第k小数。

3、lenS < k < lenL。对于longArr中的前k-lenS-1个数，都不能满足要求，因为即使它们比shortArr中所有的数都大，也无法达到第k个。longArr中的第k-lenS个数，如果它比shortArr中的所有数都大，那么它就是第k小数，否则，它也不是。对于longArr中的第k个数以后部分，也都不能满足要求。如果longArr[k-lenS-1]不是第k小数，那么shortArr[0…lenS-1]和longArr[k-lenS…k-1]这两段数组 的中位数就是整体的第k小数。
'''
#二分法求取中位数（两个等长排序数组）
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

def findKthNum(arr1, arr2, k):
    #异常处理
    if arr1 == None or arr2 == None:
        raise Exception("Your arr is invalid!")
    if k < 1 or k > (len(arr1) + len(arr2)):
        raise Exception("K is invalid!")
    longs = arr1 if len(arr1) > len(arr2) else arr2
    shorts = arr1 if len(arr1) <= len(arr2) else arr2
    l = len(longs)
    s = len(shorts)
    if k <= s:
        return getUpMedian(shorts[0:k-1],longs[0:k-1])
    if k > l:
        if longs[k-s-1] >= shorts[-1]:
            return longs[k-s-1]
        if shorts[k-l-1] >= longs[-1]:
            return shorts[k-l-1]
        return getUpMedian(longs[k-s, l-1], shorts[k-l, s-1])
    if k > s and k <= l:
        if longs[k-s-1] >= shorts[-1]:
            return longs[k-s-1]
        else:
            return getUpMedian(shorts,longs[k-s,k-1])
    # if longs[k-s-1] >= shorts[-1]:
    #     return longs[k-s-1]
    # print(222)
    # return getUpMedian(longs, k-s, k-1, shorts, 0, s-1)
