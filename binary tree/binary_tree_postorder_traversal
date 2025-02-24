'''
Link to the challenge: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Ensure val is between -100 and 100
        while True:
            if (-100 <= val <= 100):
                break
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        result = []
        stack = [root]
        node_count = 0
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.left:
                stack.append(node.left)
                node_count = node_count + 1
            if node.right:
                stack.append(node.right)

        return result[::-1]