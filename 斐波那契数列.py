# a =[1,1,2,3,5,8,13,21,34,...]  f(n)=f(n-1)+f(n-2)
def fi(n):
    if n == 1 or n==2:
        return 1
    else:
        print(1)
        return int(fi(n-1))+int(fi(n-2))

a = fi(10)
print(a)