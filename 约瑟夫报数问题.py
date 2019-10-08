'''
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位
'''
n,m = 8 ,3
dp = [i for i in range(n)]
start = 0
while len(dp)>1:
    tmp = []
    for i in dp:
        start +=1
        if start%m == 0 :
            # dp.remove(i)    这儿不可以直接remove，remove之后上面的循环被破坏
            tmp.append(i)
    dp =list(set(dp)-set(tmp))
print(dp)
