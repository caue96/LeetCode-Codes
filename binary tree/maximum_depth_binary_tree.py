'''
Link to the challenge: https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/535/
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Constraints:
The number of nodes in the tree is in the range [0, 10^4].
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        node_count = 0
        
        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                node_count = node_count + 1

                # Ensure number of nodes does not exceed 10^4
                if node_count > 10**4:
                    break
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth = depth + 1
        
        return depth