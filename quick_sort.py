def quict_sort(nums,left,right):
    if left>=right:
        return nums
    key = nums[left]
    low = left
    high = right
    while left < right:
        while left<right and nums[right]>=key:
            right-=1
        nums[left]= nums[right]
        while left<right and nums[left]<=key:
            left+=1
        nums[right] = nums[left]

    nums[left] =key
    quict_sort(nums,low,left-1)
    quict_sort(nums,left+1,high)
    return nums

nums = [1,3,2,4,2,5,8,6]
left = 0
right = len(nums)-1
print (quict_sort(nums,left,right))

