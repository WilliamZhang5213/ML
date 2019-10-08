'''
问题：将一个n*n的矩阵围绕中心顺时针旋转90度，输出之后的矩阵
eg：
in [[1,2],
    [3,4]]
out:[[3,1],
     [4,2]]
解决思路：行列转换，而且原先的列倒序
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        res = []

        while matrix[0]:
            tmp = []
            for row in matrix:
                tmp.insert(0, row.pop(0))  # list.insert(position,value)
            res.append(tmp)
            print(tmp,res)
        for i in range(len(matrix)):  # 这里，必须对matrix中的每行都进行修改，才能对其重新赋值，不能直接：matrix=res
            matrix[i] = res[i]


s = Solution()
matrix = [[1, 2], [3, 4]]
s.rotate(matrix)
print (matrix)