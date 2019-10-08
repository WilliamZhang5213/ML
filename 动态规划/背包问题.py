# 0-1 背包问题：给定 n 种物品和一个容量为 C 的背包，物品 i 的重量是 wi，其价值为 vi 。
# 问：应该如何选择装入背包的物品，使得装入背包中的物品的总价值最大（每件只有一个）？
v = [60, 100, 120]
w = [10, 20, 30]
weight = 50
n = 3
#递归，自上而下想，拿了w1物品后，剩余的钱买剩余产品的最大价值
#用二维数组dp[i][j]表示针对i个产品j元钱的时候所能得到的最大价值

dp = [[0 for i in range(weight+1)]for j in range(n+1)]  #动态规划矩阵
for i in range(1,n+1):
    for j in range(1,weight+1):
        if j >= w[i-1]:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i-1]]+v[i-1])  #状态转移方程
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])


# w = [ 1, 4, 3, 1]   #n个物体的重量
# p = [1500, 3000, 2000, 2000]   #n个物体的价值(
# n = len(w)    #计算n的个数
# m = 4   #背包的载重量
# dp = [[0 for i in range(m+1)]for j in range(n+1)]
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         if j < w[i-1]:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i-1]]+p[i-1])
# print(dp)