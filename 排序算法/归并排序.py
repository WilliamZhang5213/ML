def merge_sort(nums):
    if len(nums)<=1:
        return nums
    num = len(nums)//2
    left = merge_sort(nums[:num])
    right = merge_sort(nums[num:])
    return merge(left,right)
def merge(left,right):
    l,r = 0,0
    res = []
    while l < len(left) and r < len(right):
        if left[l]<=right[r]:
            res.append(left[l])
            l+=1
        else:
            res.append(right[r])
            r+=1
    res+=left[l:]
    res+=right[r:]
    return res

nums = [5,3,2,1,100,50]
print(merge_sort(nums))
