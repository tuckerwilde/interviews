# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # This is where we will hold the hard copies
        d = {}
        # This is how many times we are going to copy through the list itself.
        m = n = head

        # Copy over all the nodes themselves.
        while m:
            # It's a hard/deep copy, so we need to allocate new memory for each instance of the node itself.
            d[m] = RandomListNode(m.label)
            # This means stepping through the list like normal.
            m = m.next

        # Go back through and assign the pointers themselves.
        while n:
            # Great, now we need to do more than just give each node a label. It needs it's pointers.
            d[n].next = d.get(n.next)
            # Grab all that information, since we allocated all the nodes originally.
            d[n].random = d.get(n.random)
            # Continue through the list again.
            n = n.next
        # Get the newly copied head, with all pointers intact, though they are all in new memory.
        return d.get(head)
