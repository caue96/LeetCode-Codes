'''
Link to the challenge: https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
'''
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Ensure val is between -1000 and 1000
        while True:
            if (-1000 <= val <= 1000):
                break
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Ensure targetSum is between -1000 and 1000
        while True:
            if (-1000 <= targetSum <= 1000):
                break
        
        if not root:
            return False
        
        stack = [(root, root.val)]

        while stack:
            node, curr_sum = stack.pop()

            if not node.left and not node.right and curr_sum == targetSum:
                return True
            if node.right:
                stack.append((node.right, curr_sum + node.right.val))
            if node.left:
                stack.append((node.left, curr_sum + node.left.val))
        
        return False