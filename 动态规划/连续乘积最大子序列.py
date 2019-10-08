#连续子序列乘积最大（乘积最小）
#与连续子序列和最大的不同在于负负得正
nums = [1,2,-1,3,-5,0]
# nums = [1,2,-1]
#关键想法：每个节点多一个状态，最大值与最小值
dp = [ [0,0] for i in nums]
dp[0][0] = nums[0]
dp[0][1] = nums[0]
max_n = nums[0]
min_n = nums[0]
for i in range(1,len(nums)):
    dp[i][0] = max(dp[i-1][0]*nums[i],dp[i-1][1]*nums[i],nums[i])   #一个存放max ！！！注意是三个数比较
    dp[i][1] = min(dp[i-1][0]*nums[i],dp[i-1][1]*nums[i],nums[i])   #一个存放min
    max_n = max(max_n,dp[i][0])
    min_n =min(min_n,dp[i][1])
print(dp)
print(max_n,min_n)
