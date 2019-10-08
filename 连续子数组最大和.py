# 暴力求解
# a = [1, -2, 3, 10, -4, 7, 2, -5,8]
# num = 0
# for i in range(len(a)):
#     for j in range(i,len(a)+1):
#         num = max(num,sum(a[i:j]))
# print(num)

#动态规划
a = [1, -2, 3, -10, -4, 7, 2, -5]
num = a[0]
start = 0
sum_list=[num]
num_list = [[num]]
for i in a[1:]:
    num = max(i,num+i)
    sum_list.append(num)
    if num == i:
        start = a.index(i)
        num_list.extend([i])
    else:
        num_list.append(a[start:a.index(i)+1])
print(sum_list,num_list)