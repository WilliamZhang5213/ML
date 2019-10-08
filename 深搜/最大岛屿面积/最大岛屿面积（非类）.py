'''
此问题中用全局变量res会混乱，
'''

def dfs(i,j,res,grid):
    res+=1
    grid[i][j] = 2
    if i-1>=0 and grid[i-1][j]==1:
        res = dfs(i-1, j, res, grid)
    if i+1<=len(grid)-1 and grid[i+1][j]==1:
        res = dfs(i+1, j, res, grid)
    if j-1>=0 and grid[i][j-1] ==1:
        res = dfs(i, j-1, res, grid)
    if j+1<=len(grid[0])-1 and grid[i][j+1]==1:
        res = dfs(i, j+1, res, grid)
    return res


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
m,n = len(grid),len(grid[0])
for i in range(m):
    for j in range(n):
        if grid[i][j]==1:
            res = 0
            res=dfs(i, j, res, grid)
            print(res)
