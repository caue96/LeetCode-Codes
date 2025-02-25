'''
Link to the challenge: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/931/
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''
from typing import Optional, List
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Ensure that number of nodes is bigger than 0
        if not root:
            return []
        
        result = []
        queue = deque([root])
        node_count = 0 
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                node_count = node_count + 1
                
                # Ensure number of nodes does not exceed 2000
                if node_count > 2000:
                    break
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result