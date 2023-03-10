# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrder(self, root: Optional[TreeNode], answer: List[int]):
        if root:
            if root.left:
                self.inOrder(root.left, answer)
            answer.append(root.val)
            if root.right:
                self.inOrder(root.right, answer)
        
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        self.inOrder(root, answer)
        return answer
        
        