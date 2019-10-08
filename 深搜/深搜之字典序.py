'''
字典序：按照字典形式进行的排序
全排列
'''
#深度搜索
def dfs(s,res,tmp):
    if not s:
        res.append(tmp)
    for i in range(len(s)):
        ntmp=tmp+s[i]
        dfs(s[:i]+s[i+1:],res,ntmp)
s= 'abc'
res = []
tmp=''
dfs(s,res,tmp)
print(res)

#寻找任一字典序的下一排列
#eg:abc的下一排列为acb
# def nextPermutation(nums):
#     """
#     :type nums: List[int]
#     :rtype: void Do not return anything, modify nums in-place instead.
#     寻找基于字典序的下一个排列。
#     """
#     l = len(nums)
#
#     # 从右向左查询第一个小于右邻的元素
#     for i in range(l - 2, -1, -1):
#         if nums[i + 1] > nums[i]:
#             break
#     else:  # 没有找到，说明为降序排列
#         nums[:] = nums[::-1]
#         return
#
#     # 从右向左查询第一个大于nums[i]的元素
#     for j in range(l - 1, -1, -1):
#         if nums[j] > nums[i]:
#             break
#
#     # 交换i和j
#     nums[i], nums[j] = nums[j], nums[i]
#
#     # i后面的序列进行反转
#     nums[i + 1:l] = nums[-1:i:-1]
#     return nums
# print(nextPermutation(['a','b','c']))
