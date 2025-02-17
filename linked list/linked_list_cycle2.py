'''
Link to the challenge: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Constraints:
The number of the nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.
'''
class ListNode:
    def __init__(self, x):
        # Ensure x value is between -10^5 and 10^5
        while True:
            if (-10**5 <= x <= 10**5):
                break
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Ensure exist at least a node
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        count = 0
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count = count + 1
            
            if slow == fast:
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                    
                return slow
            
            # Return none in case the number of nodes in the list exceed 10^4
            if count > 10**4:
                break
        
        return None