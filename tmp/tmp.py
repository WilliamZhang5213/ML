
def get():
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                global tmp
                tmp = 0
                ntmp=dfs(i,j,tmp)
                print(ntmp)
def dfs(i,j,tmp):
    if i<0 or i>len(grid)-1 or j<0 or j>len(grid[0])-1 or grid[i][j]!=1:
        return
    tmp+=1
    grid[i][j]=2
    dfs(i-1,j,tmp)
    dfs(i+1,j,tmp)
    dfs(i,j-1,tmp)
    dfs(i,j+1,tmp)
    print(tmp)
    return tmp



grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
get()