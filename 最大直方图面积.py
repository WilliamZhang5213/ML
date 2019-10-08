'''
给定一个直方图（下图a），求直方图中能够组成的所有矩形中，面积最大为多少(宽度均为1)
'''
heights = [2,1,5,6,2,3]

#暴力求解 (复杂度O(n2))
# n = len(heights)
# res = 0
# for i in range(n):
#     for j in range(i,n):
#         height = min(heights[i:j+1])
#         res = max(res,height*(j-i+1))
# print(res)

#一次遍历求解 （栈）
heights = [0]+heights+[0]
res = 0
stack = []
for i,num in enumerate(heights):
    print('a')
    while stack and heights[stack[-1]]>num:
        top = stack.pop()
        tmp = (i-stack[-1]-1)*heights[top]
        print(tmp)
        res = max(res,tmp)
    stack.append(i)
print(res)
