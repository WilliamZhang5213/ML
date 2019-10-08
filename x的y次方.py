'''
二分的思想
'''
def jisuan(x,y):
    if y ==0 :
        return 1
    half = jisuan(x,y//2)
    if y%2==0:
        return half*half
    else:
        return half*half*x
print(jisuan(3,4))


