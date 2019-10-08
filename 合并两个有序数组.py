'''
合并两个有序数组
'''
nums1,nums2=[1, 2, 3],[4,5,6]
res=[]
while len(nums1)!=0 and len(nums2)!=0:
    if nums1[0]>nums2[0]:
        res.append(nums2.pop(0))
    else:
        res.append(nums1.pop(0))
if len(nums1) != 0 :
    res+=nums1
if len(nums2)!=0:
    res+=nums2
print(res)
'''
合并n个有序数组呢？（每个数组长度为m）
取每个数组第一个构建小顶堆（nlogm）
'''
