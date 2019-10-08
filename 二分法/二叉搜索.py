#递归中return要跟着递归，return递归函数，继续运行
def ercha(a,num):
    start = 0
    end = len(a)
    mid = len(a)//2
    # print(mid,a)
    if a[mid] > num:
        end = mid
        return ercha(a[start:end + 1], num)
    elif a[mid] < num:
        start = mid
        return ercha(a[start:end+1],num)
    else:
        return a[mid]


def ercha2(a,num):
    start = 0
    end = len(num)-1
    while start<=end:
        # mid = int((start+end)/2)
        mid = (start+end)//2
        print(start,end,mid)
        if num[mid] == a:
            return mid
        elif num[mid] >a:
            end = mid-1
        else:
            start = mid+1
    return False
num = [1,2,3,4,5,6,7,8,9,10]
a = 11
b = ercha2(a,num)
print(b)