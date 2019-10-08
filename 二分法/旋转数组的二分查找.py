'''
有序数组：[1,2,3,4,5,6,7]
旋转有序数组：[5,6,7,1,2,3,4]
整体不再有序，但部分有序
核心思想：mid = len(nums)//2 左右一定有一个是有序的
'''


def xuanzhuan_erfen(nums,target):
    low = 0
    high = len(nums)-1
    mid = high//2-1
    if nums[mid] == target:
        return mid
    if nums[mid] >= nums[0]:
        if nums[mid] > target and target >= nums[low]:
            high = mid-1
        else:
            low = mid+1
    if nums[mid] <= nums[high]:
        if nums[mid] < target and nums[high]>= target:
            low = mid+1
        else:
            high = mid-1
    xuanzhuan_erfen(nums[low,high],target)

nums = [5,6,7,1,2,3,4]
target = 2
low = 0
high = len(nums)-1
while low <= high:
    mid = (high-low)//2+low
    print(mid)
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] >= nums[0]:
        if nums[mid] > target and target >= nums[low]:
            high = mid-1
        else:
            low = mid+1
    elif nums[mid] <= nums[high]:
        if nums[mid] < target and nums[high]>= target:
            low = mid+1
        else:
            high = mid-1
    print(low,high)
# print('no')

