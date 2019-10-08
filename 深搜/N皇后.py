'''
在N*N的方格棋盘放置了N个皇后，使得它们不相互攻击（即任意2个皇后不允许处在同一排，同一列，也不允许处在与棋盘边框成45角的斜线(不仅仅是左右对角线)上。
你的任务是，对于给定的N，求出有多少种合法的放置方法。
思路：
判断皇后冲突时，
1. 横向冲突就是Y相同，X不同的位置上出现了别的Q
2. 竖向冲突就是X相同，Y不同的位置上出现了别的Q
check_zhi
3. /向冲突就是 X + Y的和 相同的坐标上出现了别的Q
4. \向冲突就是 Y - X的差 相同的坐标上出现了别的Q
check_xie

n=1 1
n=2 0
n=3 0

'''
import copy
def check_zhi(a,b):
    label = True
    for i in range(n):
        if dp[a][i] == 1 or dp[i][b]==1:
            label = False
            break
    return label
def check_xie(a,b):
    label = True
    for i in range(1,n):
        if a-i>=0 and b-i>=0 and dp[a-i][b-i]==1:
            label = False
            break
        if a+i<=n-1 and b+i<=n-1 and dp[a+i][b+i]==1:
            label = False
            break
        if a-i>=0 and b+i<=n-1 and dp[a-i][b+i]==1:
            label = False
            break
        if a+i<=n-1 and b-i>=0 and dp[a+i][b-i]==1:
            label = False
            break
    return label

def dfs(a,b):
    global res
    global end
    if check_zhi(a,b) and check_xie(a,b): #（a,b）为横纵坐标，对这个位置进行判断，判断此位置是否可以放皇后
        dp[a][b] = 1 #放下皇后
        if a == n-1: #如果到了最后一行，结束
            tmp = copy.deepcopy(dp)
            end.append(tmp) #end是每一个可行方案，这儿需要深复制，dp在下面会还原，不深复制后面都会变成0
            res+=1 #res是结果的数量，每到这一步说明多一个可行解
        else:
            for i in range(n):
                dfs(a+1,i) #对下一行的每一列进行测试
        dp[a][b] = 0 #回溯，要移除皇后，恢复，进行之后的遍历

n = 5
end = []
res = 0
dp = [[0 for i in range(n)] for j in range(n)] #生成一个空棋盘（还没放皇后）
for i in range(n):
    dfs(0,i) #0为行，i为列，最外层的一层循环
print(end)
print(res)

