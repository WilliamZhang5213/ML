'''
leetcode 452
射气球：贪心就好
'''

def pre(n):
    start=nums[n][0]
    res = 0
    for i in nums:
        if i[1]<=start:
            res+=1
    return res-1
def get(n):
    if n<0:
        return 0
    if n ==0:
        return 1
    if n>0:
        return get(pre(n))+1

onums=[[9.4,9.5],[8,9.3],[9.2,10],[9.4,10.3],[11,12.3],[8,12.5],[11.3,13],[15,16],[14,17]]
# global nums
nums = sorted(onums,key=lambda x:x[0])
print(get(len(nums)-1))

