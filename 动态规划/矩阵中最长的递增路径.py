nums =[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
m = len(nums)
n =len(nums[0])
dp = [[1 for i in range(n)] for j in range(m)]
num_dict  = {}
nums_max = 0
for i in range(m):
	for j in range(n):
		num_dict[(i,j)] = nums[i][j]
new_dict= sorted(num_dict.items(),key = lambda x:x[1])
print(new_dict)
v = num_dict.keys()
for k in new_dict:
	print(k)
	i = k[0][0]
	j = k[0][1]
	if (i+1,j) in v and nums[i+1][j] < nums[i][j] :
		dp[i][j]=dp[i+1][j]+1
	if (i-1,j) in v and nums[i-1][j] < nums[i][j]:
		dp[i][j]=dp[i-1][j]+1
	if (i,j+1) in v and nums[i][j+1] < nums[i][j] :
		dp[i][j]=dp[i][j+1]+1
	if (i,j-1) in v and nums[i][j-1] < nums[i][j] :
		dp[i][j]=dp[i][j-1]+1
	nums_max = max(nums_max,dp[i][j])
print (dp)
print (nums_max)