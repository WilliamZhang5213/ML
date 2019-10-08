num1,num2 = "123","456"
num1,num2 = num1[::-1],num2[::-1]
res = [0 for i in range(len(num1)+len(num2))]   #最大位数，当然也有可能达不到最大位数
for i in range(len(num1)):
    for j in range(len(num2)):
        res[i+j] += int(num1[i])*int(num2[j])  #这儿是+=而非=
# print(res)
ans = []
for j in range(len(res)-1):
    tmp = res[j]%10
    ans.insert(0,str(tmp))
    res[j+1]+=int(res[j]/10)
print("".join(ans))