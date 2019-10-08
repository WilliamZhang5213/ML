class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = ListNode(-1)
        h.next = head
        pre = h
        while pre.next != None and pre.next.next != None:
            #找到三个节点
            node1 = pre.next
            node2 = node1.next
            lat = node2.next
#交换顺序
            pre.next = node2
            node2.next = node1
            node1.next = lat

            pre = node1

        return h.next
