class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self,val):
        temp = Node(val)
        if self.head is None:
            self.head = temp
            self.tail = temp
            self.count += 1
        else:
            temp.next = self.tail
            self.tail = temp
            self.count += 1

    def dequeue(self):
        if self.head is None:
            return None
        else:
            self.count -= 1
            if self.head == self.tail:
                self.head.next = None
                temp = self.head
                self.head, self.tail = None, None
                return temp.val

            temp = self.head
            runner = self.tail
            
            while runner.next != temp:
                runner = runner.next

            self.head = runner
            runner.next = None
            return runner.val

    def peek(self):
        if self.head:
            return self.head.val
        else:
            return None


def main():
    test_queue = Queue()

    for i in xrange(10):
        test_queue.enqueue(i)

    while test_queue.peek() is not None:
        print test_queue.peek()
        test_queue.dequeue()


if __name__ == '__main__':
    main()