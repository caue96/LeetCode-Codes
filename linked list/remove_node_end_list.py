'''
Link to the challenge: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''
class ListNode:
    def __init__(self, val=0, next=None):
        # Ensure Node val is between 0 and 100
        while True:
            if (0 <= val <= 100):
                break
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        temp = head

        # Ensure sz value is between 1 and 30
        while temp:
            sz = sz + 1
            temp = temp.next

            if sz > 30:
                return

        # Ensure n value is between 1 and sz
        while True:
            if (1 <= n <= sz):
                break
        
        dummy = ListNode(0)
        dummy.next = head
        
        slow = dummy
        fast = dummy
        
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return dummy.next