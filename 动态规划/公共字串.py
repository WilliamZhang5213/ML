a='abdfg'
b ='weqfgdabadg'
n1,n2 = len(a),len(b)
dp = [[0 for i in range(n2+1)] for j in range(n1+1)]
for i in range(1,n1+1):
    for j in range(1,n2+1):
        if a[i-1]==b[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp)