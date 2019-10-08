'''
每个IP段的范围是0-255
类型：运用了全局变量res，没有传参
'''
def dfs(s,start,res,data):
    if not s:
        if start==4:
            res.append(data[:-1])
        return
    if start==4:
        return
    dfs(s[1:],start+1,res,data+s[:1]+'.')
    if s[0] !=0:
        # if len(s)
        dfs(s[2:],start+1,res,data+s[:2]+'.')
        if int(s[:3])<=255:
            dfs(s[3:],start+1,res,data+s[:3]+'.')


s = '2552551135'
start = 0
res = []
data = ''
dfs(s,start,res,data)
print(set(res))