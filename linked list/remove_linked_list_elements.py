'''
Link to the challenge: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Constraints:
The number of nodes in the list is in the range [0, 10^4].
1 <= Node.val <= 50
0 <= val <= 50
'''
class ListNode:
    def __init__(self, val=0, next=None):
        # Ensure val is between 0 and 50
        while True:
            if 0 <= val <= 50:
                break
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        while curr:
            # Ensure curr.val is between 1 and 50
            if 1 > curr.val or curr.val > 50:
                return
            elif curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return dummy.next