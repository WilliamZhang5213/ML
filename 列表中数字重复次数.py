a = [2,3,3,1,2,4,3,5,2,1]
a_dict={}
for i in set(a):
    a_dict[i]=0
print(a_dict)
for i in a:
    a_dict[i]+=1
print(a_dict)