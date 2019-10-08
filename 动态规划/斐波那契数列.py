# a =[1,1,2,3,5,8,13,21,34,...]  f(n)=f(n-1)+f(n-2)
#递归
# def fi(n):
#     if n == 1 or n==2:
#         return 1
#     else:
#         print(1)
#         return int(fi(n-1))+int(fi(n-2))
#
# a = fi(10)
# print(a)

#记忆化递归(自下而上)
# def fi(i):
#     if i == 1 or i == 2:
#         return 1
#     else:
#         val = [0,1,1]
#         for num in range(3,i+1):
#             val.append(val[num-1]+val[num-2])
#             print(val)
# fi(10)

val=[0,1,1]
def fi(n):
    # print(n,val)
    # val = [0,1,1]
    if n == 1 or n==2:
        return 1
    elif len(val) > n:
        # print('val'+val)
        return val[n]
    else:
        val.append(fi(n-1)+fi(n-2))
        print(val)
        return val[-1] #return的必须是个值，因为append里面有+，list与int相加会报错
print(fi(6))


