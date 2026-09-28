# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current, previous = head, None
        # previous is every last value so the current become previous
        # (current)1 ->(current.next)2(current)->(current.next)3(current)->None
        while current:
            temp = current.next
            current.next = previous  # As we are reversing so every next node is null
            previous = current  # every new previous is the last value
            current = temp  # We saved this as if we do directly current.next = previous we will lose the connection
        
        return previous  # As at this point current.next will be None orignal array finished and previous is the head as last element in the orignal array

        