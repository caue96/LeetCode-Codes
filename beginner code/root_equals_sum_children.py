'''
Link to the challenge: https://leetcode.com/problems/root-equals-sum-of-children/
You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.

Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.

Constraints:
The tree consists only of the root, its left child, and its right child.
-100 <= Node.val <= 100
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
        def checkTree(self, root: Optional[TreeNode]) -> bool:
            # Ensure the tree consists only of the root, its left child, and its right child
            while True:
                if root or root.left or root.right:
                    break

            # Ensure values of all Node.val are within the given constraints
            while True:
                if (-100 <= root.val <= 100 and -100 <= root.left.val <= 100 and -100 <= root.right.val <= 100):
                    break
                
            return root.val == (root.left.val + root.right.val)