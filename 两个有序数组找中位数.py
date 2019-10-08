def getmid(l1,l2):
    m,n = len(l1),len(l2)
    #保证短的数组在前
    if m>n:
        m,n=n,m
        l1,l2 = l2,l1
    start = 0
    end = m
    mid = (m+n+1)//2
    while start<=end:
        i=(start+end)//2
        j=mid-i
        if l2[j]<l1[i-1]:
            end = i
        elif l1[i]<l2[j-1]:
            start = i
        else:
            if i==0:
                maxleft = l2[j-1]
            elif j==0:
                maxleft = l1[i-1]
            else:
                maxleft = max(l1[i-1],l2[j-1])
            if (m+n)&1==1:
                return maxleft
            if i == m:
                minright = l2[j]
            elif j == n:
                minright = l1[i]
            else:
                minright = min(l1[i],l2[j])
            return (maxleft,minright)


l1 = [2,5,6,9,10]
l2 = [1,2,3,7,12]
# l1 = [3, 5, 6, 7, 8, 12, 20]
# l2 = [1, 10, 17, 18]
print(getmid(l1,l2))