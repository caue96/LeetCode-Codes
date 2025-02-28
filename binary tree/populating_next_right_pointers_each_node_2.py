'''
Link to the challenge: https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/1016/
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Constraints:
The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100

Follow-up:
You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
'''
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        # Ensure val is between -100 and 100
        while True:
            if (-100 <= val <= 100):
                break
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        curr = root
        dummy = Node(0)
        node_count = 1
        
        while curr:
            prev = dummy
            
            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev = prev.next
                    node_count = node_count + 1
                
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next
                    node_count = node_count + 1
                
                curr = curr.next
            
            # Ensure the number of nodes is less than 6001
            if node_count > 6001:
                return

            curr = dummy.next
            dummy.next = None
        
        return root