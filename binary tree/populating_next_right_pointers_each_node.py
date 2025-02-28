'''
Link to the challenge: https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/994/
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Constraints:
The number of nodes in the tree is in the range [0, 2^12 - 1].
-1000 <= Node.val <= 1000

Follow-up:
You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
'''
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        # Ensure val is between -1000 and 1000
        while True:
            if (-1000 <= val <= 1000):
                break
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        leftmost = root
        node_count = 1
        
        while leftmost.left:
            head = leftmost

            while head:
                head.left.next = head.right
                
                if head.next:
                    head.right.next = head.next.left
                
                head = head.next
                node_count = node_count + 2

            # Ensure the number of nodes is less than 2^15 - 1
            if node_count > 4095:
                return

            leftmost = leftmost.left
        
        return root