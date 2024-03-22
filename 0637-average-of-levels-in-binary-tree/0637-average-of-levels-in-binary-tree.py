# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.values = defaultdict(list)
        self.max_index = 0
        if not root:
            return []
        self.calculateAverage(root, 0)
        return [
            sum(self.values[index]) / len(self.values[index])
            for index in range(self.max_index + 1)
        ]
            
    def calculateAverage(self, node: Optional[TreeNode], index):
        self.values[index] += [node.val]
        self.max_index = max(self.max_index, index)
        if node.left:
            self.calculateAverage(node.left, index + 1)
        if node.right:
            self.calculateAverage(node.right, index + 1)