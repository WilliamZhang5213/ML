#递归问题如果递归的话找好状态转移方程
#已知小明上楼梯时每次只能跨1~2个阶梯，假定小明从地面(第0阶)开始上台阶，要上到第m个阶梯共有多少种走法并输出走法
#时间复杂度log（2**n）
# def jump(m):
#     if m == 1:
#         return 1
#     elif m == 2:
#         return 2
#     elif m > 2:
#         return sum([jump(m-1),jump(m-2)])
# print(jump(5))


#时间复杂度n（理解：走到楼梯n的方法数= 走到楼梯n-1的方法数+走到楼梯n-2的方法数）
def jump(m):
    if m == 1:
        return 1
    elif m == 2:
        return 2
    elif m > 2:
        beg_l = [0,1,2]
        for i in range(3,m):
            print(i,beg_l)
            beg_l.append(beg_l[i-2]+beg_l[i-1])
        return beg_l

print(jump(8))
