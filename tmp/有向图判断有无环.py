'''
有向图判断有无环
'''
#3个点，有向图，1代表有联系，0代表没有

def dfs(i,j,val):
    if i<0 or i>len(val)-1 or j<0 or j>len(val[0])-1:
        return
    if val[i][j]==2:
        print(True)
        return True
    val[i][j]=2
    for i in range(len(val[j])):
        if val[j][i]==1:
            dfs(i,i,val)





# global val
val = [[0,1,0],
       [0,0,1],
       [1,0,0]]
for i in range(len(val)):
    for j in range(len(val[0])):
        if val[i][j] ==1:
            # val[i][j]=2
            print(dfs(i,j,val))


