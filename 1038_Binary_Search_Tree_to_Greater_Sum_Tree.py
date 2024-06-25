class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_level_order(arr, root, i, n):
    # Base case for recursion
    if i < n:
        if arr[i] is None:
            return None

        temp = TreeNode(arr[i])
        root = temp
        # insert left child
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)

        # insert right child
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)

    return root


def build_tree(arr):
    return insert_level_order(arr, None, 0, len(arr))


class Solution:
    def __init__(self):
        self.totalSum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        self.bstToGst(root.right)
        self.totalSum = self.totalSum + root.val
        root.val = self.totalSum
        self.bstToGst(root.left)
        return root


arr = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
root = build_tree(arr)


def inorder_traversal(root):
    if root:
        inorder_traversal(root.right)
        print(root.val, end=" ")
        inorder_traversal(root.left)


# Print the tree in-order to verify
so = Solution()
so.bstToGst(root)
inorder_traversal(root)
