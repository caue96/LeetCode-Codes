'''
Link to the challenge: https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1228/
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        # Ensure val is between 0 and 9
        while True:
            if (0 <= val <= 9):
                break
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
         # Ensure the number of nodes in l1 and l2 is in the range 1 and 100
        def check_list_size(head):
            size = 0
            
            while head:
                size = size + 1
                head = head.next

                if size > 100:
                    break

        check_list_size(l1)
        check_list_size(l2)

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next