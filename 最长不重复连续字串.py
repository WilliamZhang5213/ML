#滑动窗口（出现重复的时候去掉最左边的字母）

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:

# a = 'hahhahaha'
# if len(a) == 0:
#     print(0)
# elif len(set(a)) == 1:
#     print(1)
# else:
#     num = 0
#     len_list = []
#     while num < len(a)-1:
#         for i in range(num+1,len(a)):
#             if a[i] not in a[num:i]:
#                 len_list.append(i-num+1)
#                 if i == len(a)-1:
#                     if a[i] not in a[num:]:
#                         len_list.append(i - num + 2)
#                         num +=1
#                         break
#                     else:
#                         num+=1
#                         break
#             else:
#                 num+=1
#                 break
#     print(max(len_list))

a = 'pwwkew'
if len(a) == 0:
    print(0)
elif len(set(a)) == 1:
    print(1)
else:
    num = 0
    str_list = []
    a_dict = {} #利用字典去更新最新的字母的位置
    len_list = []
    for i in range(len(a)):
        if a[i] in a_dict and a_dict[a[i]] >= num:     #判断当前字符是否在字典中和当前字符的下标是否大于等于最近重复字符的所在位置   !!!!!!
            num = a_dict[a[i]]+1
        a_dict[a[i]] = i
        len_list.append(i-num+1)  #数量list
        str_list.append(a[num:i+1])  #字符list
        print(a_dict,len_list,str_list)
    print(len_list)



