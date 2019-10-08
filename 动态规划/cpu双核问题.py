# 题目的大概意思：一种双核CPU的两个核能够同时的处理任务，现在有n个已知数据量的任务需要交给CPU处理，假设已知CPU的每个核1秒可以处理1kb，每个核同时只能处理一项任务。n个任务可以按照任意顺序放入CPU进行处理，现在需要设计一个方案让CPU处理完这批任务所需的时间最少，求这个最小的时间。
# he = 2
# n = 8
# nval = [3,6,8,10,3,21,5,32]
# dp = [[0]* (he+1) for i in range(n+1)]
# for i in range(1,n+1):
#     for j in range(1,he+1):

w = [0, 3072, 3072, 7168, 3072, 1024]
trans_lamb = lambda x: x/1024
w = list(map(trans_lamb,w))
print(sum(w)/2)