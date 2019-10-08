# def coins_changeREC_cache(coin_values, change, known_counts):
#     """
#     添加了caching的递归零钱找零，
#     用空间换时间
#     """
#     # if known_counts == None:
#     #     known_counts = [0] * (change + 1) # why plus 1? think!
#     min_count = change
#     # base case
#     if change in coin_values:
#         return 1
#     elif known_counts[change] > 0:
#         return known_counts[change]
#     for value in [i for i in coin_values if i <= change]:
#         count = 1 + coins_changeREC_cache(coin_values,
#                                           change-value,
#                                           known_counts)
#         if count < min_count:
#             min_count = count
#     known_counts[change] = min_count
#     print(known_counts)
#     return min_count
#
# n = 11
# c_list = [1,3,5]
# known_counts = [0] * (n + 1)
# num = coins_changeREC_cache(c_list,n,known_counts)
# print(num)

#爬楼梯(or 斐波那契)
# def get_way(n):
#     if n == 1:
#         return 1
#     elif n == 2 :
#         return 2
#     else:
#         dp = [0 for i in range(n+1)]
#         dp[0] = 1
#         dp[1] = 2
#         for i in range(2,n+1):
#             dp[i]=dp[i-1]+dp[i-2]
#         return dp
# a =5
# print(get_way(a))

#最大连续序列和
arr= [-2,1,-3,4,-1,2,1,-5,4]
def get_max_sum(a):
    if len(a) == 1:
        return a[0]
    else:
        dp = [0 for i in range(len(a))]
        dp[0] = a[0]
        for i in range(1,len(a)):
            dp[i] = max(a[i],dp[i-1]+a[i])
        return dp
arr= [-2,1,-3,4,-1,2,1,-5,4]
print(get_max_sum(arr))
