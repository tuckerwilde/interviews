class TreeNode:
    def __init__(self, left=None, right=None, val=None):
        self.val = val
        self.right = right
        self.left = left

class BST:
    def __init__(self):
        self.root = None

    def insert(self,val):
        node = TreeNode(val=val)
        if self.root is None:
            self.root = node
        else:
            root = self.root
            while root is not None:
                if root.val > node.val:
                    if root.left is None:
                        root.left = node
                        break
                    else:
                        root = root.left
                else:
                    if root.right is None:
                        root.right = node
                        break
                    else:
                        root = root.right

    def delete(self,val):
        """
        TODO: Do this.
        :param val:
        :return:
        """

    def printInOrder(self, root):
        if root:
            self.printInOrder(root.left)
            print root.val
            self.printInOrder(root.right)


def main():
    test_bst = BST()

    test_bst.insert(100)
    test_bst.insert(50)
    test_bst.insert(40)
    test_bst.insert(75)
    test_bst.insert(60)
    test_bst.insert(65)
    test_bst.delete(50)
    test_bst.printInOrder(test_bst.root)

if __name__ == '__main__':
    main()