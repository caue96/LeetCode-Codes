'''
Link to the challenge: https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/536/
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
'''
from collections import deque

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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
         # Ensure number of nodes is at least 1
        if not root:
            return True
        
        queue = deque([(root.left, root.right)])
        
        while queue:
            left, right = queue.popleft()
            
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        
        return True