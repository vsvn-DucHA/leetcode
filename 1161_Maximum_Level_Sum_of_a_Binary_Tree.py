from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def findmax(node: Optional[TreeNode], level: int):
            if not node:
                return
            findmax(node.left, level+1)

            if level not in self.sums:
                self.sums[level] = node.val
            else:
                self.sums[level] += node.val

            findmax(node.right, level+1)

        self.levelmax = 1
        self.sums = dict({1: root.val})
        findmax(root, 1)

        for i in self.sums:
            if self.sums[self.levelmax] < self.sums[i]:
                self.levelmax = i
            elif self.sums[self.levelmax] == self.sums[i] and i < self.levelmax:
                self.levelmax = i

        return self.levelmax
