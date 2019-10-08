#栈，stack，先入后出（first in last out）
#队列，queue，先入先出
# 问题：（）[] {}的对应，如果是正确的结果，返回true，错误的返回false（eg:][ 或者 ([)]）,不符合正确结构的都返回false。

#方法1：replace掉
# a = '[[[[[([{}{}()])]]]]]'
# for i  in range(len(a)//2) :
#     a = a.replace('()','').replace('[]','').replace('{}','')
# if len(a) == 0:
#     print(True)
# else:
#     print(False)

#方法2：先入后出，栈的方式
a = '[[[[[([{}{}))])]]]]]'
need_dict = {')':'(',']':'[','}':'{'}
stack = []
for i in a:
    if i not in need_dict:
        stack.append(i)
    elif not stack or need_dict[i] != stack.pop():
        print(False)
print(stack)
if stack == []:
    print(True)
