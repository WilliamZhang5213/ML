# 给你一根长度为n的绳子，请把绳子剪成m段 (m和n都是整数，n>1并且m>1)每段绳子的长度记为k[0],k[1],…,k[m].请问k[0]k[1]…*k[m]可能的最大乘积是多少？例如，当绳子的长度为8时，我们把它剪成长度分别为2,3,3的三段，此时得到的最大乘积是18.
# 递归问题都有终结值（否则会进入无限循环），考虑每个问题的极端情况，像本题1》1、2》2、3》3，而4的时候就可以下分了，也就是可以递归。
# def cut(i):
#     if i == 1:
#         return 1
#     elif i == 2:
#         return 2
#     elif i == 3:
#         return 3
#     else:
#         return max([cut(i-1),2*cut(i-2),3*cut(i-3)])
# print(cut(30))

# # -*- coding:utf-8 -*-
# '''
# description:
#  name：剪绳子
#  内容：给你一根长度为n的绳子，请把绳子剪成m段(n>1,m>1)，每段绳子的长度即为k[0],k[1]....k[m],请问k[0]*k[1]*..*k[m]可能的最大乘积是多少
# '''
#
#
# class Solution:
#     def dynamic_programming(self, n):
#         if n < 2:
#             return 0
#         if n == 2:
#             return 1
#         if n == 3:
#             return 2
#         tmp_lst = [0, 1, 2, 3]  #最初的答案，记忆器
#
#         for i in range(4, n + 1):
#             max = 0
#             for j in range(1, i // 2 + 1):
#                 print(i,j,i-j,tmp_lst[j],tmp_lst[i - j])
#                 tmp = tmp_lst[j] * tmp_lst[i - j]
#                 if max < tmp:
#                     max = tmp
#             tmp_lst.append(max)
#         return tmp_lst
#
#     '''
#     我发可以发现当n<=3时如果再剪一刀那么结果肯定小于未剪时的值，而当n>3时继续剪肯定会存在大于等于未剪时的数
#     即我们将长为n的数一直剪下去知道碰到剩下的小于4时结束
#     '''
#
#     def greedy_algorithm(self, n):
#         if n < 2:
#             return 0
#         if n == 2:
#             return 1
#         if n == 3:
#             return 2
#         multi_3 = 0
#         while n > 4:
#             multi_3 += 1
#             n -= 3
#         return 3 ** multi_3 * n
#
#
# s = Solution()
# print(s.dynamic_programming(8))
# # print(s.greedy_algorithm(4))

#n的乘机结果 = max（max（n-2）*2，max（n-3）*3） 正序 加记忆器
def cut(n):
    if n == 2:
        return 2
    if n == 3:
        return 3
    else:
        beg_l = [0,0,2,3]
        for i in range(4,n+1):
            beg_l.append(max(beg_l[i-2]*2,beg_l[i-3]*3))
            print(beg_l)

cut(8)