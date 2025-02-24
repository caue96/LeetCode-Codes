'''
Link to the challenge: https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1225/
You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.

Constraints:
The number of Nodes will not exceed 1000.
1 <= Node.val <= 10^5
'''
# This code I could not solve it, so I needed to paste this version from https://github.com/doocs/leetcode/tree/main/solution/0400-0499/0430.Flatten%20a%20Multilevel%20Doubly%20Linked%20List
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def preorder(pre, cur):
            if cur is None:
                return pre
            
            cur.prev = pre
            pre.next = cur
            t = cur.next
            tail = preorder(cur, cur.child)
            cur.child = None

            return preorder(tail, t)

        if head is None:
            return None
        
        dummy = Node(0, None, head, None)
        preorder(dummy, head)
        dummy.next.prev = None
        
        return dummy.next