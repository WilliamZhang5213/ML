#公共子序列：不需要连续。
# 公共子串：连续.
#算法中的不同：子序列不需要归0（不需要连续，一直按顺序叠加），但子串就需要归0（一旦连续中断，归0）
# str_a = 'world'
# str_b = 'wordl'
#公共子序列
# 递归
# def get_long_xulie(str_a,str_b):
#     if len(str_a) ==0 or len(str_b) == 0:
#         return False
#     elif str_a[0] == str_b[0]:
#         return get_long_xulie(str_a[1:],str_b[1:])+1
#     else:
#         return max(get_long_xulie(str_a[1:],str_b),get_long_xulie(str_a,str_b[1:]))
# str_a = 'world'
# str_b = 'wordl'
# print(get_long_xulie(str_a,str_b))
#动态规划
# def get_long_xulie(str_a,str_b):
#     if len(str_a) ==0 or len(str_b) == 0:
#         return False
#     dp = [[0 for i in range(len(str_a)+1)] for j in range(len(str_b)+1)]
#     for i in range(1,len(str_b)+1):
#         for j in range(1,len(str_a)+1):
#             if str_b[i-1] == str_a[j-1]:
#                 dp[i][j] = dp[i-1][j-1]+1
#             else:
#                 dp[i][j] = max(dp[i-1][j],dp[i][j-1])
#     return dp[-1][-1]
# str_a = 'hahhlofl'
# str_b = 'wordl'
# print(get_long_xulie(str_a,str_b))


#最长公共子串
#当连接中断时归0
#动态规划
def get_long_xulie(str_a,str_b):
    max_l = 0
    if len(str_a) ==0 or len(str_b) == 0:
        return False
    dp = [[0 for i in range(len(str_a)+1)] for j in range(len(str_b)+1)]
    for i in range(1,len(str_b)+1):
        for j in range(1,len(str_a)+1):
            if str_b[i-1] == str_a[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
                max_l = max(dp[i][j],max_l)
            else:
                dp[i][j] = 0  #连续中断时归0
                # dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return max_l
str_a = 'hahhlofl'
str_b = 'wordlof'
print(get_long_xulie(str_a,str_b))