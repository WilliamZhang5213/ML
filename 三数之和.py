'''
双指针法解决三数之和
'''
nums = [-1,-2,0,1,2,2,3]
nums.sort()
res = []
for i in range(len(nums)-2):
    if nums[i]>0:
        break
    if nums[i]==nums[i+1]:
        continue
    l = i+1
    r = len(nums)-1
    data = -nums[i]
    while l<r:
        if nums[l]+nums[r]==data:
            res.append([nums[i],nums[l],nums[r]])
            while l<r and nums[l]==nums[l+1]:
                l+=1
            while l<r and nums[r]==nums[r-1]:
                r-=1
            l+=1
            r-=1
        elif nums[l]+nums[r]>data:
            r-=1
        else:l+=1
print(res)