price = [7,2,4,6,1,10]
#买卖一次
#暴力求解
# profit = 0
# for i in range(len(price)-1):
#     profit=max(profit,max(price[i+1:])-price[i])
# print(profit)



#dp
#可以买卖多次（不能当天买，当天卖）
dp = [[0]*2 for i in price]
dp[0][0],dp[0][1]=0,-price[0]
for i in range(1,len(price)):
    dp[i][0]=max(dp[i-1][0],dp[i-1][1]+price[i])
    dp[i][1]=max(dp[i-1][1],dp[i-1][0]-price[i])
print(dp)

#只可以买卖一次
# dp = [[0]*3 for i in price]
# dp[0][0],dp[0][1],dp[0][2]=0,-price[0],0
# for i in range(1,len(price)):
#     dp[i][0] = dp[i-1][0]
#     dp[i][1]=max(dp[i-1][1],dp[i-1][0]-price[i])
#     dp[i][2]=dp[i-1][1]+price[i]
# print(dp)