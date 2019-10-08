#判断一个字符串是不是回文字符串 a == a[::-1]
'''
输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
'''
#way1：遍历求解
# way2：动态规划
s = 'abccbaccdd'
k = len(s)  # 计算字符串的长度
matrix = [[0 for j in range(k)] for i in range(k)]  # 初始化n*n的列表   一个起点一个终点，所以是个n2矩阵，但这个dp矩阵存储的不是长度，而是状态
logestSubStr = ""  # 存储最长回文子串
logestLen = 0  # 最长回文子串的长度

for j in range(0, k):
    for i in range(0, j + 1):
        if j - i <= 1: #j-i<=1时i=j-1或i=j,而s[i:j]也就是s[j-1:j]或s[j:j]都是一个元素
            if s[i] == s[j]:
                matrix[i][j] = 1  # 此时f(i,j)置为true
                if logestLen < j - i + 1:  # 将s[i:j]的长度与当前的回文子串的最长长度相比
                    logestSubStr = s[i:j + 1]  # 取当前的最长回文子串
                    logestLen = j - i + 1  # 当前最长回文子串的长度
        else:
            if s[i] == s[j] and matrix[i + 1][j - 1]:  # 判断matrix[i + 1][j - 1] i+1,j-1一层层向中间缩减
                matrix[i][j] = 1
                if logestLen < j - i + 1:
                    logestSubStr = s[i:j + 1]
                    logestLen = j - i + 1
print(logestLen,logestSubStr)




