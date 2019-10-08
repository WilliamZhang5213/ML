'''
情景①：无序数组取第k大的数；
情景②：10亿个数里面取出前1000大的数
解析：①不需要整体排序；②局部有序：快排中的先整体有序后局部有序思想（partition），堆排序中的大顶堆/小顶堆思想。
'''
#①快排，k索引取值；O(n*lgn)
#②k的小顶堆  O(n*lgk)
#③改进快排

def class_sort(nums): #单次快排
    left = 0
    right = len(nums) - 1
    key = nums[left]
    while left < right:
        while left < right and nums[right] > key:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] < key:
            left += 1
        nums[right] = nums[left]
    nums[left] = key
    return nums[:left],nums[left],nums[left+1:]
def find_k(nums,k):  #条件筛选
    left_l, mid, right_l = class_sort(nums)
    if len(right_l) == k-1:
        return  mid
    elif len(right_l) > k-1:
        return find_k(right_l,k)
    else:
        return find_k(left_l,k-len(left_l))
nums = [99,1,34,223,23,45,10,67]
k = 2
print(find_k(nums,k))





