def change(nums,last_node,end):
    last_parent_node_child = 2*last_node + 1
    while last_parent_node_child <= end:
        if last_parent_node_child < end and nums[last_parent_node_child] < nums[last_parent_node_child+1]:
            last_parent_node_child += 1
        if nums[last_node] < nums [last_parent_node_child]:
            nums[last_node],nums [last_parent_node_child] =nums [last_parent_node_child],nums[last_node]
            # 解析：为什么此处用while而且下面继续进行递归？
            #当到了上一层时，父节点要与子节点以及子节点的子节点比较，确保整体有序
            #往下走，子节点变为父节点
            last_node = last_parent_node_child
            last_parent_node_child = 2*last_parent_node_child+1
        else:
            break

list_ = [4, 7, 0, 9, 1, 5, 3, 2, 6]
length = len(list_)
last = length - 1
last_parent_node = length//2-1
#构建大顶堆
while last_parent_node >= 0:
    change(list_,last_parent_node,last)
    last_parent_node -= 1
#大顶堆构造完成，开始排序取数
print(list_)
while last >= 0:
    list_[0],list_[last] = list_[last],list_[0]
    change(list_,0,last-1)
    last -= 1
print(list_)
