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
# This code I could not solve it, so I needed to paste this version from https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0142.Linked%20List%20Cycle%20II/README_EN.md
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                ans = head

                while ans != slow:
                    ans = ans.next
                    slow = slow.next

                return ans