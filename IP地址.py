def getres(s,start,res,data):
    if not s:
        if start ==4:
            res.append('.'.join(data))
        # return
    if start==4:
        return    #剪枝，减少不必要的递归，大于4段的时候已经无意义，所以此时return空值，停止运行
    getres(s[1:],start+1,res,data+[s[:1]])
    if s[0] !='0':
        if len(s)>=2:
            getres(s[2:],start+1,res,data+[s[:2]])
        if len(s)>=3 and int(s[:3])<256:
            getres(s[3:],start+1,res,data+[s[:3]])

s = '2552551135'
start = 0
res = []
data = []
getres(s,start,res,data)
print(res)