class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # This is the iterative way, which requires a manual manipulation of a stack
        stack = []
        # Our return value
        ret = []
        # Either, while we have stack items to pop, or while there are still items in the tree
        while stack or root:
            # If we are at a root, we can go left until none
            if root:
                # Push the node to the stack
                stack.append(root)
                # Go left!
                root = root.left
            else:
                # We have hit the end of the road, I.E. far left until we hit None
                # Let's move back up one from the stack
                root = stack.pop()
                # Grab that nodes value
                ret.append(root.val)
                # Now, we need to go right.
                root = root.right
        return ret

    def inorder_recursive(self, root):
        """
        :param root:
        :return: List[int]
        """
        ret = []
        self.helper_recurse(root, ret)
        return ret

    def helper_recurse(self, root, arr):
        if root:
            self.helper_recurse(root.left, arr)
            arr.append(root.val)
            self.helper_recurse(root.right, arr)