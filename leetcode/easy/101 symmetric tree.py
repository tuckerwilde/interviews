# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Parent function, just a check if root is good.
        # The function is checking symmetry AROUND the root.
        if root:
            return self.recurse(root.left, root.right)
        else:
            # An empty tree is in-itself symmetric. So return true.
            return True

    def recurse(self, left, right):
        # They are both none, so they are the same.
        if left is None and right is None:
            return True
        # If just one is none, then we know they are not the same. Immediately false.
        elif left is None or right is None:
            return False

        # So we are inside our function, let's check the two nodes we are given. If they are equal, keep diving
        if left.val == right.val:
            # The one_pair variable is always going to be on the furthest outside nodes, most left and most right
            one_pair = self.recurse(left.left, right.right)
            # two_pair is comparing the inner two values of two inner nodes.
            two_pair = self.recurse(left.right, right.left)
            # If they both are true then we will get a true, if at any point we get a false, this breaks our cycle.
            return one_pair and two_pair
        else:
            # If they're not equal, and not none, then we know we need to kick back a false.
            return False
