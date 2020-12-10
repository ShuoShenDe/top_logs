class Node(object):
    """双向链表的结点"""

    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # next 指向下一个节点的标识
        self.next = None
        # prev 指向上一结点
        self.prev = None
