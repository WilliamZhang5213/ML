def makeclass(nums,left,right):
    if left>=right:
        return nums
    key = nums[left]
    print(key)
    while left < right:
        while left<right and nums[right]%2 == 0:
            right-=1
        nums[left] = nums[right]
        print("1:"+str(nums))
        while left<right and nums[left] %2 == 1:
            left+=1
        nums[right]= nums[left]
        print("2:" + str(nums))
        print("left:"+str(left)+" right:"+str(right))
    nums[left] = key
    return nums

nums=[10,20,30,5,4,3,2,1]
print(makeclass(nums,0,len(nums)-1))