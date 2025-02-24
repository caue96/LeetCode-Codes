'''
Link to the challenge: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/
Given the root of a binary tree, return the inorder traversal of its nodes' values.

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = []
        stack = []
        curr = root
        node_count = 0
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
            node_count = node_count + 1

            # Ensure node count is between 0 and 100
            if node_count > 100:
                break
        
        return result