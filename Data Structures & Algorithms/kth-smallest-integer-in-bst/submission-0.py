# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.j = k
        self.res = 0
        def in_order_traversal(root):
            if root == None:
                return
            in_order_traversal(root.left)
            self.j -= 1
            if self.j == 0:
                self.res = root.val
                return
            in_order_traversal(root.right)
        in_order_traversal(root)
        return self.res