'''
堆排序：从小到大排序要用大顶堆！！！
'''


#二叉堆虽然是一颗完全二叉树，但它的存储方式并不是链式存储，而是顺序存储。换句话说，二叉堆的所有节点都存储在数组当中
#索引关系： 父节点索引n，则子节点索引为2n+1与2n+2（倘若没越界）



#调整父节点 与孩子大小， 制作大顶堆
def adjust_heap(data, par_node, high):

    new_par_node = par_node
    j = 2*par_node +1   #取根节点的左孩子， 如果只有一个孩子 high就是左孩子，如果有两个孩子 high 就是右孩子（par_node = length//2 -1）

    while j <= high: #如果 j = high 说明没有右孩子，high就是左孩子
        if j < high and data[j] < data[j+1]: #如果这儿不判断 j < high 可能超出索引
            # 一个根节点下，如果有两个孩子，将 j  指向值大的那个孩子（将最大的子节点与父节点交换）
            j += 1
        if data[j] > data[new_par_node]: #如果子节点值大于父节点，就互相交换
            data[new_par_node], data[j] = data[j], data[new_par_node]
            new_par_node = j #将当前节点，作为父节点，查找他的子树
            j = j * 2 + 1

        else:
            # 因为调整是从上到下，所以下面的所有子树肯定是排序好了的，
            #如果调整的父节点依然比下面最大的子节点大，就直接打断循环，堆已经调整好了的
            break


# 索引计算: 0 -->1 --->....
#    父节点 i   左子节点：偶数:2i +1  右子节点：基数:2i +2  注意：当用长度表示最后一个叶子节点时 记得 -1

# 从第一个非叶子节点(即最后一个父节点)开始，即 list_.length//2 -1（len(list_)//2 - 1）
# 开始循环到 root 索引为：0 的第一个根节点， 将所有的根-叶子 调整好，成为一个 大顶堆
def heap_sort(lst):
    """
    根据列表长度，找到最后一个非叶子节点，开始循化到 root 根节点，制作 大顶堆
    :param lst: 将列表传入
    :return:
    """
    length = len(lst)
    last = length -1  #最后一个元素的 索引
    last_par_node = length//2 -1  #最后一个父亲节点的索引

    #此while循环旨在构造大顶堆
    #构造大顶堆的思想：选择最后一个父亲节点与其子节点对比，并从最后一个父亲节点往前一次进行
    while last_par_node >= 0:  #最后父亲节点的每一个节点都是父亲节点（由下而上依次比较父亲节点与子节点）

        adjust_heap(lst, last_par_node, length-1)
        last_par_node -= 1  #每调整好一个节点，从后往前移动一个节点


    '''将大顶堆中的值输出，大顶堆中的根节点是最大值，也就是当前list的list[0],首尾对换（lst[0], lst[last] = lst[last],lst[0]）
    最大值到数组最后，最后一个值到数组头，此时list[0:last](索引0到last-1)不再是一个大顶堆，但总体上还是可以的（索引1到last-1），
    此时调整list[0],重新形成一个大顶堆，取头，向下递归
    '''
    while last > 0:

        lst[0], lst[last] = lst[last],lst[0]
        # 调整堆少让 adjust 处理最后已经排好序的数，就不处理了
        adjust_heap(lst, 0, last-1)
        last -= 1

    return lst #将列表返回

list_ = [4, 7, 0, 9, 1, 5, 3, 3, 2, 6]

heap_sort(list_)
print(list_)
