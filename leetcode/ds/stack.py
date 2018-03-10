class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, val):
        if self.head is None:
            self.head = Node(val)
            self.count += 1
        else:
            temp = Node(val)
            temp.next = self.head
            self.head = temp
            self.count += 1

    def pop(self):
        if self.head is None:
            print "Empty Stack, cannot pop"
            return None
        else:
            temp = self.head
            self.head = self.head.next
            self.count -= 1
            return temp

    def peek(self):
        if self.head:
            return self.head.val
        else:
            return None


def main():
    test_stack = Stack()

    for i in xrange(10):
        test_stack.push(i)

    while test_stack.peek():
        print test_stack.peek()
        test_stack.pop()


if __name__ == '__main__':
    main()
