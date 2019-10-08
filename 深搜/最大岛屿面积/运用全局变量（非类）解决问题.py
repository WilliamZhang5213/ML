'''
此问题中用全局变量res会混乱，
'''

def dfs(grid,x,y):
    global res
    if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1 or grid[x][y] != 1:
        return
    grid[x][y] = -1
    res+= 1
    dfs(grid,x+1,y)
    dfs(grid, x - 1, y)
    dfs(grid, x, y+1)
    dfs(grid, x, y-1)
def get_res(grid):
    global res
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                res = 0
                dfs(grid, i, j)
                print(res)

# if __name__ == '__main__':
#     grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#             [0,0,0,0,0,0,0,1,1,1,0,0,0],
#             [0,1,1,0,1,0,0,0,0,0,0,0,0],
#             [0,1,0,0,1,1,0,0,1,0,1,0,0],
#             [0,1,0,0,1,1,0,0,1,1,1,0,0],
#             [0,0,0,0,0,0,0,0,0,0,1,0,0],
#             [0,0,0,0,0,0,0,1,1,1,0,0,0],
#             [0,0,0,0,0,0,0,1,1,0,0,0,0]]
#     # get_res(grid)
#     m,n = len(grid),len(grid[0])
#     for i in range(m):
#         for j in range(n):
#             if grid[i][j]==1:
#                 global res
#                 res = 0
#                 dfs(grid,i,j)
#                 print(res)
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
res = 0
get_res(grid)