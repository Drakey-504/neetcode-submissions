# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head is None or head.next is None:
            return False

        one_step = head
        two_step = head

        while True:
            one_step = one_step.next
            two_step = two_step.next
            if two_step:
                two_step = two_step.next

            if one_step is None or two_step is None:
                return False

            if one_step == two_step:
                return True      

        return True            
        



        