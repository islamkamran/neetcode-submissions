# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        current = head  # As we don't want to lost our intial linked list
        while current:
            if current in seen:
                return True
            seen.add(current)
            current = current.next
        return False
        