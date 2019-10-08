'''
队列：appendTail,deleteHead
栈：push,pop
'''

#两个栈实现队列
'''
因为栈是后进先出的数据结构，当将数据依次压入第一个栈后，再依次从这个栈弹出，压入第二个栈，如果此时从第二个栈中获取数据，表现正好像一个 “先进先出” 的队列数据结构。
注意用栈（append与pop）实现队列（append与pop（0））
'''
class QueueWithTwoStacks(object):
    def __init__(self):
        self._stack1 = []
        self._stack2 = []

    def appendTail(self,x):
        self._stack1.append(x)  #_stack1存放入队列的元素

    def deleteHead(self):
         if self._stack2:
             return self._stack2.pop()
         else:
             if self._stack1:
                while self._stack1:
                    self._stack2.append(self._stack1.pop())
                return self._stack2.pop()
             else:
                 return None


#两个队列实现栈
'''
push()操作：

       为了保证先进栈的元素一直在栈底，需要将两个队列交替使用，才能满足需求。因此，想法是，我们只在空的那个队列上添加元素，然后把非空的那个队列中的元素全部追加到当前这个队列。这样一来，我们又得到一个空的队列，供下一次添加元素。

       pop()操作：

       因为在添加元素时，我们已经按照进栈的先后顺序把后进栈的元素放在一个队列的头部，所以出栈操作时，我们只需要找到那个非空的队列，并依次取出数据即可。
'''
class StackWithTwoQueues(object):
    def __init__(self):
        self._stack1 = []
        self._stack2 = []

    def push(self,x):
        if len(self._stack1) == 0:
            self._stack1.append(x)
        elif len(self._stack2) == 0:
            self._stack2.append(x)
        if len(self._stack2) == 1 and len(self._stack1) >= 1:
            while self._stack1:
                self._stack2.append(self._stack1.pop(0))
        elif len(self._stack1) == 1 and len(self._stack2) > 1:
            while self._stack2:
                self._stack1.append(self._stack2.pop(0))

    def pop(self):
        if self._stack1:
            return self._stack1.pop(0)
        elif self._stack2:
            return self._stack2.pop(0)
        else:
            return None