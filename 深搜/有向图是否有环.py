'''
判断一个有向图是否有环，[4，5]表示4指向5
'''
def dfs(i,val,rec):
    global label
    if val[i][0] in rec:
        label = True
        return
    else:
        rec.append(val[i][0])
    for j in range(len(val)):
        if val[j][0]==val[i][1]:
            dfs(j,val,rec)




val = [[3,4],[1,3],[2,3],[4,9],[1,2],[2,1]]
for i in range(len(val)):
    label = False
    rec = []
    dfs(i,val,rec)
    print(label)
    print(rec)

#第二种有向图的表现形式（转化为第一种）
# data = [[0,1,0],[0,0,1],[1,0,0]]
# val = []
# for i in range(len(data)):
#     for j in range(len(data[0])):
#         if data[i][j]==1:
#             val.append([i+1,j+1])
# print(val)
