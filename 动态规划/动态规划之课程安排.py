'''
动态规划算法之课程安排
问题：教务处给某一个教室安排课程，有很多老师都想来这个教室教授他们各自的课。假如第i位老师讲的第Ai门课程，课程开始时间Si,结束时间为Fi。那么教务处的老师就要利用这个时间如何安排课程，使得来这间教室上课的人数最多

最重要的一点：按照结束时间升序排序

'''

#第一种：每门课程的上课人数一样（eg，都为1），此时只要安排的课程数量最多就好（互不重叠的最大数量）
#贪心解法：①按照结束时间升序排序；②最早结束的一定会选（贪心算法：局部最优），画图更容易理解；
# onums=[[9.4,9.5],[8,9.3],[9.2,10],[9.4,10.3],[11,12.3],[8,12.5],[11.3,13],[15,16],[14,17]]
# nums=sorted(onums,key=lambda x:x[1])
# n=len(nums)
# res_l = []
# res = 1
# res_l.append(nums[0])
# end_time = nums[0][1]
# for i in range(1,n):
#     if nums[i][0]>=end_time:
#         end_time=nums[i][1]
#         res_l.append(nums[i])
#         res+=1
# print(res,res_l)


# 第二种：每门课程的上课人数不一样，要求最终总的上课人数最多
# 加了权重，不能贪心
# 动态规划(重要的思路：每个课程选定之后，只能选择这门课程开始时间之前已经结束的课程（pre的功能）)
def pre(n,nums):
    start_time = nums[n][0]
    res = 0
    for i in nums:
        if i[1]<=start_time:
            res+=1
    return res-1
def get(n,nums):
    if n <0:
        return 0
    if n==0:
        return nums[0][2]
    if n>0:
        return max(get(pre(n,nums),nums)+nums[n][2],get(n-1,nums))
onums=[[8,9,1],[8,9.3,5],[9.2,10,4],[9.4,10.3,2],[11,12.3,3],[8,12.5,2],[11.3,13,1],[15,16,3],[14,17,5]]
nums=sorted(onums,key=lambda x:x[1])
print(get(len(nums)-1,nums))

