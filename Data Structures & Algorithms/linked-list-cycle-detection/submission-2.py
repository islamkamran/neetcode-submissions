# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Ps I am setting my friend and I was discussing the concept with him and I used the variables as his name and my name so I will use the same here also he is RAZA and I am ISLAM
        raza, islam = head, head
        # according to the floyd algorithm for cycle detection check the faster pointer for the loop and null the slow will follow as it is infinite loop so at some point in future it will catch if there is a loop other wise it will end

        # with two pointers we use while and false condition so
        while islam and islam.next:
            raza = raza.next
            islam = islam.next.next
            if raza == islam:
                return True
        return False 
        