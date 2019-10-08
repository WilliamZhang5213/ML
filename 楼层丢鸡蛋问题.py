'''
问题描述：有2个鸡蛋，从100层楼上往下扔，以此来测试鸡蛋的硬度。比如鸡蛋在第9层没有摔碎，在第10层摔碎了，那么鸡蛋不会摔碎的临界点就是9层。

问：如何用最少的尝试次数，测试出鸡蛋不会摔碎的临界点？

注意：只有两个鸡蛋。第一个鸡蛋碎了，第二个鸡蛋只能挨个楼层测试了。

'''

'''
思考：临界点：max，最少的尝试次数：min ，两个鸡蛋为a、b
数学思考：假设最少需要x次，第一次：a破了：1+（x-1）=x；a没破：1+第二次。第二次：（第二次的前提是第一个已经试过了，而且没破，已存在一次）a破了：1+1+（x-2）
，因为最少需要x次，所以第二次为x-1个；a没破：1+1+第三次.......
总结 x+(x-1)+(x-2)+.....+2+1>=n   n为楼层数  100层的时候是14（神奇吧）
下面是代码思想（动态规划）
'''

# n层楼，2个鸡蛋
# def fun(n):
#     if n ==1:
#         return 1
#     else:
#         print('1')
#         return min(max(i,1+fun(n-i)) for i in range(1,n))
# print(fun(30))

# n = 100
# dp = [[0,0] for i in range(n)]
# # dp[0][0]=1
# dp[0][1]=1
# for i in range(1,n):
#     dp[i][1] = min(max(j,1+dp[i-j][1]) for j in range(1,i+1))
# print(dp)


#n层楼，m个鸡蛋
n,m = 100,2
dp = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    dp[i][0]=i+1
for i in range(m):
    dp[0][i]=1
# dp[0][0],dp[0][1],dp[0][2]=1,1,1
for i in range(1,n):
    for j in range(1,m):
        dp[i][j]=min(max(dp[start-1][j-1],1+dp[i-start][j]) for start in range(1,i+1) )
        # start = 0
print(dp)


