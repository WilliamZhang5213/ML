#最长递增子序列
arr = [2, 1, 5, 3, 6, 4, 8, 9, 7]
# num = arr[0]
# res = [1]
# start = 1
# for i in arr[1:]:
#     if i > num:
#         start += 1
#         res.append(start)
#     else:
#         start = 1
#         res.append(1)
#     num = i
# print(res)

dp = [1]*len(arr)
for i in range(1,len(arr)):
    if arr[i-1]<arr[i]:
        dp[i]=dp[i-1]+1
print(dp)