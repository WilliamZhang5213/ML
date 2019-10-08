#有1/3/5三种硬币，换取n元钱的最少硬币数量


#递归1
# def charge(n):
#     if n < 0:
#         return False
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n ==2 :
#         return 2
#     elif n == 3:
#         return 1
#     elif n == 4:
#         return 2
#     elif n == 5:
#         return 1
#     else:
#         return min(int(charge(n-1))+1,int(charge(n-3))+1,int(charge(n-5))+1)
# n = 39
# print(charge(n))


#递归2  (更普及，为了应对出现负值的情况，提前进行设置)
# n = 11
# # c_list = [1,3,5]
# def charge(n,c_list):
#     if n in c_list:
#         return 1
#     else:
#         return min([charge(n-i,c_list)+1 for i in c_list if n >= i])
# n = 24
# c_list = [1,3,5]
# print(charge(n,c_list))

#递归3 （递归很耗时，添加记忆器,假如c_list = [1,3,5],n= 30,三条路径都会经过15这一个节点,没记忆器的情况下会重复计算三次
#    记忆器:以空间换时间）]
def charge(n,c_list,n_remember):
    min_count = n
    if n in c_list:
        return 1
    elif n_remember[n] > 0:
        return n_remember[n]
    for i in c_list:
        if n >= i:
            num = 1+charge(n,c_list,n_remember)
        if num < min_count:
            min_count = num
        # min_count = min(min_count,num)
    n_remember[n] = min_count

n = 24
c_list = [1,3,5]
n_remember = [0]* (n+1)
print(charge(n,c_list,n_remember))
