'''
Link to the challenge: https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/
AND
Link to the challenge: https://leetcode.com/explore/learn/card/linked-list/210/doubly-linked-list/1294/
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

Constraints:
0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
'''
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # Get the value of the index-th node in the linked list.
    def get(self, index: int) -> int:
        # Ensure index value is between 0 and 1000.
        while True:
            if (0 <= index <= 1000):
                break
        
        current = self.head

        for _ in range(index):
            if current is None:
                return -1
            
            current = current.next

        return current.val if current else -1

    # Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
    def addAtHead(self, val: int) -> None:
        # Ensure val value is between 0 and 1000.
        while True:
            if (0 <= val <= 1000):
                break

        new_node = Node(val, self.head)
        self.head = new_node
        self.size = self.size + 1

    # Append a node of value val as the last element of the linked list.
    def addAtTail(self, val: int) -> None:
        # Ensure val value is between 0 and 1000.
        while True:
            if (0 <= val <= 1000):
                break
        
        new_node = Node(val)

        if not self.head:
            self.head = new_node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node

        self.size = self.size + 1

    # Add a node of value val before the index-th node in the linked list. If index equals the length of the linked list, the node will be appended to the end. If index is greater than the length, the node will not be inserted.
    def addAtIndex(self, index: int, val: int) -> None:
        # Ensure val and index values are between 0 and 1000.
        while True:
            if (0 <= val <= 1000 and 0 <= index <= 1000):
                break
        
        if index == 0:
            self.addAtHead(val)
        else:
            new_node = Node(val)
            current = self.head

            for _ in range(index - 1):
                if current is None:  # Prevent NoneType error
                    return
                
                current = current.next
            
            if current is None:
                return

            new_node.next = current.next
            current.next = new_node
            self.size = self.size + 1

    # Delete the index-th node in the linked list, if the index is valid.
    def deleteAtIndex(self, index: int) -> None:
        #Ensure index value is between 0 and 1000.
        while True:
            if (0 <= index <= 1000):
                break
        
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head

            for _ in range(index - 1):
                if current is None or current.next is None:
                    return
                
                current = current.next
                
            if current.next:
                current.next = current.next.next

        self.size = self.size - 1