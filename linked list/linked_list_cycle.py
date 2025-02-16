'''
Link to the challenge: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Constraint: The number of nodes is in the range [0, 10^4]
 
        # Ensure exist at least a node
        if not head:
            return False

        slow = head
        fast = head
        count = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count = count + 1

            if slow == fast:
                return True
            
            # Return false in case the number of nodes in the list exceed 10^4
            if count > 10**4:
                break

        return False