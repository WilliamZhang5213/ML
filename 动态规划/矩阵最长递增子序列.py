matrix=[
    [1,2,4,3],
    [4,5,3,6],
    [7,8,10,9]
]
m = len(matrix)
n = len(matrix[0])
dp = [[1 for i in range(n)]for j in range(m)]
matrix_dict = {}
for i in range(m):
    for j in range(n):
        matrix_dict[(i,j)] = matrix[i][j]
matrix_dict_key = matrix_dict.keys()
matrix_list = sorted(matrix_dict,key=lambda x:x[1])
print(matrix_list)
for k in matrix_list:
    i = k[0]
    j = k[1]
    if (i+1,j) in matrix_list and matrix[i+1][j] < matrix[i][j]:
        dp[i][j] = dp[i+1][j]+1
    if (i-1,j) in matrix_list and matrix[i-1][j] < matrix[i][j]:
        dp[i][j] = dp[i-1][j]+1
    if (i,j+1) in matrix_list and matrix[i][j+1] < matrix[i][j]:
        dp[i][j] = dp[i][j+1]+1
    if (i,j-1) in matrix_list and matrix[i][j-1] < matrix[i][j]:
        dp[i][j] = dp[i][j-1]+1
print(dp)