'''
由字符串A转化为字符串B的最小编辑次数。允许的编辑操作有：删除，插入，替换
'''
a = 'beauty'
b = 'beauy'
m,n = len(a),len(b)
dp =[[0 for i in range(len(a)+1)]for j in range(len(b)+1)]
for i in range(len(a)+1):
    dp[0][i]= i
for j in range(len(b)+1):
    dp[j][0] = j
for i in range(1,n+1):
    for j in range(1,m+1):
        if b[i-1] == a[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)  #这三个状态分别对应着插入、删除、替换
print(dp[m][n])