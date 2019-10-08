
'''
def perm(ss,end_ss,ss_list):
    if len(ss) == 1:
        ss_list.append(end_ss+ss)
    else:
        for i in range(len(ss)):
        
            # 错误的原因：每次都改变了ss，第一个字母还行（a），到第二个字母循环的时候就只剩下c了，ss被改变了
            # end_ss += ss[i]
            # css = ss[:i]+ss[i+1:]
            # print(css,end_ss,ss_list)
            # perm(css,end_ss,ss_list)
    
            perm(ss[:i]+ss[i+1:],end_ss+ss[i],ss_list)   #正确，ss也有被改变，但保证了首字母更换（大的循环开始）时ss没变,end_ss也没有改变

ss = 'abcd'
end_ss = ''
ss_list = []
perm(ss,end_ss,ss_list)
print (ss_list)
'''




def change(a,a_end,a_list):
    if len(a) == 1:
        print(a_end+a)
    else:
        for i in range(len(a)):
            change(a[:i]+a[i+1:],a_end+a[i],a_list)

a = 'abcd'
a_end = ''
a_list = []
change(a,a_end,a_list)