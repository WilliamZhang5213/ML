'''
什么是字典序：[1,10,11,12,2,3,4,5,6,7,8,9]
'''

n = 101
# print([int(i) for i in sorted([str(i) for i in range(1, n+1, 1)])]) #这个方法真叼
res = [0]*n
num = 1
for i in range(n):
    res[i] = num
    if num*10 <= n:
        num*=10
    else:
        while num == n or num%10 ==9:
            num=num//10
        num+=1
print(res)