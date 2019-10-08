#一条直线上，有n个房间，每个房间数量不等的财宝，一个盗贼希望从房屋中盗取财宝，由于房屋有警报器，同时从相邻两个房间盗取珠宝就会触发警报，求在不触发警报的情况下，最多可获取多少财宝？
a = [5,2,6,3,1,7]
#动态规划（最重要的是找状态转移方程）
def get_money(a):
    if len(a) == 0:
        return False
    elif len(a) == 1 or len(a) == 2:
        return max(a)
    else:
        dp = [0 for i in range(len(a))]
        dp[0] = a[0]
        dp[1] = max(a[:2])
        for i in range(2,len(a)):
            dp[i] = max(dp[i-2]+a[i],dp[i-1])
        return dp
a = [5,2,6,3,1,7]
print(get_money(a))

