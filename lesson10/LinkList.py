class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def find(self, target):
        node = self.head
        while node is not None and node.data != target:
            node = node.next
        return node

    def add(self, data):
        newNode = ListNode(data)
        newNode.next = self.head
        self.head = newNode

    def remove(self, target):
        assert self.find(target) is not None, "target not in list"
        pre = None
        node = self.head
        while node is not None and node.data != target:
            pre = node
            node = node.next
        if pre is None:
            self.head = node.next
        else:
            pre.next = node.next

    def __iter__(self):
        return ListIT(self.head)

class ListIT:
    def __init__(self, node):
        self.curr = node

    def __next__(self):
        if self.curr is None:
            raise StopIteration
        else:
            data = self.curr.data
            self.curr = self.curr.next
            return str(data)

    def __iter__(self):
        return self

if __name__ == '__main__':
    l = LinkList()
    l.add("a")
    l.add("b")
    l.add("c")
