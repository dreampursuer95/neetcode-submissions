# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Keep a hashmap of each height
        height_map = dict()

        def post_order_traversal(node, depth):
            if node == None:
                return
            if depth not in height_map:
                height_map[depth] = node.val
            post_order_traversal(node.right, depth + 1)
            post_order_traversal(node.left, depth + 1)
        
        post_order_traversal(root, 0)
        ans_list = []
        for key, val in height_map.items():
            ans_list.append(val)
        return ans_list
